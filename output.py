column_to_name = {
    "Government: Country name - conventional long form": "Official Name of Country",
    "Government: Capital - name": "Capital",
    "Geography: Climate": "Climate",
    "Geography: Terrain": "Terrain",
    "Geography: Coastline": "Length of Coastline",
    "Environment: Environment - current issues": "Environmental Issues",
    "Environment: Environment - international agreements - party to": "Environmental Agreements",
    "Geography: Location": "Relative Location",
    "Geography: Map references": "Country Region",
    "Geography: Area - comparative": "Relative Area",
    "Government: Government type": "Type of Government",
    "Government: Independence": "Independence Year and Former Colonizer (if applicable)",
    "Government: International organization participation": "International Affiliations",
    "Military and Security: Military expenditures": "Military Expenditures Percent GDP",
    "People and Society: Ethnic groups": "Ethnic Composition",
    "People and Society: Languages": "Languages Spoken",
    "People and Society: Religions": "Major Religions",
    "People and Society: Infant mortality rate - total": "Infant Mortality Rate",
    "People and Society: Life expectancy at birth - total population": "Average Life Expectancy",
    "People and Society: Population growth rate": "Population Growth Rate",
    "People and Society: Population distribution": "Population Distribution",
    "People and Society: Literacy - male": "Literacy Rate for Men",
    "People and Society: Literacy - female": "Literacy Rate for Women",
    "People and Society: Median age - total": "Median Age",
    "People and Society: Net migration rate": "Net Immigration Rate",
    "Transnational Issues: Refugees and internally displaced persons - refugees (country of origin)": "Number of Refugees",
    "Economy: GDP (official exchange rate)": "GDP",
    "Economy: Real GDP per capita": "GDP Per Capita",
    "Geography: Natural resources": "Natural Resources",
    "Economy: Exports - commodities": "Export Commodities",
    "Economy: Exports - partners": "Export Partners",
    "Economy: Imports - commodities": "Import Commodities",
    "Economy: Imports - partners": "Import Partners",
}

# outputs info on a given country
def output_country_info(df, country: str, columns_needed: list):
    print(f"\nHere is the information on the country {country.title()}!")

    for column in columns_needed:
        info_category = column_to_name[column]
        info = df.loc[df["Country"] == country, column].iloc[0]

        # making sure info isn't empty
        if info == "":
            continue

        print(f"\n\n{info_category}: {info}")