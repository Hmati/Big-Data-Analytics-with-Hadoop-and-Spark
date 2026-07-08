import re

"""
clean_data.py

This module contains functions for cleaning and validating
the Kenya Agriculture dataset.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, sum, when

#Check for duplicates

def check_duplicates(df: DataFrame) -> int:
    """
    Returns the number of duplicate rows.
    """

    total_rows = df.count()
    unique_rows = df.dropDuplicates().count()

    duplicates = total_rows - unique_rows

    return duplicates

#Remove duplicates

def remove_duplicates(df: DataFrame) -> DataFrame:
    """
    Removes duplicate rows.
    """

    return df.dropDuplicates()

#Check for missing values

def check_missing_values(df: DataFrame):
    """
    Displays missing values for each column.
    """

    missing = df.select([
        sum(
            when(col(column).isNull(), 1).otherwise(0)
        ).alias(column)

        for column in df.columns
    ])

    missing.show()
    
    #standardize column names
    import re


def standardize_column_names(df: DataFrame) -> DataFrame:
    """
    Standardizes column names by converting to lowercase,
    replacing spaces with underscores,
    and removing special characters.
    """

    for column in df.columns:

        new_name = column.lower()

        new_name = re.sub(r"[()]", "", new_name)

        new_name = new_name.replace(" ", "_")

        new_name = new_name.replace("-", "_")

        df = df.withColumnRenamed(column, new_name)

    return df

#Validate Numeric Columns

def validate_numeric_columns(df: DataFrame):
    """
    Checks for negative values
    in the Value column.
    """

    invalid = df.filter(col("value") < 0)

    print("Negative values found:", invalid.count())

    return invalid

#Data quality report 

def data_quality_report(df: DataFrame):
    """
    Displays basic data quality metrics.
    """

    print("=" * 50)

    print("Rows:", df.count())

    print("Columns:", len(df.columns))

    print("Duplicates:", check_duplicates(df))

    print("=" * 50)

    print("Missing Values")

    check_missing_values(df)
    
    
#Handling missing values
    
from pyspark.sql.functions import col
def remove_missing_values(df: DataFrame) -> DataFrame:
    """
    Removes records where the Value column is missing.

    Parameters
    ----------
    df : DataFrame
        Input Spark DataFrame.

    Returns
    -------
    DataFrame
        DataFrame containing only rows with valid Value entries.
    """

    return df.filter(col("Value").isNotNull())