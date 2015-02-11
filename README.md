Requirements:
- django
- twisted (apt-get install python-twisted)

To run:
- python manage.py migrate    (creates Sqllite database with schema)
- python -m increasing.stats_updater   (stats updater process needs to be running in a separate process)
- python manage.py runserver 0.0.0.0:8000  (or any other port)

To access the endpoint:
- http://{host_ip_address}:8000/increasing/increasingpages/?host=gizmodo.com


Implementation notes:
- Whether concurrent views are increasing is being measured by sampling some number of data points, computing the average, and comparing it to the average over the next window of data samples of the same size.  The averaging over some timewindow is done to avoid unstable "increasing" signal caused by minor blips in viewer counts.
- By default, stats updater process averages over 5 data points, with a sampling interval of 5 seconds between data point collection.  These numbers are (optionally) configurable via command line params:
  -  python -m increasing.stats_updater --interval 10 --update_threshold 6
- The url from which to read list of available hosts is also configurable via --hosts_url param

