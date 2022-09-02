# Databricks notebook source
# MAGIC %md
# MAGIC This is a test notebook that imports from utility files, uses parameters and a library.

# COMMAND ----------

dbutils.widgets.text("first_name", "")
dbutils.widgets.text("env", "dev")

first_name = dbutils.widgets.get("first_name")
env = dbutils.widgets.get("env").lower()

# COMMAND ----------

import logging

import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

from utils.b import print_greeting

# COMMAND ----------

logger = logging.getLogger("test_notebook")

# COMMAND ----------

tracking_url = f"databricks://runtasticdata{env}-d-vault:svc-db-machine-learning-DEV"
model_registry_url = f"databricks://runtasticdata{env}-d-vault:svc-db-machine-learning-DEV"
logger.info("Setting Model Registry URL to %s", model_registry_url)
mlflow.set_registry_uri(model_registry_url)
logger.info("Setting Tracking URL to %s", tracking_url)
mlflow.set_tracking_uri(tracking_url)

# COMMAND ----------

with mlflow.start_run(experiment_id="1105835291298026") as run:
  print_greeting(first_name)

  iris = datasets.load_iris()
  iris_train = pd.DataFrame(iris.data, columns=iris.feature_names)
  clf = RandomForestClassifier(max_depth=7, random_state=0)
  clf.fit(iris_train, iris.target)
  signature = infer_signature(iris_train, clf.predict(iris_train))
  mlflow.sklearn.log_model(clf, "model", signature=signature)
