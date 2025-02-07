
import json
import data_fetcher

def load_data():
  """ Loads a JSON file """
  with open("animal_data_from_user.json", "r") as handle:
    return json.load(handle)


def serialize_animal(animal):

    output = ''
    name = animal[0]['name']

    output += f'<li class="cards__item">\n'
    output += f'<div class ="card__title" > {name} </div>\n'

    diet = animal[0]['characteristics']['diet']
    output += f"<strong>Diet</strong>: {diet}<br/>\n"

    location = animal[0]['locations'][0]
    output += f"<strong>Location</strong>: {location}<br/>\n"

    if 'type' in animal[0]['characteristics'].keys() :
        type = animal[0]['characteristics']['type']
        output += f"<strong>Type</strong>: {type}<br/>\n"

    output += get_skin_types(animal)
    output += f" </li>\n"

    return output


def get_skin_types(animal):
    output_skin_type = ""
    if 'skin_type' in animal[0]['characteristics'].keys():
        skin_type = animal[0]['characteristics']['skin_type']
        output_skin_type = f"<strong>Skin Type</strong>: {skin_type}<br/>\n"
    return output_skin_type


def generate_html(animal):

    output = ''
    name = animal[0]['name']

    output += f'<li class="cards__item">\n'
    output += f'<div class ="card__title" > {name} </div>\n'

    diet = animal[0]['characteristics']['diet']
    output += f"<strong>Diet</strong>: {diet}<br/>\n"

    location = animal[0]['locations'][0]
    output += f"<strong>Location</strong>: {location}<br/>\n"

    if 'type' in animal[0]['characteristics'].keys():
        type = animal[0]['characteristics']['type']
        output += f"<strong>Type</strong>: {type}<br/>\n"

    output += get_skin_types(animal)
    output += f" </li>\n"

    return output


def get_user_input():

    """
    function asks the user for a name. at present when nothing is passed,
    the while loop will continue.
    :return:
    """
    animal_name_user = ""

    # get any INPUT
    while animal_name_user == "":

        # ask for an animal name from the user
        animal_name_user = input("Enter a name of an animal: ")

        if animal_name_user == "":
            print("ups. Try again.")

    return animal_name_user


def print_animal_data(animal_data):

    # Print formatted output
    for animal in animal_data:
        print(f"Name: {animal['name']}")
        print(f"Scientific Name: {animal['taxonomy']['scientific_name']}")
        print(f"Locations: {', '.join(animal['locations'])}")
        print(f"Top Speed: {animal['characteristics'].get('top_speed', 'N/A')}")
        print(f"Biggest Threat: {animal['characteristics'].get('biggest_threat', 'N/A')}")
        print("-" * 40)  # Separator line


def dump_animal_data_json(animal_data):
    # Dump JSON to a file
    with open("animal_data_from_user.json", "w") as json_file:
        json.dump(animal_data, json_file, indent=4)


def main():

    # get USER INPUT
    animal_name = get_user_input()

    # get the animal data by calling the function
    data = data_fetcher.fetch_data(animal_name)


    # print the entry information, if available
    if data:
        print_animal_data(data)
        dump_animal_data_json(data)
        user_animal_data = load_data()

        output = ''
        for x in range(len(user_animal_data)):
            # output += serialize_animal(animals_data)
            output += generate_html(user_animal_data)

        # Open a file in write mode and write output
        with open("user_animal_output.html", "w") as file:
            file.write(output)

    else:
        print(f"<h2>Try another name.</h2>")

if __name__ == "__main__":
    main()

