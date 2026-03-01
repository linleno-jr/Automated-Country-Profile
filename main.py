import pandas as pd
from input import get_input
from output import output_country_info

# creating a data frame from csv
df = pd.read_csv("data/filtered_countries.csv")

# converting country names in data frame to lowercase
df["Country"] = df["Country"].str.lower()

columns_needed = [
    "Government: Country name - conventional long form",
    "Government: Capital - name",
    "Geography: Climate",
    "Geography: Terrain",
    "Geography: Coastline",
    "Environment: Environment - current issues",
    "Environment: Environment - international agreements - party to",
    "Geography: Location",
    "Geography: Map references",
    "Geography: Area - comparative",
    "Government: Government type",
    "Government: Independence",
    "Government: International organization participation",
    "Military and Security: Military expenditures",
    "People and Society: Ethnic groups",
    "People and Society: Languages",
    "People and Society: Religions",
    "People and Society: Infant mortality rate - total",
    "People and Society: Life expectancy at birth - total population",
    "People and Society: Population growth rate",
    "People and Society: Population distribution",
    "People and Society: Literacy - male",
    "People and Society: Literacy - female",
    "People and Society: Median age - total",
    "People and Society: Net migration rate",
    "Transnational Issues: Refugees and internally displaced persons - refugees (country of origin)",
    "Economy: GDP (official exchange rate)",
    "Economy: Real GDP per capita",
    "Geography: Natural resources",
    "Economy: Exports - commodities",
    "Economy: Exports - partners",
    "Economy: Imports - commodities",
    "Economy: Imports - partners",
]

def main():

    # getting input from the user
    committee, topic, country = get_input(df)

    output_country_info(df, country, columns_needed)

if __name__ == "__main__":
    main()