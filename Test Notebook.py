# Databricks notebook source
# MAGIC %md
# MAGIC This is a test notebook that imports from utility files, uses parameters and a library.

# COMMAND ----------

dbutils.widgets.text("first_name", "")
first_name = dbutils.widgets.get("first_name")

# COMMAND ----------

from utils.b import print_greeting

# COMMAND ----------

print_greeting(first_name)
