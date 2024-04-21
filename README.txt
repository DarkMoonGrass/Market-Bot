This is Grass' fork of the Marketbot
https://github.com/ian2102/Market-Bot/tree/main

This bot can crawl between pages

To use you are going to have to change the coordiantes for each click.
To change what pages you want to crawl all you have to do is add strings to the "items" list near the start of the program

ISSUES and BUGS
This bot CANNOT switch between coloumns so it cannot track the left colum for mystic gem or skull key and the right coloumn for stackable consumables at the same time.

The market page becomes laggy and unresponsive, the bot should face issues at the 3 Hour mark, Fix is in development.








Setup Guide

Install Python:
Download and install Python https://www.python.org/downloads/
Run the installer and follow the on-screen instructions.

Install Tesseract OCR:
Windows:
Download the Tesseract installer from https://github.com/UB-Mannheim/tesseract/wiki
Run the installer and follow the on-screen instructions.
During installation, make sure to add Tesseract to your system PATH.

Install Python Dependencies:
Open a terminal or command prompt.
Navigate to the directory containing the script files.
Run the following command to install dependencies:
pip install -r requirements.txt
This will install all the required Python packages for the scripts to run.


Get Region Coordinates:
Open a terminal or command prompt.
Navigate to the directory containing the script files.
Run the script region.py using the following command:
python main.py
Follow the on-screen instructions.

Run the Main Script:
Open a terminal or command prompt.
Navigate to the directory containing the script files.
Run the script main.py using the following command:
python main.py
Follow the on-screen instructions.
