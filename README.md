Requirements:
- django
- twisted (apt-get install python-twisted)

To run:
- python manage.py migrate    (creates Sqllite database with schema)
- python -m increasing.stats_updater   (stats updater process needs to be running in a separate process)
- python manage.py runserver 0.0.0.0:8000  (or any other port)

To access the endpoint:
- http://{host_ip_address}:8000/increasing/increasingpages/?host=gizmodo.com
