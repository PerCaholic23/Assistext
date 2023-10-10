# Assistext
This is the source code for our project called **Assistext**. Assistext is the device that can help visual impairements enjoy their books easier. We are embarking on this project to help person who is blind reading easier. By developing the innovation called Assistext. This project is important because this project can significantly improve blind community in terms of receiving information from publications. We believe that by our strategies, we can achieve our desired outcomes. 

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

## Require libraries
1. OpenCV
   `sudo pip install opencv-python`
2. Google Text-to-Speech
   `sudo pip install gTTS`
3. Tesseract OCR
   `sudo pip install tesseract-ocr` 
4. Pytesseract
   `sudo pip install pytesseract`
5. Tesseract development package 
   `sudo apt install libtesseract-dev`
6. Thai language dataset (optional)
    `sudo apt-get install tesseract-ocr-tha`

## How to use our device
1. When the device is turned on, it will be provided a voice instruction for the visually impaired to understand how it works.
2. Bring the documents / various publications that we want to know placed on the pedestal.
3. Then press the record button (circle button) to take the images of the document / printed media to be processed and then output to user.
Also, you can press the replay button (square button) in case you want the device to repeat sentence. Last but not least you can adjust the volume by twisting it in the middle of the device.

## The result
<div align = "center">
    <img src="https://i.imgur.com/qIhH4XX.png">
</div>
This is the result of the image that was captured with the camera and then use OpenCV to revert the images to monochrome (black and white). This method will make the computer easier to seprete the texts from images.

## 3D model
<div align = "center">
    <img src="https://i.imgur.com/DOFrKD6.png">
</div>
