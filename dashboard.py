from tkinter import*
import sqlite3
from PIL import Image,ImageTk
from tkinter import messagebox
from course import CourseClass
from student import StudentClass
from exam import ExamClass
from st_exam import ScoreClass
from result import ResultClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #title
        title=Label(self.root,text="INDIRA GANDHI DELHI TECHNICAL UNIVERSITY FOR WOMEN\nStudent Result Management System",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=100)
        
        #menu
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=100,width=1330,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=110,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=325,y=5,width=200,height=40)
        btn_exam=Button(M_Frame,text="Exam",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_exam).place(x=545,y=5,width=200,height=40)
        btn_st_exam=Button(M_Frame,text="Marks",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_st_exam).place(x=765,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=990,y=5,width=200,height=40)
        
        #image
        self.bg_img=Image.open("igdtuw_logo.png")
        self.bg_img=self.bg_img.resize((820,500),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=20,y=190,width=820,height=500)

        #update
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="darkorange",fg="white")
        self.lbl_course.place(x=900,y=220,width=300,height=90)

        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=900,y=330,width=300,height=90)

        self.lbl_exam=Label(self.root,text="Total Exams\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_exam.place(x=900,y=440,width=300,height=90)

        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_result.place(x=900,y=550,width=300,height=90)
        self.update_details()
#Functions======================================================================================================================================
    def update_details(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from exam")
            cr=cur.fetchall()
            self.lbl_exam.config(text=f"Total Exams\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")


            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def add_course(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=CourseClass(self.new_win)  

    def add_student(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=StudentClass(self.new_win) 

    def add_exam(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=ExamClass(self.new_win)

    def add_st_exam(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=ScoreClass(self.new_win) 

    def add_result(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=ResultClass(self.new_win)                    
        
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
