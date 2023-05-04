# -*- coding: UTF-8 -*-
# FILE: features/environment.py

from fastapi.testclient import TestClient
from rest_api import app, db

SKIP_TAG = 'skip'


def before_all(context):
    # -- SETUP ACTIVE-TAG MATCHER (with userdata):
    # USE: behave -D browser=safari ...
    setup_python_path()
    setup_context_with_global_params_test(context)


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if SKIP_TAG in scenario.tags:
        scenario.skip(reason="Marked with @skip")
    else:
        context.db = db
        context.db.clear()
        context.client = TestClient(app)
        return


def after_scenario(context, scenario):
    if SKIP_TAG not in scenario.tags:
        context.client.close()


# -----------------------------------------------------------------------------
# SPECIFIC FUNCTIONALITY:
# -----------------------------------------------------------------------------
def setup_context_with_global_params_test(context):
    context.global_name = "env:Alice"
    context.global_age = 12


def setup_python_path():
    # -- NEEDED-FOR: formatter.user_defined.feature
    import os
    PYTHONPATH = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = "." + os.pathsep + PYTHONPATH
