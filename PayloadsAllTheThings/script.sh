#!/bin/bash

# Loop through each folder in the current directory
for folder in */; do
    # Remove the trailing slash to get the folder name
    folder_name=$(basename "$folder")

    # Check if a file named "README" exists in the folder
    if [ -e "${folder}README" ]; then
        # Rename the "README" file to the folder name
        mv "${folder}README" "${folder}${folder_name}"
        echo "Renamed ${folder}README to ${folder}${folder_name}"
    fi
done

