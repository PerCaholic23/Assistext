# Assistext
This is the source code for our project called **Assistext**. Assistext is the device that can help visual impairements enjoy their books easier. 

## The devices that are used in our project
1. Raspberry pi 4
> This is the main device of our project, we use it as the main processor unit. We give it role as a sciprt 
2. Arduino Nano
> We use it as action reciver for instance, when you press the button, It will send signal to Arduino Nano and it will script into algoritim.
3. Hikvision 4k webcam
> This is the camera that we use to capture the image of the 
4. Potentiometer
> We use Portentiometer as a volume adjuster. You can twist to left to reduce the volumn and right to increasse the volume.
5. Speakers
> The speakers use to output sound to user so they can hear it.

## How to use our device
- When this device is turned on, it will provide voice instructions for the visually impaired to understand how this thing works.
- Let us bring the documents / various publications that we want to know placed on the pedestal.
- Then let us press the record button (circle button) to take the images of the document / print media to be processed and read aloud.
- And we can press the replay button. (square button) in case we want the device to repeat the page
- and can adjust the volume through the volume dial in the middle of the device

## Result
![This is the result](C:\Users\xphic\Downloads\350355808_1240011316632200_1619632047132876801_n.png)
```
sudo pip install opencv-python
sudo pip install gTTS
sudo pip install pytesseract
sudo apt update (optional)
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo apt-get install tesseract-ocr-tha (optional)

```
