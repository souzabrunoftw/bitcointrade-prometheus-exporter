# bitcointrade-prometheus-exporter

A prometheus exporter for <https://apidocs.bitcointrade.com.br>. Provides Prometheus metrics from the API endpoint of BitcoinTrade, such as Bitcoin, Ethereum and Litecoin last price, highest price (24h), lowest price (24h), trading volume, etc.

When running this exporter with both Prometheus and Grafana, [you can create dashboards like](https://grafana.com/dashboards/3890):

![bitcointrade-single-dashboard](https://github.com/bonovoxly/bitcointrade-exporter/raw/master/img/bitcointrade.png "bitcointrade-exporter with Prometheus and Grafana")

# Developing

- Build the image:

```
docker build -t bitcointrade-prometheus-exporter:latest .
```

- Run it while listening on localhost:9100:

```
docker run --rm -p 127.0.0.1:9101:9101 bitcointrade-prometheus-exporter:latest
```

- Run it interactively:

```
docker run --rm -it --entrypoint=/bin/bash -p 127.0.0.1:9101:9101 -v ${PWD}:/opt/bitcointrade-exporter bitcointrade-prometheus-exporter:latest
```

- Then to launch:

```
python bitcointrade.py
```

# Testing the Prometheus Grafana Stack

- In the `prometheus-compose` directory, run:

```
docker-compose up
```

- Go to <http://localhost:3000>.  Log in as `admin/admin`.
- To import the dashboard, click the "Home" button at the top, then on the right, click "Import Dashboard".
- Enter `3890` in the "Grafana.com Dashboard" field.
- Select the "prometheus" data source.
- Modify the other settings as preferred. Click "Import".
- The new dashboard should be selectable and found at <http://localhost:3000/dashboard/db/bitcointrade-single>.
- The Prometheus interface can be accessed at <http://localhost:9090>

# Thanks and Links

- BitcoinTrade API link - <https://apidocs.bitcointrade.com.br>
- Prometheus exporters - <https://prometheus.io/docs/instrumenting/writing_exporters/>
- Writing JSON exporters in Python from Robust Perception - <https://www.robustperception.io/writing-json-exporters-in-python/>
- Grafana Dashboard - <https://grafana.com/dashboards/3890>
