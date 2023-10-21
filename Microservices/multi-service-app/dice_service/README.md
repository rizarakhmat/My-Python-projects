# ASE - multi service application

Part of ASE Advanced Software course

Milti service application running on Docker containers, communication throught API gateway.
testing with Locust - load testing tool

### Run the application

 ```bash

  $ docker-compose build
  $ docker-compose up -d
  ```

 ```bash

  $ locust -f locustfile.py
  ```

no problem until 300-400 users (around 20 RPS)

then scale up

 ```bash

  $ docker-compose up -d --scale string-service=6 --no-recreate
  ```
then it will scale better (around 40 RPS)
