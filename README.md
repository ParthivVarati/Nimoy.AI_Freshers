Titanic Data Analysis 🛳️

This project analyzes the Titanic dataset (titanic.csv) using Python, Pandas, and Matplotlib.
It performs data cleaning, statistical analysis, and visualization of passenger survival, demographics, and fares.
Error handling is included to make the script more robust.

📂 Project Structure
preprocessing/
│── main.py         # Main analysis script
│── titanic.csv     # Titanic dataset (input file)
│── README.md       # Project documentation

⚙️ Requirements

Install the required Python libraries:

pip install pandas matplotlib

▶️ How to Run

Place the dataset file titanic.csv in the same folder as main.py.
(It should have columns like: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.)

Run the script:

python main.py


The program will:

Clean missing values

Print analysis results

Show visualizations in pop-up windows

📊 Analysis Performed

Data Cleaning

Fill missing Age with median

Fill missing Fare with mean

Fill missing Embarked with mode

Fill missing Cabin with "Unknown"

Statistics

Mean fare

Most frequent cabin

Age group distribution

Male vs Female counts

Survival counts

Survival rate by gender

Visualizations

Age distribution (histogram)

Male vs Female (bar chart)

Survival counts (bar chart)

Survival rate by gender (bar chart)

Top 10 cabins with most passengers (bar chart)

Age group distribution (bar chart)

Fare distribution by passenger class (boxplot)

🛡️ Error Handling

The script safely handles:

Missing dataset file

Empty dataset

Missing expected columns

Unexpected runtime errors

📌 Example Output

Mean Fare: 32.20

Cabin with most passengers: Unknown (since many cabin values are missing)

Most passengers age group: 21–30 years

Survival rate by gender: Females ~74%, Males ~19%

Plots will open automatically showing the distributions.
