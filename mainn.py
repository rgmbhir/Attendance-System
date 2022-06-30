from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from Face_Detector import Detector
from attendencee import Attnedence
import sys


class Attendence_system:
    def __init__(self, root):
        #for tkinter window
        self.root = root
        self.root.geometry("1530x700+0+0")
        self.root.title('Attendace System using Face Recognition')

        #background image
        img_b = Image.open('img//back.jpg')
        img_b = img_b.resize((1530, 700), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(img_b)

        bg_label = Label(self.root, image=self.bg_image )
        bg_label.place(width=1530, height=700)

        #Student Button
        img = Image.open('img//ss.jpg')
        img = img.resize((220, 220))
        self.picture = ImageTk.PhotoImage(img)

        student_b= Button(self.root, image=self.picture, cursor='hand2', command=self.student_window)
        student_b.place(x=100, y=200)

        student_b1 = Button(self.root, text='Student Portal', cursor='hand2', bg='purple', fg='white',
                            font=('times new roman',13, 'bold'), command=self.student_window)
        student_b1.place(x=100, y=425, width=225, height=30)

        # Face recognition Button
        img3 = Image.open('img//fce.jpg')
        img3 = img3.resize((220, 220))
        self.picture3 = ImageTk.PhotoImage(img3)

        face_b = Button(self.root, command=self.face, image=self.picture3, cursor='hand2')
        face_b.place(x=400, y=200)

        face_b1 = Button(self.root, text='Face Detector', command=self.face, cursor='hand2', bg='blue', fg='white',
                        font=('times new roman', 13, 'bold'))

        face_b1.place(x=400, y=425, width=225, height=30)

        # attendance Button
        img2 = Image.open('img//att.jpeg')
        img2 = img2.resize((220, 220))
        self.picture2 = ImageTk.PhotoImage(img2)

        attendance_b = Button(self.root, image=self.picture2, command=self.attendance, cursor='hand2')
        attendance_b.place(x=700, y=200)

        attendence1_b1 = Button(self.root, text='Attendence', command=self.attendance, cursor='hand2', bg='red', fg='white',
                            font=('times new roman', 13, 'bold'))
        attendence1_b1.place(x=700, y=425, width=225, height=30)

        # exit Button
        img4 = Image.open('img//exit.jpg')
        img4 = img4.resize((220, 220))
        self.picture4 = ImageTk.PhotoImage(img4)

        exit_b= Button(self.root, image=self.picture4, cursor='hand2', command=sys.exit)
        exit_b.place(x=1000, y=200)

        exit_b1 = Button(self.root, text='Exit', cursor='hand2', bg='blue', fg='white', command=sys.exit,
                        font=('times new roman', 13, 'bold'))
        exit_b1.place(x=1000, y=425, width=225, height=30)

    def student_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def face(self):
        self.new_window = Toplevel(self.root)
        self.app = Detector(self.new_window)

    def attendance(self):
        self.new = Toplevel(self.root)
        self.app = Attnedence(self.new)


if __name__ == '__main__':
    root = Tk()
    obj = Attendence_system(root)
    root.mainloop()
