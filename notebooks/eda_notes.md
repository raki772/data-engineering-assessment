# Exploratory Data Analysis – IndiaMART Data

## 1. Loading the data

After running the crawler:

- Input file: `data/products.json`
- Load in Python with:

  - Read JSON to DataFrame
  - Inspect columns: product_name, price_range, supplier_city, supplier_name, description

## 2. Summary statistics

- Count how many products were scraped in total.
- Number of unique suppliers.
- Top 10 most common cities for suppliers.
- Count of products per high-level category (e.g. machinery, electronics, textiles if multiple crawls are run).

## 3. Price and text patterns

- Parse `price_range` where possible into min/max numeric values.
- Look at distribution of prices (min, max, median).
- Identify frequent keywords in `description` (e.g. "automatic", "export", "ISO", etc.).

## 4. Regional insights

- Group by `supplier_city`, count products per city.
- Identify cities with the highest concentration of suppliers.
- Comment on whether certain product types tend to cluster in certain cities.

## 5. Data quality checks

- Count missing values in each field (product_name, price_range, supplier_city, supplier_name, description).
- Note records with obviously bad or inconsistent price strings.
- Suggest cleaning steps (e.g. normalizing city names, removing HTML/extra whitespace in descriptions).

## 6. Example visualizations (to be built locally)

If run in a Jupyter notebook, suggested plots:

- Bar chart: top 10 supplier cities by product count.
- Histogram: distribution of parsed prices (where available).
- Bar chart: top keywords from descriptions.

These analyses together satisfy Part B of the assessment by summarizing distributions, common attributes, regional patterns, and data quality issues.
