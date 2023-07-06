from tkinter import *
import tkinter.messagebox 
import mysql.connector as mysql
from tkinter import ttk

def main():
    root=Tk()
    app=Window1(root)
    root.mainloop()
class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Automatic Question Paper Generator System")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()
        

        self.LabelTitle=Label(self.frame,text="Automatic Question Paper Generator System",font=('arial',45,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=40)

        self.Loginframe1=Frame(self.frame,width=1010,height=300,bd=20,relief='ridge')
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3=Frame(self.frame,width=1000,height=200,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)

        #==============================================================================================================================================================
        self.LblUsername=Label(self.Loginframe1,text="Username",font=('arial',30,'bold'),bd=22,)
        self.LblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.Loginframe1,font=('arial',30,'bold'),bd=20,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)
        
        self.LblPassword=Label(self.Loginframe1,text="Password",font=('arial',30,'bold'),bd=22,)
        self.LblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.Loginframe1,font=('arial',30,'bold'),bd=20,textvariable=self.Password,show="*")
        self.txtPassword.grid(row=1,column=1,padx=85)
        
        #==============================================================================================================================================================

        self.btnLogin=Button(self.Loginframe2,text="Login",width=17,font=('arial',20,'bold'),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset=Button(self.Loginframe2,text="Reset",width=17,font=('arial',20,'bold'),command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit=Button(self.Loginframe2,text="Exit",width=17,font=('arial',20,'bold'),command=self.iExit)
        self.btnExit.grid(row=0,column=2)
        #==============================================================================================================================================================

        self.btnManage=Button(self.Loginframe3,text="Database Management System",state=DISABLED,command=self.Manage_window,font=('airal',20,'bold'))
        self.btnManage.grid(row=0,column=0,pady=8,padx=22)

        self.btnGenerate=Button(self.Loginframe3,text="Generate Question Paper",state=DISABLED,command=self.Generate_window,font=('airal',20,'bold'))
        self.btnGenerate.grid(row=0,column=1,pady=8,padx=22)

        #==============================================================================================================================================================
    def Login_System(self):
        user = (self.Username.get())
        pas =  (self.Password.get())
        if (user == "Management") and (pas == "Management"):
            self.btnManage.config(state = NORMAL)
            self.btnGenerate.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Automatic Question Paper Generator System","You have entered an invalid login details") 
            self.btnManage.config(state=DISABLED)
            self.btnGenerate.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    def Reset(self):
        self.btnManage.config(state=DISABLED)
        self.btnGenerate.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Automatic Question Paper Generator System","Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return 
            
        
        #==============================================================================================================================================================




        
    def Manage_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)
    def Generate_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)

class Window2:
    def __init__(self,master):
        self.master=master
        titlespace=" "
        self.master.title("Database Management System")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master,bd=10,width=770,height=700,relief=RIDGE)
        self.frame.grid()
        self.frame.pack()

        
        TitleFrame=Frame(self.frame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3=Frame(self.frame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)

        LeftFrame=Frame(TopFrame3,bd=5,width=770,height=400,padx=2,relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1=Frame(LeftFrame,bd=5,width=600,height=180,padx=12,pady=9,relief=RIDGE)
        LeftFrame1.pack(side=TOP)


        RightFrame1=Frame(TopFrame3,bd=5,width=100,height=400,padx=2,relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a=Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        #==============================================================================================================================================================
        Semester=StringVar()
        Subject=StringVar()
        Questions=StringVar()
        weightage=StringVar()
        Unit=StringVar()
        Difficult=StringVar()
        #==============================================================================================================================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("MySQL Connection","Confirm if you want to exit")
            if iExit>0:
                master.destroy()
                return
        def Reset():
            self.entSemester.delete(0,END)
            self.entSubject.delete(0,END)
            self.entQuestions.delete(0,END)
            self.entweightage.set("")
            self.entUnit.set("")
            self.Difficult.set("")

            
        def addData():
            if(Semester=="" or Subject==""or Questions=="" or weightage=="" or Unit=="" or Difficult==""):
                tkinter.messagebox.showerror("MySQL Connection","Enter Correct Details")
            else:
                sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
                cur=sqlCon.cursor()
                cur.execute("insert into question values(%s,%s,%s,%s,%s,%s)",(Semester.get(),Subject.get(),Questions.get(),weightage.get(),Unit.get(),Difficult.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("MySQL Connection","Record Entered Successfully")
                Reset()
                
        def display():
                sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
                cur=sqlCon.cursor()
                cur.execute("select * from question ")
                result=cur.fetchall()
                if len(result)!=0:
                    self.question.delete(*self.question.get_children())
                    for row in result:
                        self.question.insert('',END,values=row)
                    sqlCon.commit()
                sqlCon.close()

        def info(ev):
            viewinfo=self.question.focus()
            learnerData=self.question.item(viewinfo)
            row=learnerData['values']
            Semester.set(row[0])
            Subject.set(row[1])
            Questions.set(row[2])
            weightage.set(row[3])
            Unit.set(row[4])
            Difficult.set(row[5])
        def update():
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("update question set Semester=%s,Subject=%s,weightage=%s,Unit=%s,Difficult=%s where Questions=%s",(Semester.get(),Subject.get(),weightage.get(),Unit.get(),Difficult.get(),Questions.get()))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection","Record Updated Successfully")


        def delete():
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("delete from question where Questions='"+Questions.get()+"'")
            sqlCon.commit()
            display()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection","Record deleted Successfully")
            Reset()
       
            

            

            
        
                
            



        #==============================================================================================================================================================

        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text="Database Management System",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)
        
        
    
        self.lblSemester=Label(LeftFrame1,font=('arial',12,'bold'),text="Semester",bd=7)
        self.lblSemester.grid(row=0,column=0,sticky=W,padx=5)
        self.entSemester=Entry(LeftFrame1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=Semester)
        self.entSemester.grid(row=0,column=1,sticky=W,padx=5)
        
        
        self.lblSubject=Label(LeftFrame1,font=('arial',12,'bold'),text="Subject",bd=7)
        self.lblSubject.grid(row=1,column=0,sticky=W,padx=5)
        self.entSubject=Entry(LeftFrame1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=Subject)
        self.entSubject.grid(row=1,column=1,sticky=W,padx=5)


        self.lblQuestions=Label(LeftFrame1,font=('arial',12,'bold'),text="Questions",bd=7)
        self.lblQuestions.grid(row=2,column=0,sticky=W,padx=5)
        self.entQuestions=Entry(LeftFrame1,font=('arial',12,'bold'),bd=7,width=44,justify='left',textvariable=Questions)
        self.entQuestions.grid(row=2,column=1,sticky=W,padx=5)


        self.lblweightage=Label(LeftFrame1,font=('arial',12,'bold'),text="weightage",bd=7)
        self.lblweightage.grid(row=3,column=0,sticky=W,padx=5)
        self.entweightage=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=weightage)
        self.entweightage['values']=(' ','K1','K2','K3')
        self.entweightage.current(0)
        self.entweightage.grid(row=3,column=1)
        
        
        
        self.lblUnit=Label(LeftFrame1,font=('arial',12,'bold'),text="Unit",bd=7)
        self.lblUnit.grid(row=4,column=0,sticky=W,padx=5)
        self.entUnit=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=Unit)
        self.entUnit['values']=(' ','1','2','3','4','5')
        self.entUnit.current(0)
        self.entUnit.grid(row=4,column=1)



        self.Difficult=Label(LeftFrame1,font=('arial',12,'bold'),text="Difficult",bd=7)
        self.Difficult.grid(row=5,column=0,sticky=W,padx=5)
        self.Difficult=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=Difficult)
        self.Difficult['values']=(' ','1','2','3')
        self.Difficult.current(0)
        self.Difficult.grid(row=5,column=1)
        #==============================================================================================================================================================
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)

        self.question=ttk.Treeview(LeftFrame,height=12,columns=("Semester","Subject","Questions","weightage","Unit","Difficult"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.question.heading("Semester",text="Semester")
        self.question.heading("Subject",text="Subject")
        self.question.heading("Questions",text="Questions")
        self.question.heading("weightage",text="weightage")
        self.question.heading("Unit",text="Unit")
        self.question.heading("Difficult",text="Difficult")

        
        self.question['show']='headings'


        self.question.column("Semester",width=55)
        self.question.column("Subject",width=55)
        self.question.column("Questions",width=500)
        self.question.column("weightage",width=55)
        self.question.column("Unit",width=50)
        self.question.column("Difficult",width=55)
        self.question.pack(fill=BOTH,expand=1)
        display()
        self.question.bind("<ButtonRelease-1>",info)

        #==============================================================================================================================================================
        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Insert",bd=4,pady=1,padx=24,width=8,height=2,command=addData).grid(row=0,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,width=8,height=2,command=update).grid(row=2,column=0,padx=1)
        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,width=8,height=2,command=delete).grid(row=3,column=0,padx=1)
        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)
        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
        
        
        

        
        
    
        #==============================================================================================================================================================



    

class Window3:
    def __init__(self,master):
        self.master=master
        self.master.title("Generate Question Paper")
        self.master.geometry('1350x750+0+0')
        self.frame=Frame(self.master)
        self.frame.pack()

        self.entBranch=StringVar()
        self.entSemester=StringVar()
        self.entCourse=StringVar()
        self.entCourseCode=StringVar()
        self.entDifficulty=StringVar()
        self.entMonth=StringVar()
        self.entYear=StringVar()
        
    
    


 #==============================================================================================================================================================
        self.Title=Label(self.frame,text="Generate Paper",font=('arial',45,'bold'),bd=20,)
        self.Title.grid(row=0,column=0,columnspan=2,pady=40)
        
        self.L=Frame(self.frame,width=1010,height=700,bd=20,relief='ridge')
        self.L.grid(row=1,column=0)
        
        self.lblBranch=Label(self.L,font=('arial',12,'bold'),text="Branch",bd=7)
        self.lblBranch.grid(row=0,column=0,sticky=W,padx=5)
        self.entBranch=ttk.Combobox(self.L,font=('arial',12,'bold'),width=43,state='readonly')
        self.entBranch['values']=(' ','Computer Science and Engineering','Civil Engineering','Mechanical Engineering')
        self.entBranch.current(0)
        self.entBranch.grid(row=0,column=1)
        
        self.lblSemester=Label(self.L,font=('arial',12,'bold'),text="Semester",bd=7)
        self.lblSemester.grid(row=1,column=0,sticky=W,padx=5)
        self.entSemester=ttk.Combobox(self.L,font=('arial',12,'bold'),width=43,state='readonly')
        self.entSemester['values']=(' ','I','II','III','IV','V','VI','VII','VIII')
        self.entSemester.current(0)
        self.entSemester.grid(row=1,column=1)
        
        sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
        cur=sqlCon.cursor()
        cur.execute("select distinct(Subject) as Subject from question")
        t=cur.fetchall()
        l=[r for r, in t]
        self.lblCourse=Label(self.L,font=('arial',12,'bold'),text="Course",bd=7)
        self.lblCourse.grid(row=2,column=0,sticky=W,padx=5)
        self.entCourse=ttk.Combobox(self.L,font=('arial',12,'bold'),width=43,state='readonly', values=l)
        self.entCourse.current(0)
        self.entCourse.grid(row=2,column=1)
        
        self.lblCourseCode=Label(self.L,font=('arial',12,'bold'),text="Course Code",bd=7)
        self.lblCourseCode.grid(row=3,column=0,sticky=W,padx=5)
        self.entCourseCode=Entry(self.L,font=('arial',12,'bold'),bd=7,width=44,justify='left')
        self.entCourseCode.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblDifficulty=Label(self.L,font=('arial',12,'bold'),text="Difficulty",bd=7)
        self.lblDifficulty.grid(row=4,column=0,sticky=W,padx=5)
        self.entDifficulty=ttk.Combobox(self.L,font=('arial',12,'bold'),width=43,state='readonly')
        self.entDifficulty['values']=(' ','Easy','Medium','Hard')
        self.entDifficulty.current(0)
        self.entDifficulty.grid(row=4,column=1)
        

        
        self.lblMonth=Label(self.L,font=('arial',12,'bold'),text="Month",bd=7)
        self.lblMonth.grid(row=5,column=0,sticky=W,padx=5)
        self.entMonth=ttk.Combobox(self.L,font=('arial',12,'bold'),width=43,state='readonly')
        self.entMonth['values']=(' ','January','February','March','April','May','June','July','August','September','October','November','December')
        self.entMonth.current(0)
        self.entMonth.grid(row=5,column=1)
        

        self.lblYear=Label(self.L,font=('arial',12,'bold'),text="Year",bd=7)
        self.lblYear.grid(row=6,column=0,sticky=W,padx=5)
        self.entYear=Entry(self.L,font=('arial',12,'bold'),bd=7,width=44,justify='left')
        self.entYear.grid(row=6,column=1,sticky=W,padx=5)


        self.Lo=Frame(self.frame,width=1000,height=200,relief='ridge')
        self.Lo.grid(row=3,column=0,pady=2)
        
        self.btnSubmit=Button(self.Lo,text="Submit",command=self.submit,font=('airal',20,'bold'))
        self.btnSubmit.grid(row=0,column=0,pady=8,padx=22)

        self.btnGenerate=Button(self.Lo,text="Generate",command=self.generate,state=DISABLED,font=('airal',20,'bold'))
        self.btnGenerate.grid(row=0,column=15,pady=8,padx=22)
    

    def submit(self):
        tv1=self.entBranch.get()
        tv2=self.entSemester.get()
        tv3=self.entCourse.get()
        tv4=self.entCourseCode.get()
        tv5=self.entDifficulty.get()
        tv6=self.entMonth.get()
        tv7=self.entYear.get()
        if tv1==self.entBranch.get() and tv2==self.entSemester.get() and tv3==self.entCourse.get() and tv4==self.entCourseCode.get() and tv5==self.entDifficulty.get() and  tv6==self.entMonth.get() and tv7==self.entYear.get():
            self.btnGenerate.config(state = NORMAL)
    def generate(self):
        tv1=self.entBranch.get()
        tv2=self.entSemester.get()
        tv3=self.entCourse.get()
        tv4=self.entCourseCode.get()
        tv5=self.entDifficulty.get()
        tv6=self.entMonth.get()
        tv7=self.entYear.get()
        print("Question Paper Generated")
        print(tv3)
        file=open("user.txt","w")
        file.write("Course Code:" + tv4)
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
        file.write("HTNO:"'\n')
        file.write('\t\t\t\t\t\t\t')
        file.write("SRI VASAVI ENGINEERING COLLEGE(Autonomous"'\n')
        file.write('\t\t\t\t\t\t\t')
        file.write("BTech")
        file.write(tv2)
        file.write("Semester Regular Examination-")
        file.write(tv6)
        file.write("-")
        file.write(tv7 + '\n')
        file.write('\t\t\t\t\t\t\t')
        file.write(tv3 + '\n')
        file.write("Time: 3Hrs"'\n')
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
        file.write("Marks:50M"'\n')
        
        if(tv5=='Easy'):
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-1"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Difficult='1' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()


            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2'  and Difficult='1' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Difficult='1' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-2"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Unit='2' and Difficult='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Difficult='1' and Unit='2' and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Difficult='1' and Unit='2' and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-3"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Unit='3' and Difficult='1' and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Difficult='1' and Unit='3' and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3'  and Difficult='1' and Unit='3'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-4"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Unit='4' and Difficult='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2'  and Difficult='1' and Unit='4'  and Subject=%s order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Difficult='1' and Unit='4'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-5"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1'  and Unit='5' and Difficult='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()
            

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2'  and Difficult='1' and Unit='5'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3'  and Difficult='1' and Unit='5'  and Subject=%s order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            file.close()
            
        elif(tv5=='Medium'):
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-1"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1'  and Difficult='2' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()


            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Difficult='2' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3'  and Difficult='2' and Unit='1'  and Subject=%s order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-2"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s  and Unit='2' and Difficult='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='2' and Unit='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='2' and Unit='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-3"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='3' and Difficult='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='2' and Unit='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='2' and Unit='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-4"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='4' and Difficult='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='2' and Unit='4' order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='2' and Unit='4' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-5"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='5' and Difficult='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()
            

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='2' and Unit='5' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='2' and Unit='5' order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            file.close()
            
        elif(tv5=='Hard'):
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-1"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Difficult='3' and Unit='1' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()


            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='3' and Unit='1' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='3' and Unit='1' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-2"'\n\n')
            cur.execute("select distinct Questions, weightage from question  where weightage='K1' and Subject=%s  and Unit='2' and Difficult='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='2' and Unit='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='3' and Unit='2' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-3"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='3' and Difficult='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='3' and Unit='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='3' and Unit='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-4"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='4' and Difficult='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='3' and Unit='4' order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='3' and Unit='4' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            
            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            file.write('\t\t\t\t\t\t\t')
            file.write("Questions from Unit-5"'\n\n')
            cur.execute("select distinct Questions,weightage from question  where weightage='K1' and Subject=%s and Unit='5' and Difficult='3' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("2m")
                file.write('\n\n')
            sqlCon.close()
           

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K2' and Subject=%s and Difficult='3' and Unit='5' order by  rand() limit 1 ;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("3m")
                file.write('\n\n')
            sqlCon.close()

            sqlCon=mysql.connect(host="localhost",user="root",password="GAYATHRI@2002",database="management")
            cur=sqlCon.cursor()
            cur.execute("select distinct Questions,weightage from question  where weightage='K3' and Subject=%s and Difficult='3' and Unit='5' order by  rand() limit 1;",(tv3,))
            result=cur.fetchall()
            for line in result:
                file.write(" ".join(line))
                file.write('\t')
                file.write("5m")
                file.write('\n\n')
            sqlCon.close()
            file.close()
            
        

         
           
    
        
   
        
        
      
        

        
    
if __name__=='__main__':
    main()
