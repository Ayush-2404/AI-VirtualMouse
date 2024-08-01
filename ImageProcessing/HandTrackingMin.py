import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)   #video capture using webcam no0.

#this is related to the hand detection model
mpHands = mp.solutions.hands
#can be skipped too.
hands = mpHands.Hands(False)  #obj created. Ctrl+click on hands opens the function and shows what parameters are already written.
mpDraw = mp.solutions.drawing_utils #function by mediapipe to detect the 21 points on the palm

pTime = 0
cTime = 0

while True:
    success, img = cap.read()   #frame
    #send rgb img to "hands" so first we convert it into cuz this class(obj) only uses rgb
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #there is a method inside this obj called process that will process the frame and give the results.
    results = hands.process(imgRGB)#process method will process the frame for us
    print(results.multi_hand_landmarks)#multi_hand_lankdarks tells if smtg is detected or not. If it sees hand it prints (Values)else "None"

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #mpDraw.draw_landmarks(img, handLms)   #draws the hand for us. (DOTS)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()    #gives the current time
    fps = 1/ ( cTime - pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)   #using in image and converting it into string. Giving it a POSITION, FONT, SCALE, COLOUR, THICKNESS.

    cv2.imshow("Image", img)  #to use webcam
    cv2.waitKey(1)