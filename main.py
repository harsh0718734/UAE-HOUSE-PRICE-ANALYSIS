import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATASET LOAD
df=pd.read_csv("UAE HOUSE PRICE PREDICTION.csv")
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.columns)


# CLEANING COLUMNS
df.columns=df.columns.str.strip().str.upper().str.replace("_"," ")
print(df.columns)

# DROPPING DUPLCIATES
df=df.drop_duplicates()
print(df.shape)

# NUMERIC COLUMNS

df["AREA"]=df["AREA"].astype(str).str.replace(",","").astype(float)
print(df["AREA"])

df["PRICE"]=df["PRICE"].astype(float)
print(df["PRICE"])

df.info()

# QUESTION NO.1 WHICH IS THE CHEAPEST AND MOST EXPENSIVE PROPERTY?

cheapest_building=df.groupby("NAME")["PRICE"].min().idxmin()
print(f"{cheapest_building} IS CHEAPEST BUILDING")

expensive_building=df.groupby("NAME")["PRICE"].max().idxmax()
print(f"{expensive_building} IS MOST EXPENSIVE BUILDING")


# QUESTION NO.2 WHICH IS THE CHEAPEST AND MOST EXPENSIVE PROPERTY TYPE SPECTURM?

cheapest_house = df.groupby("B TYPE")["PRICE"].min().idxmin()
print(f"THE PROPERTY CLASSIFICATION WITH THE CHEAPEST SINGLE UNIT IS: {cheapest_house}")

expensive_house = df.groupby("B TYPE")["PRICE"].max().idxmax()
print(f"THE PROPERTY CLASSIFICATION WITH THE MOST EXPENSIVE SINGLE UNIT IS: {expensive_house}")

# QUESTION NO.3 CITY VS AREA

city_area=df.groupby("CITY")["AREA"].mean().idxmax()
print(f"{city_area} HAS THE HIGHEST AVERAGE AREA")

city_area=df.groupby("CITY")["AREA"].mean().idxmin()
print(f"{city_area} HAS THE LOWEST AVERAGE AREA")

# QUESTION NO.4 CITY VS PRICE 

city_price=df.groupby("CITY")["PRICE"].mean().idxmax()
print(f"{city_price} HAS THE HIGHEST AVERAGE PRICE")

city_price=df.groupby("CITY")["PRICE"].mean().idxmin()
print(f"{city_price} HAS THE LOWEST AVERAGE PRICE")

# QUESTION 5 HOW DOES CITY AFFFECT PRICE?

plt.style.use("bmh")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="PRICE",data=df,color="Red")
plt.xlabel("CITY")
plt.ylabel("PRICE")
plt.title("CITY VS AVERAGE PROPERTY PRICE")
plt.savefig("city_vs_price.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.6 HOW DOES PROPERTY CLASSIFICATION (B TYPE) AFFECTS LISTING PRICE

plt.style.use("ggplot")
plt.figure(figsize=(8,4))
sns.barplot(x="B TYPE",y="PRICE",hue="CITY",data=df)
plt.xlabel("B TYPE")
plt.ylabel("PRICE")
plt.title("B TYPE VS PRICE")
plt.savefig("b_type_vs_price.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.7 HOW DOES AVERAGE PROPERTY AREA VARY ACROSS CITIES AND PROPERTY TYPES?

plt.style.use("bmh")
plt.figure(figsize=(10,4))
sns.barplot(x="CITY",y="AREA",hue="B TYPE",data=df)
plt.xlabel("CITY")
plt.ylabel("AREA")
plt.title("CITY VS AREA")
plt.savefig("city_vs_area.png", dpi=300, bbox_inches='tight')
plt.show()


# QUESTION NO.8 HOW DOES BEDROOM DISTRIBUTION VARY ACROSS DIFFERENT PROPERTY TYPES

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.boxplot(x="B TYPE", y="BEDROOMS", data=df)
plt.title("B TYPE VS BEDROOMS")
plt.xlabel("B TYPE")
plt.ylabel("BEDROOMS")
plt.savefig("bedroom_distribution.png", dpi=300, bbox_inches='tight')
plt.show()


# QUESTION NO.9 HOW DOES BATHROOM DISTRIBUTION VARY ACROSS DIFFERENT PROPERTY TYPES

plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.boxplot(x="B TYPE",y="BATHROOMS",data=df)
plt.title("B TYPE VS BATHROOMS")
plt.xlabel("B TYPE")
plt.ylabel("BATHROOMS")
plt.savefig("bathroom_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.10 WHICH IS THE CHEAPEST AND MOST EXPENSIVE DISTRICT?

cheapest_district=df.groupby("DISTRICT")["PRICE"].min().idxmin()
print(f"{cheapest_district} IS THE CHEAPEST DISTRICT")

expensive_district=df.groupby("DISTRICT")["PRICE"].max().idxmax()
print(f"{expensive_district} IS THE MOST EXPENSIVE DISTRICT")

# QUESTION NO.11 HOW DOES BEDROOMS DISTRIBUTION VARY AMONG DIFFERENT CITIES

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.barplot(x="CITY",y="BEDROOMS",data=df,hue="B TYPE")
plt.xlabel("CITIES")
plt.ylabel("BEDROOMS")
plt.title("DISTRIBUTION OF BEDROOMS ACROSS DIFFERENT CITIES")
plt.savefig("bedroom_distribution.png", dpi=300, bbox_inches='tight')  
plt.show()

# QUESTION NO.12 HOW DOES BATHROOMS DISTRIBUTUON VARY ACROSS DIFFERENT CITIES

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.barplot(x="CITY",y="BATHROOMS",data=df,hue="B TYPE")
plt.xlabel("CITIES")
plt.ylabel("BATHROOMS")
plt.title("DISTRIBUTION OF BATHROOMS ACROSS DIFFERENT CITIES")
plt.savefig("bathroom_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.13 HOW DOES AVERAGE PROPERTY AREA VARY ACROSS DIFFERENT PROPERTY TYPES AND CITIES

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.barplot(x="B TYPE",y="AREA",data=df,hue="CITY")
plt.xlabel("B TYPE")
plt.ylabel("AREA")
plt.title("DISTRIBUTION OF AREA ACROSS DIFFERENT PROPERTY TYPES")
plt.savefig("area_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.14 CREATE A CORRELATION HEATMAP TO ANALYSE THE RELATIONSHIP BETWEEN PROPERTY FEATURES.

corr=df[["PRICE", "AREA", "BEDROOMS", "BATHROOMS"]].corr()

sns.heatmap(corr,annot=True,cmap="coolwarm")

plt.title("UAE Property Correlation Heatmap")

plt.savefig("correlation_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

#  QUESTION NO.15 COUNT PLOT

plt.style.use("ggplot")
plt.figure(figsize=(10,4))
sns.countplot(x="B TYPE",hue="CITY",data=df)
plt.xlabel("B TYPE")
plt.ylabel("PROPERTY COUNT")
plt.title("COUNT PLOT")
plt.savefig("count_plot.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.16 SCATTER PLOT

plt.style.use("ggplot")
plt.figure(figsize=(10,5))
sns.scatterplot(x="AREA",y="PRICE",hue="CITY",data=df)
plt.xlabel("AREA")
plt.ylabel("PRICE")
plt.title("AREA VS PRICE")
plt.savefig("scatter_plot.png", dpi=300, bbox_inches='tight')
plt.show()

# QUESTION NO.17 TOP 10 EXPENSIVE DISTRICTS

expensive_districts=df.groupby("DISTRICT")["PRICE"].mean().sort_values(ascending=False).head(10)
print(f"THE TOP 10 EXPENSIVE DISTRICTS ARE: {expensive_districts}")

# QUESTION NO.18 TOP 10 CHEAPEST DISTRICTS

cheapest_districts=df.groupby("DISTRICT")["PRICE"].mean().sort_values(ascending=True).head(10)
print(f"THE TOP CHEAPEST DISTRICTS ARE: {cheapest_districts}")

# QUESTION NO.19 TOP 3 RICHEST CITIES

richest_cities=df.groupby("CITY")["PRICE"].mean().sort_values(ascending=False).head(3)
print(f"THE TOP 3 RICHEST CITIES ARE: {richest_cities}")

# QUESTION NO.20 TOP 3 CHEAPEST CITIES

cheapest_cities=df.groupby("CITY")["PRICE"].mean().sort_values(ascending=True).head(3)
print(f"THE TOP 3 CHEAPEST CITIES ARE: {cheapest_cities}")

# QUESTION NO.21 TOP 3 RICHEST PROPERTY TYPES

richest_properties=df.groupby("B TYPE")["PRICE"].mean().sort_values(ascending=False).head(3)
print(f"THE TOP 3 RICHEST PROPERTY TYPES ARE: {richest_properties}")

# QUESTION NO.22 TOP 3 CHEAPEST PROPERTY TYPES

cheapest_properties=df.groupby("B TYPE")["PRICE"].mean().sort_values(ascending=True).head(3)
print(f"THE TOP 3 CHEAPEST PROPERTY TYPES ARE: {cheapest_properties}")

# QUESTION NO.23  BEDROOM-WISE AVERAGE PROPERTY PRICE ANALYSIS

bedroom_prices_ranges=df.groupby("BEDROOMS")["PRICE"].mean().sort_values(ascending=False)
print(f"THE AVERAGE PRICES FOR DIFFERENT BEDROOM CONFIGURATIONS ARE: {bedroom_prices_ranges}")

# QUESTION NO.24 BATHROOM-WISE AVERAGE PROPERTY PRICE ANALYSIS

bathroom_prices_ranges=df.groupby("BATHROOMS")["PRICE"].mean().sort_values(ascending=False)
print(f"THE AVERAGE PRICES FOR DIFFERENT BATHROOM CONFIGURATIONS ARE: {bathroom_prices_ranges}")

print("\nUAE HOUSE PREDICTION  ANALYSIS COMPLETED SUCCESSFULLY!")
print("THANK YOU!")