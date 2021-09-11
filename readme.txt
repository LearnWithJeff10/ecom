Credit card for testing:
  Visa: 4111 1111 1111 1111, CVV: 123, Expiration date: any MM/YY (12/28)

Celery is required for email and payment processing.
GTK is required for Celery (in Windows, not often mentioned). 
  Install from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
RabbitMQ is required for Celery. Can be run via Docker. Version 4.4.2 works, version 5.1.2 does not
To run RabbitMQ on docker, ensure Docker desktop is running. Then do NOT run it 
  via Docker Desktop. Instead, run:
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
To run RabbitMQ directly, install the application from www.rabbitmq.com, then run:
  rabbitmq-server

To run Celery, install it using: pip install celery==4.4.2. 
After starting RabbitMQ, run Celery using:
  celery -A myshop worker -l info

To check RabbitMQ message queue, browse to http://localhost:15672 with login/pw: guest/guest

Optionally, to monitor Celery install and run Flower.
  install:  pip install flower==0.9.3
  run:      celery -A myshop flower
  view:     http://localhost:5555/dashboard