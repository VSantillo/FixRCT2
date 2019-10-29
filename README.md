# FixRCT2

In OpenRCT2, some roller coasters are prone to derailing due to the lack of "upstop wheels". These wheels prevent the 
train from derailing when going over hills too quickly. This Python script crawls through the ride data files (JSON)
and checks if the `NO_UPSTOP` flag is set, and if it is, disable it. If you use the OpenRCT2 launcher, every update
will overwrite this data. This script should be run after the launcher updates, but before the game is launched. 

This could be expanded to other parts of the JSON files, but I don't have a use case for that. All it would require is 
adding more functions when it loops through all of the files. The default path is set to my own installation's path, but
another can be provided as an argument or in the Python script.

`./FixRCT2.py --path <path_to_ride_json_dir>`

You could also move it to your local bin and run it from anywhere.