from prometheus_client import start_http_server, Metric, REGISTRY
import argparse
import json
import logging
import requests
import sys
import time

# logging setup
log = logging.getLogger('bitcointrade-exporter')
log.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


class Coin:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol.upper()


class CoinCollector:
    def __init__(self, coins):
        self.endpoint = 'https://api.bitcointrade.com.br/v1/public/{symbol}/ticker'
        self.coins = coins

    def collect(self):
        for coin in self.coins:

            # query the api
            log.info('Starting with {coin}'.format(coin=coin.name))
            r = requests.get(self.endpoint.format(symbol=coin.symbol))

            request_time = r.elapsed.total_seconds()
            log.info('Elapsed time - ' + str(request_time))

            response = json.loads(r.content.decode('UTF-8'))

            if not response['data']:
                break

            ticker = response['data']

            # setup the metric
            metric = Metric('bitcointrade_response_time', 'Total time for the bitcointrade API to respond.',
                            'summary')
            # add the response time as a metric
            metric.add_sample('bitcointrade_response_time', value=float(request_time),
                              labels={'name': 'bitcointrade.com.br', 'coin': coin.symbol})
            yield metric

            metric = Metric('bitcointrade_coin', 'bitcointrade metric values', 'gauge')

            for that in ['volume', 'trades_quantity', 'last', 'buy', 'sell']:
                btctrademetric = '_'.join(['bitcointrade_coin', that])
                log.info('Metric: ' + ' '.join([btctrademetric, coin.symbol, str(ticker[that])]))
                metric.add_sample(btctrademetric, value=float(ticker[that]), labels={'name': coin.name, 'symbol': coin.symbol})
            yield metric


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--port', nargs='?', const=9101, help='The TCP port to listen on.  Defaults to 9101.',
                            default=9101)
        args = parser.parse_args()
        log.info(args.port)

        coins = [Coin('Bitcoin', 'BTC'), Coin('Ethereum', 'ETH'), Coin('LiteCoin', 'LTC')]

        REGISTRY.register(CoinCollector(coins))
        start_http_server(int(args.port))
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        log.info("Interrupted")
        exit(0)
