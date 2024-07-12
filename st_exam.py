from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ScoreClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #title
        title=Label(self.root,text="Exam Scores Record",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180)

        #variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks_ob=StringVar()
        self.var_marks_total=StringVar()#total marks
        self.var_percentage=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        
        #widgets
        lbl_select_stName=Label(self.root,text="Select Student",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=70)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=120)
        lbl_course=Label(self.root,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=170)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=220)
        lbl_marks_total=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=270)

        #entry fields
        self.txt_select_stName=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_select_stName.place(x=540,y=70,width=200)
        self.txt_select_stName.set("Select")
        #search button
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=750,y=70,width=120,height=28)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=540,y=120,width=330)

        txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow",state='readonly').place(x=540,y=170,width=330)

        self.txt_marks_ob=Entry(self.root,textvariable=self.var_marks_ob,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_marks_ob.place(x=540,y=220,width=330)

        self.txt_marks_total=Entry(self.root,textvariable=self.var_marks_total,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_marks_total.place(x=540,y=270,width=330)

        #buttons
        self.btn_add=Button(self.root,text='Submit',font=("goudy old style",15,'bold'),bg="lightgreen",fg="black",cursor="hand2",command=self.add)
        self.btn_add.place(x=500,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,'bold'),bg="yellow",fg="black",cursor="hand2",command=self.update)
        self.btn_update.place(x=630,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="lightgray",fg="black",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=760,y=400,width=110,height=40)

        #functions

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks_ob.set("")
        self.var_marks_total.set("")
    
    def fetch_roll(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])    
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def update(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Exam name should be required",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select exam from list",parent=self.root)
                else:
                    per=(int(self.var_marks_ob.get())*100)/int(self.var_marks_total.get())
                    cur.execute("update result set name=?,course=?,marks_ob=?,marks_total=?,percentage=? where roll=?",(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_marks_total.get(),
                        str(per),
                        self.var_roll.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Scores updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")            
            
    def add(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Scores already present",parent=self.root)
                else:
                    per=(int(self.var_marks_ob.get())*100)/int(self.var_marks_total.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,marks_total,percentage)values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_marks_total.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Scores added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")   

    def search(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")                         

if __name__=="__main__":
    root=Tk()
    obj=ScoreClass(root)
    root.mainloop()        