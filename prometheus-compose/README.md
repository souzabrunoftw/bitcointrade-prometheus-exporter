# prometheus-compose

This docker-compose file initializes a Prometheus and Grafana stack, including the bitcointrade exporter. It uses localhost ports 3000 and 9090.

To use:

- Start the docker-compose stack:

```
docker-compose up
```

- Go to <http://localhost:3000>.  Log in as `admin/admin`.
- To import the dashboard, click the "Home" button at the top, then on the right, click "Import Dashboard".
- Enter `3890` in the "Grafana.com Dashboard" field.
- Select the "prometheus" data source.
- Modify the other settings as preferred. Click "Import".
- The new dashboard should be selectable and found at <http://localhost:3000/dashboard/db/coinmarketcap-single>.
- The Prometheus interface can be accessed at <http://localhost:9090>
