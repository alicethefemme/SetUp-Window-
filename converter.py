import os
import json


def get_file_locations():
    # Create variable strings
    crime_file = ""
    outcome_file = ""

    crime_file_valid = False
    outcome_file_valid = False

    # While there is no valid crime file
    while not crime_file_valid:
        cf = input("Path to crime file (.CSV): ")

        # Check that the file ends in the right extension.
        if not cf.upper().endswith(".CSV"):
            continue

        # Check that the file exists in the filesystem
        if not os.path.exists(cf):
            continue

        with open(cf, 'r') as file:
            first_line = file.readlines()[0]
            # Check that the file has the right number of headers
            if len(first_line.split(",")) != 12:
                continue

            # Check that the file has the right headers.
            if first_line.replace("\n",
                                  "") != "Crime ID,Month,Reported by,Falls within,Longitude,Latitude,Location,LSOA code,LSOA name,Crime type,Last outcome category,Context":
                continue

        # Set the path for return.
        crime_file_valid = True
        crime_file = cf

    # While there is no valid outcome file:
    while not outcome_file_valid:
        of = input("Path to outcome fie (.CSV) ")

        # Check that the file ends in the right extension
        if not of.upper().endswith(".CSV"):
            continue

        # Check that hte file exists in the filesystem
        if not os.path.exists(of):
            continue

        with open(of, 'r') as file:
            first_line = file.readlines()[0]
            # Check that the file has the right number of headers
            if len(first_line.split(",")) != 10:
                continue

            # Check that the file has the right headers:
            if first_line.replace("\n",
                                  "") != "Crime ID,Month,Reported by,Falls within,Longitude,Latitude,Location,LSOA code,LSOA name,Outcome type":
                continue

        # Set the path for return.
        outcome_file_valid = True
        outcome_file = of

    # Return the crime file and outcome file.
    return crime_file, outcome_file


def process_crime_file(crime_file_path):
    return_list = []

    with open(crime_file_path, 'r') as file:
        # Go over each line in the file from the first line of data
        for line in file.readlines()[1:]:
            # Remove the new line character from the line.
            line = line.replace("\n", "")

            # Get the split line
            line_vals = line.split(",")

            # Get variables from the line
            crime_id, month, reported_by, falls_within, longitude, latitude, location, lsoa_code, lsoa_name, crime_type, last_outcome_cat, context = line_vals

            # Put variables into a dict
            dictt = {
                "crimeId": crime_id,
                "month": month,
                "reportedBy": reported_by,
                "fallsWithin": falls_within,
                "longitude": longitude,
                "latitude": latitude,
                "location": location,
                "LSOACode": lsoa_code,
                "LSOAName": lsoa_name,
                "crimeType": crime_type,
                "lastOutcomeCategory": last_outcome_cat,
                "context": context
            }

            # Add the dictionary to the list.
            return_list.append(dictt)

        return return_list


def process_outcome_file(outcome_file_location):
    return_list = []

    with open(outcome_file_location, 'r') as file:
        # Go over each line in the file from teh first line of data
        for line in file.readlines()[1:]:
            # Remove the new line character from the line
            line = line.replace("\n", '')

            # Get the split line
            line_vals = line.split(",")

            # Get variables from line
            crime_id, month, reported_by, falls_within, longitude, latitude, location, lsoa_code, lsoa_name, outcome_type = line_vals

            # Put variables into a dict
            dictt = {
                "crimeId": crime_id,
                "month": month,
                "reportedBy": reported_by,
                "fallsWithin": falls_within,
                "longitude": longitude,
                "latitude": latitude,
                "location": location,
                "LSOACode": lsoa_code,
                "LSOAName": lsoa_name,
                "outcomeType": outcome_type
            }

            # Add the dictionary to the return list
            return_list.append(dictt)

    return return_list


def create_outcome_file(crimes, outcomes):
    # Create and open the file.
    with open('output.json', 'w') as file:
        # Write the outcome to a file. Indent=4 to prettyprint.
        file.writelines(json.dumps(
            {"crimes": crimes,
             "outcomes": outcomes
             }, indent=4
        ))

    print(f"File has been processed and saved to {os.path.abspath('output.json')}")


if __name__ == "__main__":
    crime_file_location, outcome_file_location = get_file_locations()

    # Get a list of dictionaries of the crimes and outcomes
    crimes = process_crime_file(crime_file_location)
    outcomes = process_outcome_file(outcome_file_location)

    create_outcome_file(crimes, outcomes)
