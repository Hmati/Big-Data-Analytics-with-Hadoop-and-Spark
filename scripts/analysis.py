from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    sum,
    avg,
    min,
    max,
    countDistinct
)


def dataset_overview(df: DataFrame):
    """
    Display basic information about the dataset.
    """

    print("=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)
    print(f"Rows: {df.count()}")
    print(f"Columns: {len(df.columns)}")
    print(f"Columns: {df.columns}")


def summary_statistics(df: DataFrame):
    """
    Return summary statistics for numeric columns.
    """

    return df.describe(["value"])


def top_items(df: DataFrame, n=10):
    """
    Return the top N items based on total value.
    """

    return (
        df.groupBy("item")
        .agg(sum("value").alias("total_value"))
        .orderBy(col("total_value").desc())
        .limit(n)
    )


def lowest_items(df: DataFrame, n=10):
    """
    Return the lowest N items based on total value.
    """

    return (
        df.groupBy("item")
        .agg(sum("value").alias("total_value"))
        .orderBy(col("total_value"))
        .limit(n)
    )


def values_by_year(df: DataFrame):
    """
    Calculate total value for each year.
    """

    return (
        df.groupBy("year")
        .agg(sum("value").alias("total_value"))
        .orderBy("year")
    )


def highest_year(df: DataFrame):
    """
    Return the year with the highest total value.
    """

    return (
        values_by_year(df)
        .orderBy(col("total_value").desc())
        .limit(1)
    )


def lowest_year(df: DataFrame):
    """
    Return the year with the lowest total value.
    """

    return (
        values_by_year(df)
        .orderBy(col("total_value"))
        .limit(1)
    )


def average_value(df: DataFrame):
    """
    Calculate the average value.
    """

    return (
        df.select(
            avg("value").alias("average_value")
        )
    )


def unique_items(df: DataFrame):
    """
    Count unique agricultural items.
    """

    return (
        df.select(
            countDistinct("item").alias("unique_items")
        )
    )


def units(df: DataFrame):
    """
    Display all measurement units.
    """

    return (
        df.select("unit")
        .distinct()
        .orderBy("unit")
    )


def value_statistics(df: DataFrame):
    """
    Display minimum, maximum and average values.
    """

    return (
        df.select(
            min("value").alias("minimum_value"),
            max("value").alias("maximum_value"),
            avg("value").alias("average_value")
        )
    )


def item_statistics(df: DataFrame):
    """
    Display the number of unique items.
    """

    return (
        df.select(
            countDistinct("item").alias("number_of_items")
        )
    )


def year_statistics(df: DataFrame):
    """
    Display the range of years in the dataset.
    """

    return (
        df.select(
            min("year").alias("first_year"),
            max("year").alias("last_year"),
            countDistinct("year").alias("number_of_years")
        )
    )


def element_statistics(df: DataFrame):
    """
    Display the unique element(s) contained in the dataset.
    """

    return (
        df.select("element")
        .distinct()
        .orderBy("element")
    )