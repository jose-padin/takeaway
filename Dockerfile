ARG PYTHON_VERSION=3.7

# Download python image
FROM python:${PYTHON_VERSION} as base
LABEL maintainer='Jose Padin <jose.padin@kubicum.com>'

ARG PROJECT_NAME=takeaway

ENV TZ=${TZ:-Europe/Madrid} \
    PIPENV_VENV_IN_PROJECT=${PIPENV_VENV_IN_PROJECT:-1} \
    PIPENV_DOTENV_LOCATION=${PIPENV_DOTENV_LOCATION:-/project/.env} \
    WORKON_HOME=${WORKON_HOME:-/project/.venv}

# Run this commands inside container
RUN apt update && \
	apt upgrade -y && \
	apt install -y \
		apt-utils \
		build-essential \
		git \
		locales \
		postgresql-client \
		sudo \
		tree \
		vim && \
	apt purge -y --auto-remove && \
	apt clean;

# set the working directory for any instruction that follow
WORKDIR /project
COPY project/.env /project
COPY project/Pipfile /project/Pipfile

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

COPY ./project /project

# Expose a port to communicate between host and container
EXPOSE 9988

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:9988"]
# CMD ["pipenv", "run", "uvicorn", "--reload", "--bind 0.0.0.0:9000", "takeaway.wsgi:application"]