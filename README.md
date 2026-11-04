# UAE House Price Analysis

## About the Project

I created this project to explore the real estate market across different cities and districts in the UAE. The main goal was to understand how property prices vary based on location, property type, area, bedrooms, and bathrooms.

Using Python, I performed Exploratory Data Analysis (EDA) to identify pricing patterns, compare property categories, and understand differences across the UAE property market.

## Dataset Information

The dataset contains UAE property listings with information about:

- Property Name
- City
- District
- Property Type
- Property Price
- Area
- Bedrooms
- Bathrooms

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Data Cleaning & Preparation

Before starting the analysis, I performed the following steps:

- Loaded the dataset using Pandas.
- Checked the first and last records.
- Examined missing values and column information.
- Cleaned column names by removing extra spaces and standardizing the format.
- Removed duplicate records.
- Converted Area and Price columns into numeric formats.
- Checked the dataset structure and data types.

## Exploratory Data Analysis

I explored the dataset through 24 questions covering different aspects of the UAE real estate market.

**Property Price Analysis**
- Identified the cheapest and most expensive properties.
- Compared prices across different property types.
- Analyzed bedroom-wise and bathroom-wise average property prices.

**City & District Analysis**
- Compared average property prices across cities.
- Identified the highest and lowest average property areas.
- Analyzed the cheapest and most expensive districts.
- Identified the top 10 expensive and cheapest districts.
- Compared the top 3 expensive and cheapest cities.

**Property Features Analysis**
- Studied the relationship between property area and price.
- Compared bedroom and bathroom distributions.
- Analyzed average area across different property types and cities.
- Examined property classification and its impact on pricing.

**Additional Analysis**
- Compared property prices across different property classifications.
- Analyzed property counts by type and city.
- Identified the top 3 expensive and cheapest property types.
- Created a correlation heatmap to understand relationships between numerical features.

## Project Visualizations

The project includes visualizations created using Matplotlib and Seaborn:

## Project Visualisations & Analysis

### 1. City-wise Average Property Price

![City-wise Average Property Price](visualizations/city_vs_price.png)

### 2. Property Type vs Price

![Property Type vs Price](visualizations/b_type_vs_price.png)

### 3. City-wise Average Property Area

![City-wise Average Property Area](visualizations/city_vs_area.png)

### 4. Bedroom Distribution Across Cities

![Bedroom Distribution](visualizations/bedroom_distribution.png)

### 5. Bathroom Distribution Across Cities

![Bathroom Distribution](visualizations/bathroom_distribution.png)

### 6. Property Area Distribution

![Property Area Distribution](visualizations/area_distribution.png)

### 7. Correlation Heatmap

![Correlation Heatmap](visualizations/correlation_heatmap.png)

### 8. Property Count by Type and City

![Property Count](visualizations/count_plot.png)

### 9. Area vs Price Scatter Plot

![Area vs Price](visualizations/scatter_plot.png)

## Key Learnings

Through this project, I improved my understanding of:

- Data cleaning and preprocessing using Pandas.
- GroupBy operations and statistical analysis.
- Mean, median, minimum, and maximum calculations.
- Comparing property prices across cities and districts.
- Working with different property features.
- Creating meaningful visualizations using Matplotlib and Seaborn.
- Performing Exploratory Data Analysis on real-world datasets.

## Conclusion

This project helped me explore different factors affecting property prices across the UAE. By comparing cities, districts, property types, and property features, I gained a better understanding of real estate market trends and strengthened my practical data analysis skills using Python.
