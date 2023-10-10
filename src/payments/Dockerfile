FROM python:3.9

USER root
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /usr/src/app/orders

COPY . .

CMD [ "python3", "-u", "app.py"]
