# HACK THE FEED HACKATHON

## Title and Introduction

This is the comprehensive report of the data analysis of all four datasets in the `Hack the feed` competition.

This report details the scope and objective of the analysis, as well as insights and recommendations extracted from the work. For each dataset, we performed the same type of analysis and answered key questions relating to the:
- Impressions
- Reach
- Click-Through Rate

of the individual datasets. All the datasets were sourced from the competition's webpage [here](https://portfolio.diceytech.co.uk/project-opportunity/1692893137471x831086163701530600). The `.csv` files were downloaded and then renamed to enable ease of access from the directories they were stored in.

## Data pre-processing

Each of the datasets were examined and it was observed that all of them were structured in the same format with the same number of columns and the same column names.

Following from that observation, each dataset was opened using the `pandas` library with a line to format the `Date` column into a `datetime` format. Then a [python function](../src/clean_data.py) was written to clean up and format each dataset for easier analysis. The python function does the following:
- Splits the `Date` column into a `Date` and `Time` column
- Drops some selected columns like "Post Type", "Network", "Post ID", "Profile", as they are unnecesary for the analysis
- Drops all columns that has no values in them (columns with `NaN` values)
- Creates a new column called `Time Period` that groups each post time into "morning", "afternoon" and "evening"
- Sets the `Date` column as the index of the dataframe
- Sorts the `Date` column from the earliest date as the first row and the latest date as the last row
- Converts all columns with numbers to decimal numbers (floating point numbers) for easy computation
## Dataset 1 - Facebook

We explain in plain language what the individual notebooks are doing and then attach the plot images here as well.

### 2. Instagram

The Instagram dataset

### LinkedIn

This ....

### Twitter

This ....

## Recommendations

We recommend...

## Summary

Here we summarise....