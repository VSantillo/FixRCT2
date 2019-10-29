#!/usr/local/bin/python3

# Import statements
import os  # Move around and inspect directories
import sys  # Why do I need this?
import json  # To handle the json data

whats_happening = '''Starting RCT2 Fix
-------------------
This script can fix aspects of RCT2 that I don't like.
This script sets the 'VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH' to false.
This prevents rides like the Side Friction Coaster from crashing when going over hills too quickly.
It's more fun this way.
This could be expanded, if I find more use for it.'''

# TODO: Linux and Windows? What are their typical paths?
best_path_guess = f'/Users/{os.getenv("USER")}/Library/Application Support/OpenRCT2/bin/OpenRCT2.app/Contents' \
                  f'/Resources/object/rct2/ride '

def no_upstop_wheels(data):
    # Determine if ride has the NO_UPSTOP flag
    if 'properties' in data.keys():
        if 'cars' in data['properties'].keys():
            if type(data['properties']['cars']) is dict:
                data["properties"]["cars"]["VEHICLE_ENTRY_FLAG_NO_UPSTOP_BOBSLEIGH"] = False

            with open(filename, "w") as fn:
                json.dump(data, fn, indent=4)
                print(f'{filename} was updated')


if __name__ == "__main__":
    # Let the user know what's happening
    print(whats_happening)

    # TODO: Accept path from input args
    # Move to RCT2 Directory
    os.chdir(best_path_guess)

    print(f'Operating in: {os.getcwd()}')

    # Iterate through all files in the directory
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.json'):
            with open(filename, 'r') as fn:
                data = json.load(fn)

                no_upstop_wheels()
