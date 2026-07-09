from pyspark.sql import DataFrame
from pyspark.sql.functions import col, sum




def prepare_analysis_dataset(df: DataFrame) -> DataFrame:
    """
    Prepare the dataset for analysis by selecting the required
    columns and removing records with missing values.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return (
        df.select(
            "item",
            "element",
            "year",
            "unit",
            "value"
        )
        .filter(col("value").isNotNull())
    )


def filter_by_element(df: DataFrame, element: str) -> DataFrame:
    """
    Filter the dataset by a specific element.

    Parameters
    ----------
    df : DataFrame
        Cleaned Spark DataFrame.

    element : str
        Element to filter by (e.g. Production,
        Area harvested, Yield).

    Returns
    -------
    DataFrame
        Filtered DataFrame.
    """

    return df.filter(col("element") == element)


def select_analysis_columns(df: DataFrame) -> DataFrame:
    """
    Select only the columns needed for analysis.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return df.select(
        "item",
        "element",
        "year",
        "unit",
        "value"
    )


def aggregate_yearly_production(df: DataFrame) -> DataFrame:
    """
    Calculate total production for each year.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return (
        df.groupBy("year")
          .agg(sum("value").alias("total_production"))
          .orderBy("year")
    )


def aggregate_crop_production(df: DataFrame) -> DataFrame:
    """
    Calculate total production for each crop.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return (
        df.groupBy("item")
          .agg(sum("value").alias("total_production"))
          .orderBy(col("total_production").desc())
    )


def aggregate_crop_year(df: DataFrame) -> DataFrame:
    """
    Calculate production by crop and year.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return (
        df.groupBy("item", "year")
          .agg(sum("value").alias("total_production"))
          .orderBy("item", "year")
    )


def sort_by_year(df: DataFrame) -> DataFrame:
    """
    Sort the dataset by year.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
    """

    return df.orderBy("year")