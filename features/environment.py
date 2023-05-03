from fastapi.testclient import TestClient
from rest_api import app, db

SKIP_TAG = 'skip'


def before_scenario(context, scenario):
    if SKIP_TAG not in scenario.tags:
        context.db = db
        context.db.clear()
        context.client = TestClient(app)
        print(f"{scenario.name} started")
        return
    else:
        scenario.skip("Marked with @skip")


def after_scenario(context, scenario):
    if SKIP_TAG not in scenario.tags:
        context.client.close()
        print(f"{scenario.name} finished")
