# Home Automation Project

## Introduction

- The purpose of this project is to allow the user to access their room and all its appliances on the Internet. The front end allows the user to easily control the relays that are connected to different appliances.
- This is also an introductory project designed to be the center for a curriculum for ECLAIR members who choose to be a part of the beginner's track

## Installation (Highly recommend using Linux or MacOS for this or a WSL if you are on Windows)

### Note: The backend can only be run on a Raspberry Pi due to the usage of RPi.GPIO library which lets python applications change the state of GPIO pins in a raspberry pi

- Clone the Repo
- create a new virtual environment using ```python -m venv <name-for-environment>``` or if you are using miniconda or anaconda (recommended) ```conda create --name <name-for-environment>```
- cd into backend-service ```cd backend-service```
- activate virtual environment using ```conda activate <name-for-environment``` (if using miniconda or anaconda) or ```bash ./<name-for-environment>/bin/activate```
- run ```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt``` if you are on a mac
- run ```make run``` to start the backend server
- start a new terminal and cd into frontend-service ```cd frontend-service```
- run ```npm install```
- run ```npm start``` to start up the frontend
- You should now see a new browser window open and the webpage displayed!

## Backend

- Lets user add appliances
- Lets user change the state of appliances
- Lets user stream audio using a .wav file or a youtube video link

## Frontend

- Contains cards for each appliance that allow user to change the state of an appliance
- Contains cards for Youtube Audio inks and .wav audio files


