import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables
API_KEY = os.getenv('API_KEY')


def fetch_data(name):

    """
    function takes a name and requests at api for a json
    :param name:
    :return json :
    """

    # get animal json from api
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    # response = requests.get(api_url, headers={'X-Api-Key': 'dayY5a337OIGLd8VT9DB6w==KQPAMe23QmQtfWFv'})
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY })

    if response.status_code == requests.codes.ok:

        # get animal info as json
        animal_info_json = response.json()

        # return the info in a json format
        return animal_info_json

    else:

        error_text = f"<h2>The animal '{name}' doesn't exist.</h2>"

        # if an ERROR appears , this text will show
        if name == "":
            error_text = f"<h2>Please enter an animal name.</h2>"

        print(error_text)
        # print("Error:", response.status_code, response.text)


