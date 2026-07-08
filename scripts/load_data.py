"""
load_data.py

This module contains functions for:
1. Creating a Spark session
2. Loading the Kenya Agriculture dataset
3. Performing initial data inspection
"""

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, sum, when


def create_spark_session() -> SparkSession:
    """
    Creates and returns a Spark Session.

    Returns
    -------
    SparkSession
        Active Spark session.
    """

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("Kenya Agriculture Analytics")
        .getOrCreate()
    )

    # Reduce unnecessary Spark log messages
    spark.sparkContext.setLogLevel("ERROR")

    return spark


def load_dataset(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Loads a CSV dataset into a Spark DataFrame.

    Parameters
    ----------
    spark : SparkSession
        Active Spark session.

    file_path : str
        Path to the CSV file.

    Returns
    -------
    DataFrame
        Spark DataFrame containing the dataset.
    """

    try:
        df = (
            spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(file_path)
        )

        print("Dataset loaded successfully.")

        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        raise


def preview_data(df: DataFrame, rows: int = 5) -> None:
    """
    Displays the first rows of the dataset.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.

    rows : int
        Number of rows to display.
    """

    df.show(rows)


def dataset_shape(df: DataFrame) -> tuple:
    """
    Returns the dimensions of the dataset.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.

    Returns
    -------
    tuple
        Number of rows and columns.
    """

    rows = df.count()
    columns = len(df.columns)

    return rows, columns


def dataset_schema(df: DataFrame) -> None:
    """
    Displays the schema of the dataset.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.
    """

    df.printSchema()


def list_columns(df: DataFrame) -> list:
    """
    Returns all column names.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.

    Returns
    -------
    list
        List of column names.
    """

    return df.columns


def dataset_summary(df: DataFrame) -> None:
    """
    Displays summary statistics for the dataset.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.
    """

    df.describe().show()


def check_missing_values(df: DataFrame) -> None:
    """
    Displays the number of missing values in each column.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.
    """

    missing_values = df.select([
        sum(when(col(column).isNull(), 1).otherwise(0)).alias(column)
        for column in df.columns
    ])

    missing_values.show()


def row_count(df: DataFrame) -> int:
    """
    Returns the total number of rows.

    Parameters
    ----------
    df : DataFrame
        Spark DataFrame.

    Returns
    -------
    int
        Number of rows.
    """

    return df.count()