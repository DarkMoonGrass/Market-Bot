#Grass' fork of the Market Bot
import pyautogui
import pytesseract
import time
import re
import os
import datetime
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

#Enter in names of items you want to track
ticker = 0
IMsShittyCoding = 0
items = "Gold Ingot", "Gold Powder", "Gold Ore", "Rubysilver Ingot"
upper = len(items) - 1

#print (items)


data_dir = 'data/'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

existing_files = os.listdir(data_dir)

counter = 0

for file in existing_files:
    match = re.search(r'(\d+)', file)
    if match:
        number = int(match.group(1))
        counter = max(counter, number)

counter += 1

filename = f'{data_dir}averages{counter}'

print("Filename:", filename)

time.sleep(3)

#===================Search and Get===================
#====================================================
while True:
    if IMsShittyCoding == 20:
        pyautogui.moveTo(162, 43, duration=0.01)
        pyautogui.click(162, 43)
        time.sleep(0.5)
        pyautogui.moveTo(864, 616, duration=0.01)
        pyautogui.click(864, 616)
        pyautogui.moveTo(1178, 254, duration=0.01)
        pyautogui.click(1178, 254)
        IMsShittyCoding = 0
        time.sleep(0.5)
    if ticker < upper:
        ticker += 1
        IMsShittyCoding += 1
    else:
        ticker = 0
        IMsShittyCoding += 1

    #Click Reset
    pyautogui.click(247, 206)
    #Click Tab Down
    pyautogui.click(127, 205)
    #Click Test Entry
    pyautogui.click(79, 244)
    #Type in Item
    pyautogui.write(items[ticker], interval = 0.05)
    #Check Box
    pyautogui.click(111, 279)
    #Filter
    pyautogui.moveTo(1788, 277, duration=0.01)
    pyautogui.click(1788, 277)
    time.sleep(3)
    print("----------" + str(items[ticker]) + "-----------")
    
    screenshot = pyautogui.screenshot()

    # Right Slot (1599, 340, 1693, 956)
    # Left Slot(1473, 338, 1549, 958) (1588, 334, 1641, 955)
    region = (1599, 340, 1693, 956)

    cropped_image = screenshot.crop(region)

    cropped_image = cropped_image.convert('L')

    text = pytesseract.image_to_string(cropped_image)
    new_text = ""
    lines = text.split("\n")
    for line in lines:
        new_line = line.split("x")
        new_text += new_line[0] + "\n"

    values = re.findall(r'(\d+\.\d+|\d+)', new_text)
    #print(new_text)
    #print(values)

    if values:
        total = sum(float(value) for value in values)
        average = total / len(values)
        low = values[0]
        high = values[-1]
        if float(average) < float(low):
            average = low
    else:
        middle = 0
        low = 0
        high = 0 
    print("Low " + str(low))
    print("Average " + str(average))
    print("High " + str(high))
    
    current_datetime = datetime.datetime.now()

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    data = f"{formatted_datetime},{average},{high},{low}\n"
    with open(filename+ str(items[ticker]) + ".csv", "a") as file:
        file.write(data)
    time.sleep(1)
