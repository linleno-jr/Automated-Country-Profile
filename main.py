import pandas as pd
from country_io import output_country_info, get_input
from data.info import columns_needed

# creating a data frame from csv file that contains data needed
df = pd.read_csv("data/filtered_countries.csv")

# converting country names in data frame to lowercase for easier access
df["Country"] = df["Country"].str.lower()

# main function
def main():

    # getting input from the user
    committee, topic, country = get_input(df)

    # outputting info on the country based on the user's input
    output_country_info(df, country, columns_needed)

if __name__ == "__main__":
    # running main function, handling keyboard interrupt error
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled by user.")
