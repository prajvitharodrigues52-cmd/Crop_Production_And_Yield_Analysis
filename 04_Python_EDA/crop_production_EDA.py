import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Find the project folder
project_folder = Path("C:\\Crop Production & Yield Analysis\\Data cleaning and prepration\\crop_production.csv").resolve().parent.parent

# Find the CSV dataset
csv_files = list((project_folder / "Dataset").glob("*.csv"))

if not csv_files:
    print("Error: No CSV file found in the Dataset folder.")
else:
    df = pd.read_csv(csv_files[0])

    print("Dataset loaded successfully!")
    print("Total rows:", df.shape[0])
    print("Total columns:", df.shape[1])

    print("\nFirst 5 rows:")
    print(df.head())


    # Top 10 States by Crop Production

state_production = (
    df.groupby("State_Name")["Production"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

state_production.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 States by Crop Production")
plt.xlabel("State")
plt.ylabel("Total Production")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(project_folder / "Python_EDA" / "Charts" / "top_10_states_production.png", dpi=300, bbox_inches="tight")
plt.show()

# Top 10 Crops by Production

crop_production = (
    df.groupby("Crop")["Production"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

crop_production.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 Crops by Production")
plt.xlabel("Crop")
plt.ylabel("Total Production")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "top_10_crops_production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Crop Production by Season

season_production = (
    df.groupby("Season")["Production"]
    .sum()
    .sort_values(ascending=False)
)

season_production.plot(kind="pie", autopct="%1.1f%%", figsize=(8, 8))

plt.title("Crop Production by Season")
plt.ylabel("")

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "production_by_season.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Yearly Crop Production Trend

yearly_production = (
    df.groupby("Crop_Year")["Production"]
    .sum()
    .sort_index()
)

yearly_production.plot(kind="line", figsize=(12, 6), marker="o")

plt.title("Yearly Crop Production Trend")
plt.xlabel("Year")
plt.ylabel("Total Production")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "yearly_production_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Chart 5: Top 10 Districts by Production

top_districts = (
    df.groupby("District_Name")["Production"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_districts.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 Districts by Crop Production")
plt.xlabel("District")
plt.ylabel("Total Production")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "top_10_districts.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Chart 6: Cultivated Area by Top 10 States

state_area = (
    df.groupby("State_Name")["Area"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

state_area.plot(kind="bar", figsize=(12, 6))

plt.title("Top 10 States by Cultivated Area")
plt.xlabel("State")
plt.ylabel("Total Cultivated Area")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "top_10_states_area.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Chart 7: Number of Different Crop Types by Season

crop_count = df.groupby("Season")["Crop"].nunique()

crop_count.plot(kind="bar", figsize=(10, 6))

plt.title("Number of Crop Types by Season")
plt.xlabel("Season")
plt.ylabel("Number of Different Crops")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "crop_types_by_season.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Chart 8: Production by State and Season

state_season = df.pivot_table(
    index="State_Name",
    columns="Season",
    values="Production",
    aggfunc="sum",
    fill_value=0
)

state_season.plot(kind="bar", stacked=True, figsize=(14, 7))

plt.title("Crop Production by State and Season")
plt.xlabel("State")
plt.ylabel("Total Production")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig(
    project_folder / "Python_EDA" / "Charts" / "state_season_production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Python EDA Summary Report

report_path = (
    project_folder
    / "Python_EDA"
    / "python_eda_summary.txt"
)

with open(report_path, "w", encoding="utf-8") as file:
    file.write("CROP PRODUCTION & YIELD ANALYSIS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Records: {df.shape[0]}\n")
    file.write(f"Total Columns: {df.shape[1]}\n\n")

    file.write("Column Names:\n")
    file.write(", ".join(df.columns) + "\n\n")

    file.write("Missing Values:\n")
    file.write(df.isnull().sum().to_string())
    file.write("\n\n")

    file.write(f"Duplicate Rows: {df.duplicated().sum()}\n\n")

    file.write("Data Types:\n")
    file.write(df.dtypes.to_string())
    file.write("\n")

print("Python EDA summary saved successfully!")
print("Location:", report_path)