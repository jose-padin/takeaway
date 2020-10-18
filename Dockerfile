ARG PYTHON_VERSION=3.7

# Download python image
FROM python:${PYTHON_VERSION} as base
LABEL maintainer='Jose Padin <jose.padin@kubicum.com>'

ARG PROJECT_NAME=takeaway

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
RUN pip install --upgrade pip
RUN pip install pipenv
RUN python -m pip install Django
RUN pip install uvicorn
COPY ./project /project

# Expose a port to communicate between host and container
EXPOSE 9988
