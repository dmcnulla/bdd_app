from fastapi.testclient import TestClient
from rest_api import app, db


def before_scenario(context, scenario):
    context.db = db
    context.db.clear()
    context.client = TestClient(app)
    print(f"{scenario.name} started")


def after_scenario(context, scenario):
    context.client.close()
    print(f"{scenario.name} finished")
