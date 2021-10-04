release: python3 manage.py makemigrations && python3 manage.py migrate
web: daphne fig_cel.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python3 manage.py runworker channel_layer -v2
tasksworker: celery -A fig_cel.celery wroker -l info
beatworker: celery -A  fig_cel beat wroker -l info