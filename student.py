from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x680+0+0")
        self.root.title('Student Portal')

    #adding imagees
        img = Image.open('img//clg.jpg')
        img = img.resize((700, 170), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(img)
        label_1 = Label(self.root, image=self.pic)
        label_1.place(x=0, y=0,  width=700, height=170)

        img1 = Image.open('img//student.jpg')
        img1 = img1.resize((700, 170), Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(img1)
        label_2 = Label(self.root, image=self.pic1)
        label_2.place(x=700, y=0,  width=700, height=170)

    # adding background image
        img_b = Image.open('img//sbg.jpg')
        img_b = img_b.resize((1530, 700))
        self.bg_pic = ImageTk.PhotoImage(img_b)

        bg_label = Label(self.root, image=self.bg_pic)
        bg_label.place(x=0, y=171, width=1530, height=700)

        text_label = Label(bg_label, text='STUDENT PORTAL ', font=('times new roman', 25, 'bold'), fg='green', bg='white')
        text_label.place(x=0, y=0, width=1530,height=35)

    #Creating frame
        main_frame = Frame(bg_label,bg='white', bd=2)
        main_frame.place(x=5, y=40, width=1350, height=600)

        #left frame
        left_frame = LabelFrame(main_frame, bg='white', bd=2, relief=SUNKEN,text='Add Student Details')
        left_frame.place(x=10, y=10, width=630, height=580)

        img_s = Image.open('img//sbg.jpg')
        img_s = img_s.resize((700, 200))
        self.s_pic = ImageTk.PhotoImage(img_s)

        s_label = Label(left_frame, image=self.s_pic)
        s_label.place(x=0, y=0, width=700, height=120)

        #Course details frame
        course_frame = LabelFrame(left_frame, bg='white',bd=1, relief=RIDGE, text="Course Information")
        course_frame.place(x=10, y=125,width=610, height=80)

        self.var_course = StringVar()
        d_label = Label(course_frame, text="Course", bg="white", font=('times new roman', 14, 'bold'))
        d_label.grid(row=0, column=0, padx=10, pady=10)

        d_combox = ttk.Combobox(course_frame, width=25, state='readonly', textvariable=self.var_course)
        d_combox['values'] = ('select course', 'BCA', 'BBA', 'B.tech')
        d_combox.current(0)
        d_combox.grid(row=0, column=1)

        sem_label = Label(course_frame, text="Semester", bg="white", font=('times new roman', 14, 'bold'))
        sem_label.grid(row=0, column=3, padx=10, pady=10)

        self.var_sem = StringVar()
        sem_combox = ttk.Combobox(course_frame, width=25, state='readonly', textvariable=self.var_sem,)
        sem_combox['values'] = ('select Semester', '1', '2', '3', '4', '5', '6')
        sem_combox.current(0)
        sem_combox.grid(row=0, column=5)

        #student details
        s_frame = LabelFrame(left_frame, bg='white', bd=1, relief=RIDGE, text="Student Information")
        s_frame.place(x=10, y=210, width=610, height=220)

        #adding labels and entryboxes
        roll_label = Label(s_frame, text="Student Roll No:",bg='white', font=('times new roman', 12))
        roll_label.grid(row=0, column=0, sticky='w')
        self.var_rollno = StringVar()
        roll_entry = ttk.Entry(s_frame, width=20, textvariable=self.var_rollno)
        roll_entry.grid(row=0, column=1, padx=5, pady=7)

        name_label = Label(s_frame, text="Student Name:", bg='white', font=('times new roman', 12))
        name_label.grid(row=0, column=3, sticky='w', padx=10)
        self.var_name = StringVar()
        name_entry = ttk.Entry(s_frame, width=20, textvariable=self.var_name)
        name_entry.grid(row=0, column=4, padx=5, pady=7)

        dob_label = Label(s_frame, text="DOB:", bg='white', font=('times new roman', 12))
        dob_label.grid(row=1, column=0, sticky='w')
        self.var_dob = StringVar()
        dob_entry = ttk.Entry(s_frame, width=20, textvariable=self.var_dob)
        dob_entry.grid(row=1, column=1, padx=5, pady=7)

        phone_label = Label(s_frame, text="Phone No :", bg='white', font=('times new roman', 12))
        phone_label.grid(row=2, column=0, sticky='w')
        self.var_phone = StringVar()
        phone_entry = ttk.Entry(s_frame, width=20, textvariable=self.var_phone)
        phone_entry.grid(row=2, column=1, padx=5, pady=7)

        add_label = Label(s_frame, text="E-mail :", bg='white', font=('times new roman', 12))
        add_label.grid(row=1, column=3, sticky='w', padx=10,pady=7)
        self.var_email = StringVar()
        add_entry = ttk.Entry(s_frame, textvariable=self.var_email, width=20)
        add_entry.grid(row=1, column=4, padx=5, pady=7)

        gender_label = Label(s_frame, text="Gender :", bg='white', font=('times new roman', 12))
        gender_label.grid(row=2, column=3, sticky='w', padx=10, pady=7)
        self.var_gender = StringVar()
        gender_combox = ttk.Combobox(s_frame, textvariable=self.var_gender, width=17, state = 'readonly')
        gender_combox['values'] = ('Select Gender', 'Male', 'Female')
        gender_combox.current(0)
        gender_combox.grid(row=2, column=4, padx=5, pady=7)

        # Button frame
        b_frame = LabelFrame(s_frame, bg='white', bd=1, relief=RIDGE)
        b_frame.place(x=1, y=120, width=605, height=80)

        #adding buttons
        save_button = Button(b_frame, text="SAVE", fg='white', command=self.add_details, bg='orange',font=('times new roman', 12, 'bold'), width=20)
        save_button.grid(row=0, column=0, padx=5,pady=5)

        update_button = Button(b_frame, text="UPDATE",command=self.update_data, fg='white', bg='blue', font=('times new roman', 12, 'bold'),width=20)
        update_button.grid(row=0, column=1, padx=5, pady=5)

        delete_button = Button(b_frame, text="DELETE", fg='white', command=self.delete_data, bg='red', font=('times new roman', 12, 'bold'),width=20)
        delete_button.grid(row=0, column=3, padx=5, pady=5)

        photo_button = Button(b_frame, text="TAKE PHOTO", fg='white',command=self.dataset, bg='purple', font=('times new roman', 12, 'bold'),width=20)
        photo_button.grid(row=1, column=0, padx=10)

        update_button = Button(b_frame, text="UPDATE PHOTO", fg='white', bg='purple', font=('times new roman', 12, 'bold'),
                              width=20)
        update_button.grid(row=1, column=1,padx=10)

        #right frame
        right_frame = LabelFrame(main_frame, bg='white', bd=2, relief=SUNKEN, text='Students Record')
        right_frame.place(x=650, y=10, width=630, height=580 )

        search_frame = LabelFrame(right_frame, bg='white', bd=1, relief=SUNKEN)
        search_frame.place(x=1, y=5, width=620, height=90)

        #adding label and buttons for searching
        search_label = Label(search_frame, text="Search By :", bg='white', font=('times new roman', 15, 'bold'))
        search_label.grid(row=0, column=0, sticky='w', padx=5, pady=3)
        search_combox = ttk.Combobox(search_frame,state='readonly' )
        search_combox['values'] = ('Select', 'Name', 'Roll No')
        search_combox.current(0)
        search_combox.grid(row=0, column=1, padx=10, pady=3)
        search_entry = ttk.Entry(search_frame, width=25)
        search_entry.grid(row=0, column=4, padx=10, pady=3)

        search_button = Button(search_frame, text="SEARCH", fg='white', bg='red', font=('times new roman', 12, 'bold'), width=15)
        search_button.grid(row=1, column=0, padx=10, pady=5)

        show_button = Button(search_frame, text="SHOW ALL", fg='white', bg='magenta', font=('times new roman', 12, 'bold'), width=15)
        show_button.grid(row=1, column=1, padx=10, pady=5)

        #table frame for showing records
        table_frame = Frame(right_frame, bg='white', bd=2, relief=RIDGE)
        table_frame.place(x=1, y=100, width=620, height=330)

        #scroll bars
        x_scrollbar = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        y_scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)

        #res = ['Name', 'Course', 'Semester', 'DOB', 'E-mail', 'Phone No', 'Roll No', 'Gender']
        self.s_table = ttk.Treeview(table_frame, column=('course', 'sem', 'roll no','name', 'dob', 'phone', 'email', 'gender' ),
                                    xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

        x_scrollbar.pack(side=BOTTOM, fill=X)
        y_scrollbar.pack(side=RIGHT, fill=Y)
        x_scrollbar.config(command=self.s_table.xview)
        y_scrollbar.config(command=self.s_table.yview)

        self.s_table.heading('course', text='Course')
        self.s_table.heading('sem', text='Semester')
        self.s_table.heading('roll no', text='Roll No')
        self.s_table.heading('name', text='Student Name')
        self.s_table.heading('dob', text='DOB')
        self.s_table.heading('phone', text='Phone No')
        self.s_table.heading('email', text='E-mail')
        self.s_table.heading('gender', text='Gender')
        self.s_table["show"] = "headings"
        self.s_table.pack(expand=1, fill=BOTH)
        self.s_table.bind('<ButtonRelease>', self.hover)
        self.fetch()


    def add_details(self):
        if (self.var_course.get() == 'select course' or self.var_sem.get()== 'select Semester' or self.var_rollno.get()==''
            or self.var_name.get() == '' or self.var_gender.get() == 'Select Gender' or self.var_dob.get() ==''
           or self.var_email.get()== ''or self.var_phone.get() == ''):
            messagebox.showerror("Error", 'All fields are Mandatory', parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212", database="attendancedb")
                cur = mydb.cursor()
                cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.var_course.get(), self.var_sem.get(), self.var_rollno.get(), self.var_name.get(),
                         self.var_dob.get(),self.var_phone.get()
                        ,self.var_email.get(), self.var_gender.get()))

                mydb.commit()
                self.fetch()
                mydb.close()
                messagebox.showinfo('Success', 'Details added to database', parent=self.root)

            except Exception as e:
                messagebox.showerror('Error', f'{str(e)}', parent=self.root)

    def fetch(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212", database="attendancedb")
        cur = mydb.cursor()
        cur.execute('select * from students')
        data = cur.fetchall()

        if len(data) != 0:
            self.s_table.delete(*self.s_table.get_children())
            for i in data:
                self.s_table.insert("", END, values=i)
            mydb.commit()
        mydb.close()

    def hover(self, event=""):
        cursor = self.s_table.focus()
        content = self.s_table.item(cursor)
        data = content['values']
        self.var_course.set(data[0])
        self.var_sem.set(data[1])
        self.var_rollno.set(data[2])
        self.var_name.set(data[3])
        self.var_dob.set(data[4])
        self.var_phone.set(data[5])
        self.var_email.set(data[6])
        self.var_gender.set(data[7])

    def update_data(self):
        if (self.var_course.get() == 'select course' or self.var_sem.get()== 'select Semester' or self.var_rollno.get()==''
            or self.var_name.get() == '' or self.var_gender.get() == 'Select Gender' or self.var_dob.get() ==''
           or self.var_email.get()== ''or self.var_phone.get() == ''):
            messagebox.showerror("Error", 'All fields are Mandatory', parent=self.root)
        else:
            try:
                update = messagebox.askyesno('Update', 'Want to update the data', parent=self.root)
                if update:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212",database="attendancedb")
                    cur = mydb.cursor()
                    cur.execute("UPDATE students SET Course=%s, Semester=%s, Name=%s, DOB=%s, Phone_No=%s, Email=%s,Gender=%s WHERE ROll_No=%s",
                        (self.var_course.get(), self.var_sem.get(),  self.var_name.get(),
                         self.var_dob.get(),self.var_phone.get()
                        ,self.var_email.get(), self.var_gender.get(), self.var_rollno.get()))

                else:
                    if not update:
                        return
                messagebox.showinfo('Success', "Updated Successfully", parent=self.root)
                mydb.commit()
                self.fetch()
                mydb.close()
            except Exception as e:
                messagebox.showerror('Error',f'{str(e)}', parent=self.root)

    def delete_data(self):
        if self.var_rollno == '':
            messagebox.showerror("Error", 'Please Enter the RollNo', parent=self.root)
        else:
           delete = messagebox.askyesno("Delete","Sure to Delete", parent=self.root)
           try:
               if delete:
                mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212", database="attendancedb")
                cur = mydb.cursor()
                cur.execute('delete from students where Roll_No=%s', (self.var_rollno.get(),))
               else:
                   if not delete:
                       return
               mydb.commit()
               self.fetch()
               mydb.close()
               messagebox.showinfo("Deleted",'Deleted Successfully', parent=self.root)
           except Exception as e:
               messagebox.showerror("Error", f'{str(e)}', parent=self.root)

    def dataset(self):
        if (self.var_course.get() == 'select course' or self.var_sem.get() == 'select Semester' or self.var_rollno.get() == ''
                or self.var_name.get() == '' or self.var_gender.get() == 'Select Gender' or self.var_dob.get() == ''
                or self.var_email.get() == '' or self.var_phone.get() == ''):
            messagebox.showerror("Error", 'All fields are Mandatory', parent=self.root)
        else:
            try:
                mydb = mysql.connector.connect(host="localhost", user="root", password="raghav1212",database="attendancedb")
                cur = mydb.cursor()
                cur.execute('select * from students')
                my_data = cur.fetchall()
                id = 0
                for x in my_data:
                    id += 1
                cur.execute("UPDATE students SET Course=%s, Semester=%s, Name=%s, DOB=%s, Phone_No=%s, Email=%s,Gender=%s WHERE ROll_No=%s",
                (self.var_course.get(), self.var_sem.get(), self.var_name.get(),
                 self.var_dob.get(), self.var_phone.get()
                 , self.var_email.get(), self.var_gender.get(), self.var_rollno.get() == id+1,))
                mydb.commit()
                self.fetch()
                mydb.close()
                
                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def cropped(img):
                    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(grey, 1.3, 5)

                    for (x, y, w, h) in faces:
                        cropped = img[y:y+h, x:x+w]
                        return cropped

                capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                img_id = 0
                while True:
                    ret, capture_frame = capture.read()
                    if cropped(capture_frame) is not None:
                        img_id += 1
                        face = cv2.resize(cropped(capture_frame), (500, 500))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path = "photos/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id),(50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 200, 0), 2)
                        cv2.imshow('Faces', face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 60:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Done', 'Pictures Captured', parent=self.root)
                self.train_dataset()


            except Exception as e:
                messagebox.showerror('Error', f'{e}', parent=self.root)



    def train_dataset(self):
        data_file = "photos"
        files = [os.path.join(data_file, file) for file in os.listdir(data_file)]

        id_s = []
        faces = []

        for img in files:
            image = Image.open(img).convert('L')
            image_np = np.array(image, 'uint8')
            id_ = int(os.path.split(img)[1].split('.')[1])

            faces.append(image_np)
            id_s.append(id_)
        id_s = np.array(id_s)

        # training classifier
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, id_s)
        classifier.write("classifier.xml")


if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
