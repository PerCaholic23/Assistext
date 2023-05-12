import os, time, cv2
from pytesseract import pytesseract
from gtts import gTTS

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    #cv2.imshow('frame',frame)
    button = str(input("Type capture or read to init: "))
    if button == "capture":
        print("Capture")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(0,0),sigmaX=30,sigmaY=30)
        divide = cv2.divide(gray, blur, scale=255)
        thresh = cv2.threshold(divide,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(1,1))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernal)
        cv2.imwrite('T.png',morph)
        
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        print("Capture1")
        gray1 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray1 = cv2.bilateralFilter(gray,11,17,17)
        cv2.imwrite('T1.png',gray1)
        
    elif button == "read":
        print("Read")
        time.sleep(2)
        img = cv2.imread('T.png')
        text = pytesseract.image_to_string(img,lang='tha')
        print(text)
        myText = text
        language = 'th'
        output = gTTS(text = myText, lang = language, slow = False)
        
        output.save("VoiceOutput.mp3")
        print ("saved succesfully")
        os.system("xdg-open VoiceOutput.mp3")
    
    elif cv2.waitKey(1) & 0xFF == ord('t'):
        print("Read")
        time.sleep(2)
        img = cv2.imread('T1.png')
        text = pytesseract.image_to_data(img,config='')
        print(text)
        
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#cap.release()
#cv2.destroyAllWindows()

