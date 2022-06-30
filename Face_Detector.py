from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
import numpy as np


class Detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x680+0+0")
        self.root.title('Face Recognition')

        title_label = Label(self.root, text='Face Recognition', font=('times new roman', 30, 'bold'), fg='purple', bg='white')
        title_label.place(x=0, y=0, width=1350, height=45)

        img1 = Image.open('img//iStock-biometrics2.jpg')
        img1 = img1.resize((670, 640))
        self.bg_img1 = ImageTk.PhotoImage(img1)
        bg_label1 = Label(self.root, image=self.bg_img1)
        bg_label1.place(x=0, y=46, width=660, height=640)

        img2 = Image.open('img//facial_.jpg')
        img2 = img2.resize((690, 640))
        self.bg_img2 = ImageTk.PhotoImage(img2)
        bg_label2 = Label(self.root, image=self.bg_img2)
        bg_label2.place(x=651, y=46, width=690, height=640)

        button = Button(self.root, text='Scan Face', command=self.recognition, cursor='hand2', font=('times new roman', 14, 'bold'), bg='green', fg='white' )
        button.place(x=580, y=620, width=180, height=40)

    def recognition(self):

        def boundary(img, classifier, scale, neighbour, color, text, clf):
            grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grey_img, scale, neighbour)
            #cv2.CascadeClassifier.d
            cordinates = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (20, 20, 20), 2)
                id, predict = clf.predict(grey_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict//300)))

                mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212",
                                               database="attendancedb")
                cur = mydb.cursor()
                cur.execute("SELECT Name from students WHERE Roll_No="+str(id))
                n = cur.fetchone()
                #print(n)
                n = "+".join(n)

                cur.execute("SELECT Roll_No from students WHERE Roll_No="+str(id))
                r = cur.fetchone()
                r = '+'.join(r)
                cur.execute("SELECT Course from students WHERE Roll_No="+str(id))
                c = cur.fetchone()
                c = '+'.join(c)

                if confidence > 80:
                    cv2.putText(img, f'Name:{n}', (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 25, 0), 2)
                    self.attendence(n, r, c)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(img, 'Unknown Face', (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (25, 25, 250), 2)

                cordinates = [x, y, w, h]
            return cordinates

        def recognize(img, clf, cascade):
            cordinates = boundary(img, cascade, 1.2, 7, (50, 50, 50), "Face", clf)
            return img
        cascadee = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, im = video_cap.read()
            im = recognize(im, clf, cascadee)
            cv2.imshow("Welcome", im)

            if cv2.waitKey(1) == 13:
                break
                video_cap.release()
                cv2.destroyAllWindows()

    def attendence(self, n, r, c):
        with open("attendence_sheet.csv", 'r+', newline="\n") as f:
            data = f.readlines()
            name_list = []

            for i in data:
                entry = i.split(",")
                name_list.append(entry[0])
                #print(name_list)
            if (n not in name_list) and (r not in name_list) and (c not in name_list):
                date = datetime.now()
                d1 = date.strftime("%d/%m/%Y")
                time = date.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{c},{d1},{time},Present")




if __name__ == '__main__':
    root = Tk()
    obj = Detector(root)
    root.mainloop()