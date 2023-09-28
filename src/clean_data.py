import pandas as pd
import numpy as np

def clean_df(df, columns_to_drop=None):
    """
    Cleans and preprocesses a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to be cleaned.
        columns_to_drop (list of str, optional): A list of column names to drop from the DataFrame. Default is None.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Data Validation
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")

    # Convert datetime column to date and time components
    df["Time"] = df["Date"].dt.time
    df["Date"] = df["Date"].dt.date

    # Columns to drop
    if columns_to_drop is None:
        columns_to_drop = ["Post Type", "Network", "Post ID", "Profile"]

    # Ensure specified columns to drop exist in DataFrame
    non_existent_cols = [col for col in columns_to_drop if col not in df.columns]
    if non_existent_cols:
        raise ValueError(
            f"Columns to drop do not exist in the DataFrame: {', '.join(non_existent_cols)}"
        )

    # Drop specified columns
    df = df.drop(columns=columns_to_drop)

    # Drop columns with all NaN values
    for col in df.columns:
        if df[col].value_counts().sum() == 0:
            df = df.drop(col, axis=1)


    # Create 'Time Period' column based on time
    time_periods = ["morning", "afternoon", "evening"]
    conditions = [
        (df["Time"] >= pd.to_datetime("00:00:00").time())
        & (df["Time"] < pd.to_datetime("12:00:00").time()),
        (df["Time"] >= pd.to_datetime("12:00:00").time())
        & (df["Time"] < pd.to_datetime("17:00:00").time()),
        (df["Time"] >= pd.to_datetime("17:00:00").time())
        & (df["Time"] <= pd.to_datetime("23:59:59").time()),
    ]
    labels = time_periods

    df["Time Period"] = np.select(conditions, labels, default="unknown")

    # Set 'Date' as index and sort
    df = df.set_index("Date")
    df = df.sort_values("Date")

    # Define a function for converting numbers to float
    def convert_numbers_to_float(s):
        if isinstance(s, str):
            try:
                return float(s.replace(",", ""))
            except ValueError:
                pass
        return s

    # Apply the 'convert_numbers_to_float' function to all DataFrame values
    df = df.applymap(convert_numbers_to_float)

    return df
