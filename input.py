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
            input("Press enter to continue, or Ctrl + c to cancel: ")

            return committee, topic, country

        else:
            print(f"\n{country} is an invalid country. Please try again.")