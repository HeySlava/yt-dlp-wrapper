FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/list/*

ENV YT_DLP_VERSION=2023.7.6

ENV PATH=/venv/bin:$PATH
RUN :\
    && python -m venv /venv \
    && pip install --no-cache-dir yt-dlp==${YT_DLP_VERSION} \
    && :

ENTRYPOINT ["yt-dlp"]
