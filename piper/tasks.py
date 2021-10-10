from django_rq import job

import logging

logger = logging.getLogger(__name__)


@job
def hello():
    print("hello")
    logger.info("\n\nHello World\n\n")
