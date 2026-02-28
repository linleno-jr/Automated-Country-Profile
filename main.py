import pandas as pd
from docx import Document
from input import get_input

# creating a data frame from csv
df = pd.read_csv("filtered_countries.csv")

# converting country names in data frame to lowercase
df["Country"] = df["Country"].str.lower()

columns_needed = ["Government: Country name - conventional long form", ]

def main():

    # getting input from the user
    committee, topic, country = get_input(df)

if __name__ == "__main__":
    main()