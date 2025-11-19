def city_country(city, country, population=None):
    """Return a string like 'Santiago, Chile' or
    'Santiago, Chile - population 5000000'."""
    city = city.title()
    country = country.title()

    if population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"
