import cv2
import mediapipe as mp
from time import sleep

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    sleep(0.2)
    ret, img = cap.read()
    results = hands.process(img)

    if results.multi_hand_landmarks:


        for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
            print('\n-----------------------')

        WRIST_X = hand_landmarks.landmark[mp_hands.HandLandmark(0).value].x
        WRIST_Y = hand_landmarks.landmark[mp_hands.HandLandmark(0).value].y

        THUMB_CMC_X = hand_landmarks.landmark[mp_hands.HandLandmark(1).value].x
        THUMB_CMC_Y = hand_landmarks.landmark[mp_hands.HandLandmark(1).value].y

        THUMB_MCP_X = hand_landmarks.landmark[mp_hands.HandLandmark(2).value].x
        THUMB_MCP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(2).value].y

        THUMB_DIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(3).value].x
        THUMB_DIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(3).value].y

        THUMB_TIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(4).value].x
        THUMB_TIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(4).value].y
        THUMB_TIP_Z = hand_landmarks.landmark[mp_hands.HandLandmark(4).value].z

        INDEX_MCP_X = hand_landmarks.landmark[mp_hands.HandLandmark(5).value].x
        INDEX_MCP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(5).value].y

        INDEX_PIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(6).value].x
        INDEX_PIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(6).value].y
        INDEX_PIP_Z = hand_landmarks.landmark[mp_hands.HandLandmark(6).value].z

        INDEX_DIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(7).value].x
        INDEX_DIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(7).value].y

        INDEX_TIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(8).value].x
        INDEX_TIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(8).value].y

        MIDDLE_MCP_X = hand_landmarks.landmark[mp_hands.HandLandmark(9).value].x
        MIDDLE_MCP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(9).value].y

        MIDDLE_PIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(10).value].x
        MIDDLE_PIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(10).value].y
        MIDDLE_PIP_Z = hand_landmarks.landmark[mp_hands.HandLandmark(10).value].z

        MIDDLE_DIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(11).value].x
        MIDDLE_DIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(11).value].y

        MIDDLE_TIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(12).value].x
        MIDDLE_TIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(12).value].y

        RING_MCP_X = hand_landmarks.landmark[mp_hands.HandLandmark(13).value].x
        RING_MCP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(13).value].y

        RING_PIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(14).value].x
        RING_PIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(14).value].y
        RING_PIP_Z = hand_landmarks.landmark[mp_hands.HandLandmark(14).value].z

        RING_DIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(15).value].x
        RING_DIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(15).value].y

        RING_TIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(16).value].x
        RING_TIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(16).value].y

        PINKY_MCP_X = hand_landmarks.landmark[mp_hands.HandLandmark(17).value].x
        PINKY_MCP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(17).value].y

        PINKY_PIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(18).value].x
        PINKY_PIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(18).value].y
        PINKY_PIP_Z = hand_landmarks.landmark[mp_hands.HandLandmark(18).value].z

        PINKY_DIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(19).value].x
        PINKY_DIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(19).value].y

        PINKY_TIP_X = hand_landmarks.landmark[mp_hands.HandLandmark(20).value].x
        PINKY_TIP_Y = hand_landmarks.landmark[mp_hands.HandLandmark(20).value].y


        """for i in range(20):
            print(f'{mp_hands.HandLandmark(i).name}:')
            print(f'{hand_landmarks.landmark[mp_hands.HandLandmark(i).value]}')"""

        if (THUMB_TIP_Y < (PINKY_PIP_Y and PINKY_TIP_Y)) and THUMB_TIP_X < RING_PIP_X and THUMB_TIP_X > PINKY_PIP_X:
            print("M")
        elif (RING_TIP_Y > PINKY_TIP_Y) and (THUMB_TIP_Y < (PINKY_TIP_Y and RING_TIP_Y)) and (MIDDLE_TIP_Y < THUMB_TIP_Y) and (INDEX_TIP_Y < THUMB_TIP_Y) and (THUMB_TIP_X > MIDDLE_TIP_X) and (THUMB_TIP_X < INDEX_TIP_X):
            print("K")
        elif (THUMB_TIP_Y < (INDEX_PIP_Y and INDEX_TIP_Y and MIDDLE_PIP_Y and MIDDLE_TIP_Y and RING_TIP_Y and RING_PIP_Y and PINKY_PIP_Y and PINKY_TIP_Y)) and (THUMB_TIP_Z < MIDDLE_PIP_Z)and (THUMB_TIP_Z < RING_PIP_Z) and (THUMB_TIP_Z < INDEX_PIP_Z) and (THUMB_TIP_Z < PINKY_PIP_Z):
            print("S")
        elif (THUMB_TIP_Y < (INDEX_PIP_Y and INDEX_TIP_Y and MIDDLE_PIP_Y and MIDDLE_TIP_Y and RING_TIP_Y and RING_PIP_Y and PINKY_PIP_Y and PINKY_TIP_Y)) and THUMB_TIP_X > INDEX_PIP_X:
            print("A")
        elif (THUMB_TIP_Y < (INDEX_PIP_Y and INDEX_TIP_Y and MIDDLE_PIP_Y and MIDDLE_TIP_Y and RING_TIP_Y and RING_PIP_Y and PINKY_PIP_Y and PINKY_TIP_Y)) and THUMB_TIP_X < INDEX_PIP_X and THUMB_TIP_X > MIDDLE_PIP_X:
            print("T")
        elif (THUMB_TIP_Y < (INDEX_PIP_Y and INDEX_TIP_Y and MIDDLE_PIP_Y and MIDDLE_TIP_Y and RING_TIP_Y and RING_PIP_Y and PINKY_PIP_Y and PINKY_TIP_Y)) and THUMB_TIP_X < MIDDLE_PIP_X and THUMB_TIP_X > RING_PIP_X:
            print("N")
        elif (INDEX_TIP_Y < INDEX_DIP_Y) and (MIDDLE_TIP_Y < MIDDLE_DIP_Y) and (RING_TIP_Y < RING_DIP_Y) and (PINKY_TIP_Y < PINKY_PIP_Y) and (RING_TIP_X<THUMB_TIP_X<INDEX_TIP_X):
            print("B")
        elif (PINKY_TIP_Y<THUMB_TIP_Y) and (PINKY_TIP_Y< (INDEX_TIP_Y and MIDDLE_TIP_Y and RING_TIP_Y)) and (THUMB_TIP_Y < (INDEX_TIP_Y and MIDDLE_TIP_Y and RING_TIP_Y)):
            print("Y")
        elif (INDEX_TIP_Y < INDEX_DIP_Y) and (MIDDLE_PIP_Y < MIDDLE_DIP_Y) and (RING_PIP_Y < RING_DIP_Y) and (PINKY_PIP_Y < PINKY_DIP_Y) and (THUMB_TIP_X < THUMB_DIP_X):
            print("D")
        elif (THUMB_TIP_Y > (INDEX_PIP_Y and INDEX_TIP_Y and MIDDLE_PIP_Y and MIDDLE_TIP_Y and RING_TIP_Y and RING_PIP_Y and PINKY_PIP_Y and PINKY_TIP_Y) and (INDEX_DIP_Y < INDEX_TIP_Y) and (MIDDLE_DIP_Y < MIDDLE_TIP_Y) and (RING_DIP_Y < RING_TIP_Y) and (PINKY_DIP_Y < PINKY_TIP_Y)):
	        print("C")

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark)

    cv2.imshow("Feed", img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
