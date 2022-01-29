broker_url = 'amqp://guest:guest@rabbitmq:5672//'
result_backend = 'db+sqlite:///results.db'	
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
celery_imports = ("tasks",)