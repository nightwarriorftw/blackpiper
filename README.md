[![Open Issues](https://img.shields.io/github/issues/nightwarriorftw/scale?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/scale/issues) [![Forks](https://img.shields.io/github/forks/nightwarriorftw/scale?style=for-the-badge&logo=github)](https://github.com/nightwarriorftw/scale/network/members) [![Stars](https://img.shields.io/github/stars/nightwarriorftw/scale?style=for-the-badge&logo=reverbnation)](https://github.com/nightwarriorftw/scale/stargazers) ![Maintained](https://img.shields.io/maintenance/yes/2021?style=for-the-badge&logo=github) ![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet?style=for-the-badge&logo=python)![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red?style=for-the-badge&logo=open-source-initiative) ![Built with Love](https://img.shields.io/badge/Built%20With-%E2%99%A5-critical?style=for-the-badge&logo=ko-fi) [![Follow Me](https://img.shields.io/twitter/follow/nightwarriorftw?color=blue&label=Follow%20%40nightwarriorftw&logo=twitter&style=for-the-badge)](https://twitter.com/intent/follow?screen_name=nightwarriorftw) [![Telegram](https://img.shields.io/badge/Telegram-Chat-informational?style=for-the-badge&logo=telegram)](https://telegram.me/nightwarriorftw)

# Blackpiper

## :ledger: Index

- [About](#beginner-about)
- [Development](#wrench-development)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Development Environment](#nut_and_bolt-development-environment)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license)

## :beginner: About

A simple app that use `Django` and `Redis` together to queueing jobs and processing them in the background.
This project uses `django-rq` which is a simple app that allows you to confiure your queues in django. `django-rq` internally uses [RQ](https://python-rq.org/).

In layman language `RQ` is an alternative of [celery](https://docs.celeryproject.org/en/stable/).
There are many ways to run async tasks in python. Most of the companies uses `celery`, since it's pretty famous also. But, here we are, now looking at an alternative of celery which is pretty easy to setup as well `RQ`.

#### Difference between RQ and Celery

Let's go through a couple of difference between `celery` and `RQ` :

- `RQ`is known for it's simplicity whereas `Celery` is known for it robustness.

- `RQ` uses `redis` as a message broker, whereas `Celery` suports both `redis` and `rabbitMQ`. `Celery` has clearly won here.

There are other differences as well, why don't you explore those on your own :)

IMHO, `celery` is awesome ;)

## :wrench: Development

### :notebook: Pre-Requisites

Knowledge of Django and zeal to learn :)

### :nut_and_bolt: Development Environment

#### 1. Make a virtual environment and activate

```BASH
python3 -m venv .venv
source ./.venv/bin/activate
```

#### 2. Clone the repo and install requirements

```BASH
git clone https://github.com/nightwarriorftw/blackpiper.git
pip install -r requirements.txt
```

#### 3. Setup Redis

`RQ` uses `redis` as a meesage broker. So, it's important to have redis installed on your system.

In case you don't have `redis` installed on your system. You can follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04) to install `redis` on your system.

#### 4. Setup Environment variables

- Create a `.env` file in the root folder of the project.

- Add the following variables in your `.env` file :

    ```BASH
    SECRET_KEY="<your django secret key>"
    DEBUG=TRUE
    RQ_QUEUE_HOST="localhost"
    RQ_QUEUE_PORT=6379
    RQ_QUEUE_DB=0
    RQ_QUEUE_DEFAULT_TIMEOUT=360
    RQ_QUEUE_PASSWORD="<your redis password>"

    ```

#### 5. Redis Configuration

Add the following in your project's `settings.py`

```BASH
# RQ Configurations
RQ_QUEUES = {
    "default": 
        {
            "HOST": env("RQ_QUEUE_HOST"), 
            "PORT": env("RQ_QUEUE_PORT"), 
            "DB": env("RQ_QUEUE_DB"), 
            "DEFAULT_TIMEOUT": env("RQ_QUEUE_DEFAULT_TIMEOUT"),
            "PASSWORD": env("RQ_QUEUE_PASSWORD")
        },
}

# RQ Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "root": {"handlers": ["console"], "level": "DEBUG",},
}
```

You can change your `logging` configuration depending upon your usecase. Like, there are hell lot of options you can find [here](https://github.com/rq/django-rq#configuring-logging).

#### 6. Makemigrations, migrate and run the server

```BASH
python manage.py makemigrations
python manage.py migrate
```

#### 6. Run server

```BASH
python manage.py runserver
```

#### 7. Start RQ worker

Open another new terminal and run the following command respectivley in both of them

```BASH
python manage.py rqworker default
```

The above command starts with rq default worker. There are lot of ways you can configure this. Change your `RQ` configuration depending upon your usecase. Refer, `django-rq` docs for this :)

#### 8. Test the real

- Open the shell

    ```BASH
    python manage.py shell
    ```

- Run `hello` method to test if everything is working on not

    ```BASH
    from piper.tasks import hello
    
    hello.delay()
    ```

You will find the call will return a reference of async method. You can check your terminal/console to validate if your setup is complete.

Do read the `django-rq` and `RQ` docs. It's pretty awesome :)

## :star2: Credit/Acknowledgment

[Aman Verma](https://nightwarriorftw.netlify.app)

- Github: [nightwarriorftw](https://github.com/nightwarriorftw)

- Linkedin: [developer-aman-verma](https://linkedin.com/in/developer-aman-verma)

- Twitter: [nightwarriorftw](https://twitter.com/nightwarriorftw)

Credits goes to me

## :lock: License

[LICENSE](/LICENSE)
