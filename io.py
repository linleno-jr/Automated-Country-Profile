import pandas as pd
from data.info import column_to_name

# outputs info on a given country
def output_country_info(df, country: str, columns_needed: list):
    print(f"\nHere is the information on the country {country.title()}!")

    for column in columns_needed:
        info_category = column_to_name[column]
        info = df.loc[df["Country"] == country, column].iloc[0]

        # making sure info isn't empty
        if pd.isnull(info):
            continue

        print(f"\n\n{info_category}: {info}")

# This function will handle all user input
def get_input(df):
    print("Welcome to the automated country profile generator!\n")

    # getting the user's committe, topic, and country
    committee = input("What is your committee? ")
    topic = input("\nWhat is your topic? ")

    while True:
        country = input("\nWhat is your country? ")

        # making sure user's country is valid
        if country.lower() in df["Country"].values:
            print(f"\nYour committee: {committee}\nYour topic: {topic}\nYour country: {country.title()}")
            input("\nPress enter to continue, or Ctrl + c to cancel: ")

            return committee, topic, country

        else:
            print(f"\n{country} is an invalid country. Please try again.")