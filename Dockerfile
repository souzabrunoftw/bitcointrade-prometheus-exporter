FROM python:3.6-alpine
RUN pip install prometheus_client requests
RUN mkdir -p /opt/bitcointrade-exporter
COPY bitcointrade.py /opt/bitcointrade-exporter/
WORKDIR /opt/bitcointrade-exporter

ENTRYPOINT ["python3", "bitcointrade.py"]
