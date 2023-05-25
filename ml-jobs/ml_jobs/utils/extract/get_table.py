"""
fill me in
"""

from pyspark.sql import SparkSession


def get_table(table_name):
    """
    fill me in
    """

    SparkSession.getActiveSession().table(table_name)
