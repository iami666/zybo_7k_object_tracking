# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 12:53:33 2018

@author: patelviv
"""
import sys

import numpy as np
import cv2
import pickle
import pygame
import os
from definition import define

def file_path_check(file_name_fm_same_dir):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name_fm_same_dir)
    if not os.path.exists(file_path):
        print("[ERROR] does not exist path  {} ".format(file_path))
        sys.exit(-1)
    else:
        print("[INFO] checked path {} ".format(file_path))
        return file_path

def face_recog_pygm(screen, title):

    print("[INFO] face_recog_pygm start")

    # objected created for cascadeclassifer
    face_cascade_name = "haarcascade_frontalface_default.xml"
    face_cascade_path = file_path_check(face_cascade_name)
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    recognizer = cv2.face.createLBPHFaceRecognizer()

    recognizer_file = "trainner.yml"
    recognizer_path = file_path_check(recognizer_file)
    file_path_check(recognizer_path)
    recognizer.load(recognizer_path)


    labels={"person_name" : 1}
    labels_file = "labels.pickle"
    labels_path = file_path_check(labels_file)
    try:
        with open(labels_path, 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k, v in og_labels.items()}
    except Exception as error:
        print(error)
        raise

    cap = cv2.VideoCapture(0)

    while cap.isOpened():

        ret, frame = cap.read()

        # resize frame for required size
        resize_frame = cv2.resize(frame, (define.HORIZ_PIXELS_SMALL, define.VERT_LINES_SMALL))

        # opencv understand BGR, inorder to display we need to convert image  form   BGR to RGB
        frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2RGB) # for display

        # covert image into gray
        gray = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY) # for processing

        # detect object of different size i nthe input image.
        # the detected objects are returned as a list of rectangles.
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+w), (255, 0, 0), 2) # RGB
            roi_gray= gray[y:y+h, x:x+w]
            # roi_color = frame[y:y+h, x:x+w]

            id_ = recognizer.predict(roi_gray)
            # id_, conf = recognizer.predict(roi_gray)

            # if conf >= 30 or conf<= 85:
            front = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,0,0)
            # width of text
            stroke = 2

            cv2.putText(frame, name, (x,y), front, 1.0, color, stroke, cv2.LINE_AA)


        # Display the frame
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        screen.blit(title, (200, 25))
        screen.blit(frame, (50, 100)) # x, y
        # screen.blit(frame, (50, 50))  # x, y


        pygame.display.flip()
        if cv2.waitKey(30) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

def main():

    # objected created for cascadeclassifer
    face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.createLBPHFaceRecognizer()

    recognizer.load("trainner.yml")

    print("hre")
    labels={"person_name" : 1}
    with open("labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v:k for k, v in og_labels.items()}

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("frame")
    # read image through cv2
    #img = cv2.imread(r'C:\Users\PatelViv\opencv\images\viv\viv_4.jpg')



    while cap.isOpened():

        ret, frame = cap.read()
        # covert image into gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detecte object of different size i nthe input image.
        #the detected objects are returned as a list of rectangles.
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+w), (0,0,225), 2) #BGR
            roi_gray= gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            id_, conf = recognizer.predict(roi_gray)

            if conf >= 30 or conf<= 85:
                front = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255,255,255)
                stroke = 2

            cv2.putText(frame, name, (x,y), front, 1, color, stroke, cv2.LINE_AA)


        # Display the frameq
        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()