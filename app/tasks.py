import logging

from procrastinate.contrib.django import app

logger = logging.getLogger(__name__)


@app.periodic(cron="*/1 * * * *")
@app.task
def run_healthchecks(timestamp: int):
    logger.info("Running healthchecks")
