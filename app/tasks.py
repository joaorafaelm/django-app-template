import logging

from procrastinate.contrib.django import app

logger = logging.getLogger(__name__)


@app.periodic(cron="*/1 * * * *")
@app.task
def run_healthchecks(timestamp: int):
    logger.info("Running healthchecks")


@app.task
def task_1(obj_pk):
    # obj = MyModel.objects.get(pj=obj_pk)

    # calling the task
    # from myapp.tasks import mytask

    # mytask.defer(obj_pk=obj.pk)
    pass
