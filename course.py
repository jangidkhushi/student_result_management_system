from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #title
        title=Label(self.root,text="Course Record",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180)
        
        #variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_faculty=StringVar()
        self.var_exam=StringVar()
        #widgets
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_duration=Label(self.root,text="Duration",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_charges=Label(self.root,text="Charges",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_faculty=Label(self.root,text="Faculty",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_description=Label(self.root,text="Description",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        lbl_exam=Label(self.root,text="Exam",font=("goudy old style",15,"bold"),bg="white").place(x=400,y=60)
        
        #entry fields
        self.exam_list=["Select"]
        #function call
        self.fetch_exam()
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_courseName.place(x=150,y=60,width=200)

        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)

        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)

        self.txt_faculty=Entry(self.root,textvariable=self.var_faculty,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_faculty.place(x=150,y=180,width=200)

        self.txt_description=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_description.place(x=150,y=220,width=500,height=100)
        
        self.txt_exam=ttk.Combobox(self.root,textvariable=self.var_exam,values=self.exam_list,font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_exam.place(x=470,y=60,width=200)
        self.txt_exam.current(0)

        #buttons
        self.btn_add=Button(self.root,text='Save',font=("goudy old style",15,'bold'),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("goudy old style",15,'bold'),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("goudy old style",15,'bold'),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,'bold'),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        #search panel
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
       
        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","faculty","exam","description"))
        self.CourseTable.heading("cid",text="ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("faculty",text="Faculty")
        self.CourseTable.heading("exam",text="Exam")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("cid",width=30)
        self.CourseTable.column("name",width=50)
        self.CourseTable.column("duration",width=90)
        self.CourseTable.column("charges",width=60)
        self.CourseTable.column("faculty",width=70)
        self.CourseTable.column("exam",width=70)
        self.CourseTable.column("description",width=100)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#---------------------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.show()
        self.var_course.set('')
        self.var_duration.set('')
        self.var_charges.set('')
        self.var_faculty.set('')
        self.var_exam.set('')
        self.var_search.set('')
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)

    def fetch_exam(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select name from exam")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.exam_list.append(row[0])    
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    

    def delete(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select course from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")                

    def get_data(self,ev):
        self.txt_courseName.config(state="readonly")
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.var_faculty.set(row[4])
        self.var_exam.set(row[5])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[6])

    def add(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course name already present",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,faculty,exam,description)values(?,?,?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.var_faculty.get(),
                        self.var_exam.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
            
    def update(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,faculty=?,exam=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.var_faculty.get(),
                        self.var_exam.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
            

    def show(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  

    def search(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  
         

           
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()