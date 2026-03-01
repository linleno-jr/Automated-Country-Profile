import pandas as pd
from country_io import output_country_info, get_input
from data.info import columns_needed

# creating a data frame from csv
df = pd.read_csv("data/filtered_countries.csv")

# converting country names in data frame to lowercase
df["Country"] = df["Country"].str.lower()

def main():

    # getting input from the user
    committee, topic, country = get_input(df)

    output_country_info(df, country, columns_needed)

if __name__ == "__main__":
    main()