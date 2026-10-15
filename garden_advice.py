"""
Garden Advice App

This program asks the user for a season and plant type, then displays
gardening advice based on their answers.
"""

def get_gardening_advice(season, plant_type):
    """Returns gardening advice for the chosen season and plant type."""
    advice_by_season = {
        "spring": "Plant new seeds and watch for late frosts.",
        "summer": "Water your plants regularly and provide some shade.",
        "autumn": "Clear fallen leaves and prepare sensitive plants for colder weather.",
        "winter": "Protect your plants from frost with covers.",
    }

    advice_by_plant = {
        "flower": "Use suitable fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests and check your vegetables regularly.",
        "herb": "Harvest herbs regularly to encourage healthy new growth.",
        "houseplant": "Check the soil before watering and provide suitable light.",
    }

    # Gets advice for the season and plant type.
    season_advice = advice_by_season.get(
        season, "No advice is available for that season."
    )
    plant_advice = advice_by_plant.get(
        plant_type, "No advice is available for that type of plant."
    )

    return f"Season advice: {season_advice}\nPlant advice: {plant_advice}"


def main():
    """Collect user choices and display the matching advice."""
    valid_seasons = ("spring", "summer", "autumn", "winter")
    valid_plants = ("flower", "vegetable", "herb", "houseplant")

    # Asks for input instead of using hardcoded values.
    season = input(
        "Choose a season (spring, summer, autumn, winter): "
    ).strip().lower()
    plant_type = input(
        "Choose a plant type (flower, vegetable, herb, houseplant): "
    ).strip().lower()

    # Explains the available choices when the user enters an unrecognised value.
    if season not in valid_seasons:
        print("That season is not recognised. The program will still provide general advice.")
    if plant_type not in valid_plants:
        print("That plant type is not recognised. The program will still provide general advice.")

    print()
    print(get_gardening_advice(season, plant_type))


if __name__ == "__main__":
    main()
