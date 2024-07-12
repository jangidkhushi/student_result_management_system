from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ExamClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #title
        title=Label(self.root,text="Exam Record",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180)
        
        #variables
        self.var_exam=StringVar()
        self.var_of_marks=StringVar()
        self.var_start_date=StringVar()
        self.var_end_date=StringVar()
        #widgets
        lbl_examName=Label(self.root,text="Exam Name",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=60)
        lbl_of_marks=Label(self.root,text="Of Marks",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=100)
        lbl_start_date=Label(self.root,text="Start Date",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=140)
        lbl_end_date=Label(self.root,text="End Date",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=180)
        lbl_syllabus=Label(self.root,text="Syllabus",font=("goudy old style",15,"bold"),bg="white").place(x=10,y=220)
        
        #entry fields
        self.txt_examName=Entry(self.root,textvariable=self.var_exam,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_examName.place(x=150,y=60,width=200)

        txt_of_marks=Entry(self.root,textvariable=self.var_of_marks,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=100,width=200)

        txt_start_date=Entry(self.root,textvariable=self.var_start_date,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=150,y=140,width=200)

        self.txt_end_date=Entry(self.root,textvariable=self.var_end_date,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_end_date.place(x=150,y=180,width=200)

        self.txt_syllabus=Text(self.root,font=("goudy old style",15,"bold"),bg="lightyellow")
        self.txt_syllabus.place(x=150,y=220,width=500,height=100)

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
        lbl_search_examName=Label(self.root,text="Exam Name",font=("goudy old style",15,"bold"),bg="white").place(x=720,y=60)
        txt_search_examName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg="lightyellow").place(x=870,y=60,width=180)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,'bold'),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)
       
        #content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","of_marks","start_date","end_date","syllabus"))
        self.CourseTable.heading("cid",text="ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("of_marks",text="Of Marks")
        self.CourseTable.heading("start_date",text="Start Date")
        self.CourseTable.heading("end_date",text="End Date")
        self.CourseTable.heading("syllabus",text="Syllabus")
        self.CourseTable["show"]='headings'

        self.CourseTable.column("cid",width=30)
        self.CourseTable.column("name",width=70)
        self.CourseTable.column("of_marks",width=70)
        self.CourseTable.column("start_date",width=80)
        self.CourseTable.column("end_date",width=80)
        self.CourseTable.column("syllabus",width=130)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#---------------------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.show()
        self.var_exam.set('')
        self.var_of_marks.set('')
        self.var_start_date.set('')
        self.var_end_date.set('')
        self.var_search.set('')
        self.txt_syllabus.delete('1.0',END)
        self.txt_examName.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_exam.get()=="":
                messagebox.showerror("Error","Exam name should be required",parent=self.root)
            else:
                cur.execute("select * from exam where name=?",(self.var_exam.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select exam from the list",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from exam where name=?",(self.var_exam.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Exam deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")                

    def get_data(self,ev):
        self.txt_examName.config(state="readonly")
        self.txt_examName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_exam.set(row[1])
        self.var_of_marks.set(row[2])
        self.var_start_date.set(row[3])
        self.var_end_date.set(row[4])
        self.txt_syllabus.delete('1.0',END)
        self.txt_syllabus.insert(END,row[5])

    def add(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_exam.get()=="":
                messagebox.showerror("Error","Exam name should be required",parent=self.root)
            else:
                cur.execute("select * from exam where name=?",(self.var_exam.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Exam name already present",parent=self.root)
                else:
                    cur.execute("insert into exam(name,of_marks,start_date,end_date,syllabus)values(?,?,?,?,?)",(
                        self.var_exam.get(),
                        self.var_of_marks.get(),
                        self.var_start_date.get(),
                        self.var_end_date.get(),
                        self.txt_syllabus.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Exam added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
            
    def update(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            if self.var_exam.get()=="":
                messagebox.showerror("Error","Exam name should be required",parent=self.root)
            else:
                cur.execute("select * from exam where name=?",(self.var_exam.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select exam from list",parent=self.root)
                else:
                    cur.execute("update exam set of_marks=?,start_date=?,end_date=?,syllabus=? where name=?",(
                        self.var_of_marks.get(),
                        self.var_start_date.get(),
                        self.var_end_date.get(),
                        self.txt_syllabus.get("1.0",END),
                        self.var_exam.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Exam updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    
            

    def show(self):
        con=sqlite3.connect(database="equinox.db")
        cur=con.cursor()
        try:
            cur.execute("select * from exam")
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
            cur.execute(f"select * from exam where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  
         

           
if __name__=="__main__":
    root=Tk()
    obj=ExamClass(root)
    root.mainloop()