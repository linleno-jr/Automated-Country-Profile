import pandas as pd
from docx import Document
from input import get_input

# creating a data frame from csv
df = pd.read_csv("filtered_countries.csv")

# converting country names in data frame to lowercase
df["Country"] = df["Country"].str.lower()

"""
list of columns needed
Government: Country name - conventional long form
Government: Capital - name
Geography: Climate
Geography: Terrain
Geography: Coastline
Environment: Environment - current issues
Environment: Environment - international agreements - party to
Geography: Location
Geography: Map references              Region country is most associated with
Geography: Area - comparative
Government: Government type
Government: Independence
Government: International organization participation
Military and Security: Military expenditures
"""

def main():

    # getting input from the user
    committee, topic, country = get_input(df)

if __name__ == "__main__":
    main()