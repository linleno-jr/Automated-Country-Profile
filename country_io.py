import pandas as pd
from data.info import column_to_name

def output_country_info(df, country: str, columns_needed: list):
    """ Prints out information on a country

    Args:
        df (pd.DataFrame: Input dataset
        country (str): Country to find info on
        columns_needed (list): Info on the country to pull
    """

    print(f"\nHere is the information on the country {country.title()}!")

    # printing out each column
    for column in columns_needed:
        info_category = column_to_name[column]
        info = df.loc[df["Country"] == country, column].iloc[0]

        # making sure info isn't empty
        if info == "":
            continue

        print(f"\n\n{info_category}: {info}")

# This function will handle all user input
def get_input(df):
    """ Gets input from the user, specifically their committee, topic, and country, then returns it.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        committee (str): user inputted committee
        topic (str): user inputted topic
        country (str): user inputted country, validated with dataset
    """

    print("Welcome to the automated country profile generator!\n")

    # getting the user's committe, topic, and country
    committee = input("What is your committee? ")
    topic = input("\nWhat is your topic? ")

    while True:
        country = input("\nWhat is your country? ").lower();

        # making sure user's country is valid, if it is, return values, else redo process
        if country.lower() in df["Country"].values:
            print(f"\nYour committee: {committee}\nYour topic: {topic}\nYour country: {country.title()}")
            input("\nPress enter to continue, or Ctrl + c to cancel: ")

            return committee, topic, country

        else:
            print(f"\n{country} is an invalid country. Please try again.")