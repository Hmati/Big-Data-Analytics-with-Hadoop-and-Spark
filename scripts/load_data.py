from pyspark.sql import SparkSession


def create_spark_session():
    """
    Create a Spark Session.
    """
    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("Kenya Agriculture Analytics")
        .getOrCreate()
    )
    return spark


def load_dataset(spark, file_path):
    """
    Load the CSV dataset into a Spark DataFrame.
    """
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(file_path)
    )
    return df