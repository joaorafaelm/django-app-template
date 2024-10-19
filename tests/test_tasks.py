from app.tasks import run_healthchecks

def test_run_healthchecks(app):
    run_healthchecks.defer(1)
