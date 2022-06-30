from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
from tkinter import filedialog
import csv
import os


data = []
class Attnedence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x680+0+0")
        self.root.title('Student Portal')

        # adding imagees
        img = Image.open('img//clg.jpg')
        img = img.resize((700, 170), Image.ANTIALIAS)
        self.pic = ImageTk.PhotoImage(img)
        label_1 = Label(self.root, image=self.pic)
        label_1.place(x=0, y=0, width=700, height=170)

        img1 = Image.open('img//student.jpg')
        img1 = img1.resize((700, 170), Image.ANTIALIAS)
        self.pic1 = ImageTk.PhotoImage(img1)
        label_2 = Label(self.root, image=self.pic1)
        label_2.place(x=700, y=0, width=700, height=170)

        img_b = Image.open('img//sbg.jpg')
        img_b = img_b.resize((1530, 700))
        self.bg_pic = ImageTk.PhotoImage(img_b)

        bg_label = Label(self.root, image=self.bg_pic)
        bg_label.place(x=0, y=171, width=1530, height=700)

        text_label = Label(bg_label, text='Attendence PORTAL ', font=('times new roman', 25, 'bold'), fg='green', bg='white')
        text_label.place(x=0, y=0, width=1530, height=35)

        # Creating frame
        main_frame = Frame(bg_label, bg='white', bd=2)
        main_frame.place(x=5, y=40, width=1350, height=600)

        # left frame
        left_frame = LabelFrame(main_frame, bg='white', bd=2, relief=SUNKEN, text='Student Details')
        left_frame.place(x=10, y=10, width=630, height=580)

        img_s = Image.open('img//sbg.jpg')
        img_s = img_s.resize((700, 200))
        self.s_pic = ImageTk.PhotoImage(img_s)

        s_label = Label(left_frame, image=self.s_pic)
        s_label.place(x=0, y=0, width=700, height=120)

        #course frame
        course_frame = LabelFrame(left_frame, bg='white', bd=1, relief=RIDGE, text="Course Information")
        course_frame.place(x=10, y=125, width=610, height=500)

        roll_label = Label(course_frame, text="Student Roll No:", bg='white', font=('times new roman', 14))
        roll_label.grid(row=0, column=0, sticky='w')
        self.var_rollno = StringVar()
        roll_entry = ttk.Entry(course_frame, width=20, textvariable=self.var_rollno)
        roll_entry.grid(row=0, column=1, padx=5, pady=10)

        name_label = Label(course_frame, text="Student Name:", bg='white', font=('times new roman', 14))
        name_label.grid(row=1, column=0, sticky='w', pady=10)
        self.var_name = StringVar()
        name_entry = ttk.Entry(course_frame, width=20, textvariable=self.var_name)
        name_entry.grid(row=1, column=1, padx=5, pady=7)

        date_label = Label(course_frame, text="Date:", bg='white', font=('times new roman', 14))
        date_label.grid(row=2, column=0, sticky='w')
        self.var_date = StringVar()
        date_entry = ttk.Entry(course_frame, width=20, textvariable=self.var_date)
        date_entry.grid(row=2, column=1, padx=5, pady=10)

        status_label = Label(course_frame, text="Status :", bg='white', font=('times new roman', 14))
        status_label.grid(row=4, column=0, sticky='w', pady=10)
        self.var_status = StringVar()
        status_combox = ttk.Combobox(course_frame, textvariable=self.var_status, width=17, state='readonly')
        status_combox['values'] = ('Status', 'Present', 'Absent')
        status_combox.current(0)
        status_combox.grid(row=4, column=1, padx=5, pady=7)

        # Button frame
        b_frame = LabelFrame(course_frame, bg='white', bd=1, relief=RIDGE)
        b_frame.place(x=1, y=220, width=605, height=80)

        # adding buttons
        import_button = Button(b_frame, text="Import Csv", command=self.importcsv, fg='white', bg='orange',
                             font=('times new roman', 12, 'bold'), width=15)
        import_button.grid(row=0, column=0, padx=2, pady=5)

        export_button = Button(b_frame, text="Export Csv", command=self.export, fg='white', bg='blue',
                               font=('times new roman', 12, 'bold'), width=15)
        export_button.grid(row=0, column=1, padx=2, pady=5)

        update_button = Button(b_frame, text="Update", fg='white', bg='red',
                               font=('times new roman', 12, 'bold'), width=15)
        update_button.grid(row=0, column=2, padx=2, pady=5)

        reset_button = Button(b_frame, text="Reset", fg='white', bg='green', command=self.reset,
                              font=('times new roman', 12, 'bold'), width=15)
        reset_button.grid(row=0, column=3, padx=2, pady=5)

        # right frame
        right_frame = LabelFrame(main_frame, bg='white', bd=2, relief=SUNKEN, text='Attendence ')
        right_frame.place(x=650, y=10, width=630, height=580)

        table_frame = Frame(right_frame, bg='white', bd=2, relief=RIDGE)
        table_frame.place(x=1, y=5, width=620, height=400)

        # scroll bars
        x_scrollbar = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        y_scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendence_table = ttk.Treeview(table_frame, column=('roll no', 'name', 'course', 'date', 'status'),
                                             xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)

        x_scrollbar.pack(side=BOTTOM, fill=X)
        y_scrollbar.pack(side=RIGHT, fill=Y)
        x_scrollbar.config(command=self.attendence_table.xview)
        y_scrollbar.config(command=self.attendence_table.yview)

        self.attendence_table.heading('roll no', text='Roll No')
        self.attendence_table.heading('name', text='Student Name')
        self.attendence_table.heading('course', text='Course')
        self.attendence_table.heading('date', text='Date')
        self.attendence_table.heading('status', text='Status')
        self.attendence_table["show"] = "headings"

        '''self.attendence_table.column('roll no', width=100)
        self.attendence_table.column('name', width=100)
        self.attendence_table.column('course', width=100)
        self.attendence_table.column('date', width=100)
        self.attendence_table.column('status', width=100)
'''
        self.attendence_table.pack(expand=1, fill=BOTH)
        self.attendence_table.bind("<ButtonRelease>", self.hover)
        self.fetch(data)

    def fetch(self, rows):
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert('', END, values=i)

    def importcsv(self):
        global data
        data.clear()
        file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Open csv', filetypes=(('CSV File', '*.csv'),
                                          ('All File', '*.*')), parent=self.root)

        with open(file) as f:
            read = csv.reader(f, delimiter=',')
            for i in read:
                data.append(i)
            self.fetch(data)

    def export(self):
        try:
            if len(data) < 1:
                messagebox.showerror('Error', 'No Data Found', parent=self.root)
                return
            file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Open csv', filetypes=(('CSV File', '*.csv'),
                                                ('All File', '*.*')),parent=self.root)
            with open(file, 'w', newline="") as f:
                writer = csv.writer(f, delimiter=",")
                for i in data:
                    writer.writerow(i)
        except Exception as e:
            messagebox.showerror('Error', f'{e}', parent=self.root)

    def hover(self, event=""):
        cursor = self.attendence_table.focus()
        content = self.attendence_table.item(cursor)
        rows = content['values']
        self.var_rollno.set(rows[0])
        self.var_name.set(rows[1])
        self.var_date.set(rows[2])
        self.var_status.set(rows[3])

    def reset(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_date.set("")
        self.var_status.set("")


if __name__ == '__main__':

    root = Tk()
    obj = Attnedence(root)
    root.mainloop()