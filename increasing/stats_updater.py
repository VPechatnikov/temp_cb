import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'increasing_api.settings'

import sys
import argparse
import requests
import json
import logging
from twisted.internet import task
from twisted.internet import reactor
from increasing.models import PageStats

log = logging.getLogger("stats_updater")

#hardcoded for POC, should move to env configuration (e.g. environment variables)
TOPPAGES_URL = "http://api.chartbeat.com/live/toppages/?apikey=317a25eccba186e0f6b558f45214c0e7&host={}&limit=100"
HOSTS_URL = "https://s3.amazonaws.com/interview-files/hosts.json"

def run_stats_updater(update_threshold, hosts):
    for host in hosts:
        try:
            toppagesresp = requests.get(TOPPAGES_URL.format(host), headers={'x-li-format': 'json'})
            toppages_data = json.loads(toppagesresp.text)
            for page_data in toppages_data:
                try:
                    page_stats, created = PageStats.objects.get_or_create(host=host, page_path=page_data['path'])
                    new_data = page_data['visitors']
                    page_title = page_data.get('i')
                    if page_title:
                        page_stats.page_title = page_title
                    
                    new_avg = (new_data + (page_stats.num_new_points * (page_stats.new_avg or 0)))/(page_stats.num_new_points+1)
                    num_new_points = page_stats.num_new_points + 1
                    if num_new_points >= update_threshold:
                        if page_stats.cur_avg is not None and page_stats.new_avg is not None:
                            increasing_flag = new_avg > page_stats.cur_avg
                            if increasing_flag != page_stats.increasing:
                                log.debug(u'host {} page {}, direction changed.  Increasing: {}'.format(host, page_title, increasing_flag))
                            page_stats.increasing = increasing_flag
                            page_stats.last_speed = new_avg - page_stats.cur_avg
                        page_stats.new_avg = 0
                        page_stats.num_new_points = 0
                        page_stats.cur_avg = new_avg
                    else:
                        page_stats.new_avg = new_avg
                        page_stats.num_new_points = num_new_points
                    page_stats.save()
                except:
                    log.exception('Unable to process page data')  #TODO log more info about it

                #TODO -- handle case where page drops off the toppages list (top 100 for this POC) --> purge from page_stats
        except:
            log.exception('Unable to get toppages info for host {}'.format(host)) #TODO - handle different error scenarios separately


if __name__ == '__main__':

    #Looking at change directionality between just two data points isn't a stable measure of overall growth in viewership, so
    #this uses a sampling approach, comparing the avg num viewers over "update_threshold" number of data points,
    #sampled at intervals of length "interval"
    
    import django
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", default=5, type=float, help='interval between data point collection, in seconds')
    parser.add_argument("--hosts_url", default=HOSTS_URL)
    parser.add_argument("--update_threshold", default=5, type=int, help='number of data points to collect before updating increasing flag')
    args = parser.parse_args()

    
    try:
        hostsresp = requests.get(args.hosts_url, headers={'x-li-format': 'json'})
        hosts = json.loads(hostsresp.text)
    except Exception as e:
        err = 'Unable to load hosts list {}.'.format(hostsresp.text)
        log.exception(err)
        sys.exit(-1)

    PageStats.objects.filter(host=hosts).delete()   #assumption is that each process that runs this will "own" a set of hosts
                                                    #so clear current stats for these hosts when the process starts up  (for POC simplicity)
    update_task = task.LoopingCall(run_stats_updater, update_threshold = args.update_threshold, hosts=hosts)
    update_task.start(args.interval)

    reactor.run()