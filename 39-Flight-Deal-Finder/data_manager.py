from pprint import pprint

import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a42fa8b3975fee3420f30a5d825612f4/[100DaysOfPython]FlightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Todo 39.2.2: Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]  # "prices" = name of sheet on GSheet

        # Todo 39.2.3: Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # Todo 39.2.6: In the DataManager Class make a PUT request and use the row id from sheet_data
    #  to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
