#!/usr/bin/python
import os, time, sys, cv2, subprocess, multiprocessing 
import RPi.GPIO as GPIO
from smbus import SMBus
from pytesseract import pytesseract
from gtts import gTTS

addr = 0x8
bus = SMBus(1)
GPIO.setmode(GPIO.BCM)
bReading = 27 #Replay
bCapturing = 26 #Capture adn read

GPIO.setup(bReading, GPIO.IN)
GPIO.setup(bCapturing, GPIO.IN)
vid = cv2.VideoCapture(0)

def MainStatement():
    while(True):
        bReadingState = GPIO.input(bReading)
        bCapturingState = GPIO.input(bCapturing)
        try:
            if bReadingState == True and bCapturingState == True:
                print("Close")
                break

            elif bReadingState == True: #Replay
                print("Reading")
                os.system("cvlc --play-and-exit --quiet /home/pi/VoiceFromText.mp3")

            elif bCapturingState == False: #Capture, cvt to text and read
                print("Capture")
                os.system("cvlc --play-and-exit --quiet /home/pi/Capture.mp3")
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (0,0), sigmaX = 70, sigmaY = 70)
                divide = cv2.divide(gray, blur, scale = 255)
                thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
                kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
                morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernal)
                cv2.imwrite('Cvt_img.png', morph)
                print("saved")
                os.system("cvlc --play-and-exit --quiet /home/pi/CaptureComplete.mp3")
                time.sleep(2)
                img = cv2.imread('Cvt_img.png')
                text = pytesseract.image_to_string(img, lang = 'eng')
                print (text)
                myText = text
                language = 'en'
                output = gTTS(text = myText, lang = language, slow = False)
                output.save("VoiceFromText.mp3")
                os.system("cvlc --play-and-exit --quiet /home/pi/VoiceFromText.mp3")
                
        except AssertionError:
            print("No text detected")
            os.system("cvlc --play-and-exit --quiet /home/pi/ErrorSound.mp3")
            time.sleep(0.3)
            os.system("cvlc --play-and-exit --quiet /home/pi/NoText.mp3")
            continue
        
        except cv2.error:
            print("No camera")
            os.system("cvlc --play-and-exit --quiet /home/pi/ErrorSound.mp3")
            time.sleep(0.3)
            os.system("cvlc --play-and-exit --quiet /home/pi/CamNotDetect.mp3")
            continue

def VolumnControl():
    while(True):
        data = bus.read_byte(addr)
        if data == 0:
            os.system("amixer -q sset PCM 0%")
        elif data == 1:
            os.system("amixer -q sset PCM 25%")
        elif data == 2:
            os.system("amixer -q sset PCM 50%")
        elif data == 3:
            os.system("amixer -q sset PCM 75%")
        elif data == 4:
            os.system("amixer -q sset PCM 100%")
            
def ReadCam():
    while(True):
        global ret, frame
        ret, frame = vid.read()
        frame = cv2.resize(frame, (640, 480))
    
print ("Welcome")
os.system("cvlc --play-and-exit --quiet /home/pi/GreetingVoice.mp3")
if __name__ == '__main__':
    script0 = multiprocessing.Process(target=MainStatement)
    script1 = multiprocessing.Process(target=VolumnControl)
    script2 = multiprocessing.Process(target=ReadCam)

    script0.start()
    script1.start()
    script2.start()
