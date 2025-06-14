#!/bin/bash

# Save this script by name updated-run.sh
# In updated-run.sh, make following changes
# Volume mount the current folder on the host to the folder "/hostfolder"
# Pass the GREETING env var with value "Spring was earlier."
# make sure to provide your image name
# And don't forget to make the updated-run.sh script executable (chmod +x updated-run.sh)


docker run -p 5002:5001 -d prk546-assignment1:latest

#docker run -p 5001:5001 -v $(pwd):/hostfolder -e GREETING="Spring was earlier." -d prk546-assignment1:latest  
