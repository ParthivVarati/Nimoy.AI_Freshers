#! D:\Nimoy\preprocessing\.venv\Scripts\python.exe
import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_data(filepath):
    """Load Titanic dataset with error handling."""
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded dataset: {filepath}")
        return df
    except FileNotFoundError:
        print(f" Error: File not found -> {filepath}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: The file is empty.")
        sys.exit(1)
    except Exception as e:
        print(f" Unexpected error: {e}")
        sys.exit(1)

def clean_data(df):
    """Handle missing values safely."""
    try:
        if "Age" in df.columns:
            df["Age"] = df["Age"].fillna(df["Age"].median())
        if "Fare" in df.columns:
            df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
        if "Embarked" in df.columns:
            df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
        if "Cabin" in df.columns:
            df["Cabin"] = df["Cabin"].fillna("Unknown")
        return df
    except Exception as e:
        print(f" Error while cleaning data: {e}")
        sys.exit(1)

def analyze_data(df):
    """Perform Titanic dataset analysis with error checks."""
    try:
        print("\n--- Dataset Info ---")
        print("Shape:", df.shape)
        print("\nPreview:\n", df.head())

        if df.empty:
            print(" Error: Dataset is empty.")
            return

        # Mean Fare
        if "Fare" in df.columns:
            mean_fare = df["Fare"].mean()
            print("\nMean Fare:", mean_fare)

        # Cabin with most people
        if "Cabin" in df.columns:
            cabin_counts = df["Cabin"].value_counts()
            print("\nCabin with most people:\n", cabin_counts.head(1))

        # Age group distribution
        if "Age" in df.columns:
            age_bins = pd.cut(
                df["Age"],
                bins=[0,10,20,30,40,50,60,70,80],
                labels=["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80"]
            )
            age_group_counts = age_bins.value_counts().sort_index()
            print("\nAge group distribution:\n", age_group_counts)

        # Male vs Female count
        if "Sex" in df.columns:
            sex_counts = df["Sex"].value_counts()
            print("\nMales vs Females:\n", sex_counts)

        # Survival counts
        if "Survived" in df.columns:
            survived_counts = df["Survived"].value_counts()
            print("\nSurvived (0=No, 1=Yes):\n", survived_counts)

            # Survival rate by sex
            if "Sex" in df.columns:
                survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100
                print("\nSurvival rate by sex (%):\n", survival_by_sex)

    except Exception as e:
        print(f" Error during analysis: {e}")
        sys.exit(1)

def visualize_data(df):
    """Generate plots with error handling."""
    try:
        if "Age" in df.columns:
            plt.figure(figsize=(8,6))
            plt.hist(df["Age"], bins=20, color="skyblue", edgecolor="black")
            plt.title("Age Distribution of Passengers")
            plt.xlabel("Age")
            plt.ylabel("Count")
            plt.show()

        if "Sex" in df.columns:
            df["Sex"].value_counts().plot(kind="bar", color=["blue","pink"], figsize=(6,4))
            plt.title("Number of Males vs Females")
            plt.ylabel("Count")
            plt.show()

        if "Survived" in df.columns:
            df["Survived"].value_counts().plot(kind="bar", color=["red","green"], figsize=(6,4))
            plt.title("Survival Count (0 = No, 1 = Yes)")
            plt.ylabel("Count")
            plt.show()

        if "Sex" in df.columns and "Survived" in df.columns:
            survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100
            survival_by_sex.plot(kind="bar", color=["blue","pink"], figsize=(6,4))
            plt.title("Survival Rate by Sex (%)")
            plt.ylabel("Survival Rate %")
            plt.show()

        if "Cabin" in df.columns:
            df["Cabin"].value_counts().head(10).plot(kind="bar", figsize=(10,6), color="purple")
            plt.title("Top 10 Cabins with Most Passengers")
            plt.ylabel("Count")
            plt.show()

        if "Age" in df.columns:
            age_bins = pd.cut(
                df["Age"],
                bins=[0,10,20,30,40,50,60,70,80],
                labels=["0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80"]
            )
            age_bins.value_counts().sort_index().plot(kind="bar", figsize=(8,6), color="orange")
            plt.title("Passenger Distribution by Age Group")
            plt.ylabel("Count")
            plt.show()

        if "Fare" in df.columns and "Pclass" in df.columns:
            plt.figure(figsize=(8,6))
            df.boxplot(column="Fare", by="Pclass")
            plt.title("Fare Distribution by Class")
            plt.suptitle("")  # remove extra title
            plt.ylabel("Fare")
            plt.show()

    except Exception as e:
        print(f" Error while plotting: {e}")

# --- MAIN ---
if __name__ == "__main__":
    filepath = "train.csv"  # change path if needed
    df = load_data(filepath)
    df = clean_data(df)
    analyze_data(df)
    visualize_data(df)
