from __future__ import unicode_literals
from __future__ import print_function
from logging import StreamHandler, Formatter
from time import sleep
from datetime import timedelta
from vaam.scraper import get_available_banks
from vaam.twitter import send_tweet
import logging

logger = logging.getLogger(__name__)
sleep_interval = timedelta(minutes=30)


def config_logger():
    vaam_logger = logging.getLogger('vaam')
    vaam_logger.setLevel('DEBUG')

    handler = StreamHandler()
    handler.setFormatter(Formatter('[%(asctime)-15s %(name)s] %(message)s'))

    vaam_logger.addHandler(handler)


def notify():
    logger.info('Notifying')
    try:
        banks = get_available_banks()

        if len(banks):
            text = 'Voila! ' + ' '.join(banks)
        else:
            text = 'Nothing :('
    except Exception as exc:
        logger.exception('Exception in scrapping', exc_info=exc)
        text = 'Error!'

    try:
        send_tweet(text)
    except Exception as exc:
        logger.exception('Exception in twitting', exc_info=exc)


def run_periodically():
    while True:
        notify()
        logger.debug('sleeping for %d', sleep_interval.seconds)
        sleep(sleep_interval.seconds)
