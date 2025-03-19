from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
     self.root = root
     self.root.geometry("1530x790+0+0")
     self.root.title("Student Management System")
     def fetch_data(self):
      print("Data fetched....")
    



     
     #----Variables
     self.var_dep=StringVar()
     self.var_course=StringVar()
     self.var_year=StringVar()
     self.var_semester=StringVar()
     self.var_std_id=IntVar()
     self.var_std_name=StringVar()
     self.var_gender=StringVar()
     self.var_dob=StringVar()
     self.var_email=StringVar()
     self.var_phone=StringVar()
     self.var_div=StringVar()
     self.var_address=StringVar()
     self.var_teacher=StringVar()
    

    # first imag
     img = Image.open(r"E:\Face recognition\UI images\student1.jpeg")
     img = img.resize((500, 130), Image.Resampling.LANCZOS)
     self.photoimg = ImageTk.PhotoImage(img)

     f_lbl=Label(self.root, image=self.photoimg)
     f_lbl.place(x=0, y=0, width=500, height=130)

    # second image
     img1 = Image.open(r"E:\Face recognition\UI images\student2.jpeg")
     img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
     self.photoimg1 = ImageTk.PhotoImage(img1)

     f_lbl = Label(self.root, image=self.photoimg1)
     f_lbl.place(x=500, y=0, width=500, height=130)

# third imag
     img2 = Image.open(r"E:\Face recognition\UI images\student3.jpeg")
     img2 = img2.resize((550, 130), Image.Resampling.LANCZOS)
     self.photoimg2 = ImageTk.PhotoImage(img2)

     f_lbl = Label(self.root, image=self.photoimg2)
     f_lbl.place(x=1000, y=0, width=550, height=130)



     #bg image
     
     img3=Image.open(r"E:\Face recognition\UI images\blank img.jpg")
     img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
     self.photoimg3=ImageTk.PhotoImage(img3)

     bg_img=Label(self.root,image=self.photoimg3)
     bg_img.place(x=0,y=130,width=1530,height=710)

     title_lbl=Label(bg_img,text="STUDENT MANAGEMNET SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
     title_lbl.place(x=0,y=0,width=1530,height=45)
    
    
    
    

     main_frame=Frame(bg_img,bd=2)
     main_frame.place(x=10,y=55,width=1500,height=600)


     # #left label frame

     Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
     Left_frame.place(x=10,y=10,width=730,height=580)


     img_left = Image.open(r"E:\Face recognition\UI images\student3.jpeg")
     img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
     self.photoimg_left = ImageTk.PhotoImage(img_left)

     f_lbl = Label(Left_frame, image=self.photoimg_left)
     f_lbl.place(x=5, y=0, width=720, height=130)

        #current course
     current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("Arial",12,"bold"))
     current_course_frame.place(x=5,y=135,width=720,height=150)

#Department
     dep_label=Label(current_course_frame,text="Department",font=("Arial",12,"bold"),bg="white")
     dep_label.grid(row=0,column=0,padx=10,sticky=W)

     dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Arial",12,"bold"),width=17,state="readonly")
     dep_combo["values"]=("Select Department","BCS","BBS","BIHM") 
     dep_combo.current(0)
     dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#Course

     course_label=Label(current_course_frame,text="Course",font=("Arial",12,"bold"),bg="white")
     course_label.grid(row=0,column=2,padx=10,sticky=W)

     course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Arial",12,"bold"),width=20,state="readonly")
     course_combo["values"]=("Select Course","AI","CS","DS") 
     course_combo.current(0)
     course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#Year

     year_label=Label(current_course_frame,text="Year",font=("Arial",12,"bold"),bg="white")
     year_label.grid(row=1,column=0,padx=10,sticky=W)

     year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Arial",12,"bold"),width=20,state="readonly")
     year_combo["values"]=("Select Year","2022-2025","2023-2026","2024-2027","2025-2028") 
     year_combo.current(0)
     year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)





#Semester

     semester_label=Label(current_course_frame,text="Semester",font=("Arial",12,"bold"),bg="white")
     semester_label.grid(row=1,column=2,padx=10,sticky=W)

     semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Arial",12,"bold"),width=20,state="readonly")
     semester_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th") 
     semester_combo.current(0)
     semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)




  #Class Student Info
     class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Info",font=("Arial",12,"bold"))
     class_student_frame.place(x=5,y=250,width=720,height=300)


#Student id
     studentID_label=Label(class_student_frame,text="STudent_ID:",font=("Arial",12,"bold"),bg="white")
     studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


     studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("Arial",12,"bold"))
     studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

     # studentID = self.var_std_id.get()  # Get input value
     # print(f"Debug: Student_ID before inserting: {studentID}, Type: {type(studentID)}")

     #    # Ensure it's an integer before saving
     # try:
     #        studentID = int(studentID)  # Convert to integer if possible
     # except ValueError:
     #        print("Invalid Student ID: Must be a number!")

     

#Student name
     studentName_label=Label(class_student_frame,text="STudent_Name:",font=("Arial",12,"bold"),bg="white")
     studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

     studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("Arial",12,"bold"))
     studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

#class division
 
     class_div_label=Label(class_student_frame,text="CLass_division:",font=("Arial",12,"bold"),bg="white")
     class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

     class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("Arial",12,"bold"))
     class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

#Email

     email_label=Label(class_student_frame,text="EMail:",font=("Arial",12,"bold"),bg="white")
     email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

     email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Arial",12,"bold"))
     email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#Address
     address_label=Label(class_student_frame,text="Address:",font=("Arial",12,"bold"),bg="white")
     address_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
 
     address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Arial",12,"bold"))
     address_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

     


#Teacher name

     teacher_label=Label(class_student_frame,text="Teacher_NAme:",font=("Arial",12,"bold"),bg="white")
     teacher_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

     teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Arial",12,"bold"))
     teacher_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#Gender

     gender_label=Label(class_student_frame,text="Gender:",font=("Arial",12,"bold"),bg="white")
     gender_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

     gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("Arial",12,"bold"))
     gender_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

     
#DOB
     
     dob_label=Label(class_student_frame,text="DOB:",font=("Arial",12,"bold"),bg="white")
     dob_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
   
     dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Arial",12,"bold"))
     dob_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

     
     
     #Radio buttons
     self.var_radio1=StringVar()
     Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
     Radiobutton1.grid(row=4,column=0)

     
     Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text=" No Photo Sample",value="No")
     Radiobutton2.grid(row=4,column=1)

     #button frame
     button_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
     button_frame.place(x=0,y=160,width=715,height=75)

     save_button=Button(button_frame,text="Save",command=self.add_data,width=17,font=("Arial",12,"bold"),bg="white",fg="blue")
     save_button.grid(row=0,column=0)

     update_button=Button(button_frame,text="Update",width=17,font=("Arial",12,"bold"),bg="white",fg="blue")
     update_button.grid(row=0,column=1)

     delete_button=Button(button_frame,text="Delete",width=17,font=("Arial",12,"bold"),bg="white",fg="blue") #inside write command=self.delete_data
     delete_button.grid(row=0,column=2)

     reset_button=Button(button_frame,text="Reset",width=17,font=("Arial",12,"bold"),bg="white",fg="blue")
     reset_button.grid(row=0,column=3)

     button_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
     button_frame1.place(x=0,y=235,width=715,height=115)


     take_photo_button=Button(button_frame1,command=self.generate_dataset,text="Take photo sample",width=35,font=("Arial",12,"bold"),bg="white",fg="blue")
     take_photo_button.grid(row=0,column=0)

     update_photo_button=Button(button_frame1,text="Update photo sample",width=35,font=("Arial",12,"bold"),bg="white",fg="blue")
     update_photo_button.grid(row=0,column=1)




     #right label frame

     Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Arial",12,"bold"))
     Right_frame.place(x=750,y=10,width=720,height=580)

     
     img_right = Image.open(r"E:\Face recognition\UI images\student3.jpeg")
     img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
     self.photoimg_right = ImageTk.PhotoImage(img_right)

     f_lbl = Label(Right_frame, image=self.photoimg_right)
     f_lbl.place(x=5, y=0, width=720, height=130)


     #--------- Searching------------
     Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("Arial",12,"bold"))
     Search_frame.place(x=5,y=135,width=710,height=70)

     search_label=Label(Search_frame,bg="white",text="Search BY:",font=("Arial",12,"bold"))
     search_label.grid(row=0,column=0,pady=5,sticky=W)




     search_combo=ttk.Combobox(Search_frame,font=("Arial",12,"bold"),width=15,state="readonly")
     search_combo["values"]=("Select","StudentID","Email") 
     search_combo.current(0)
     search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

     search_entry=ttk.Entry(Search_frame,width=15,font=("Arial",12,"bold"))
     search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


     search_button=Button(Search_frame,text="Search",width=12,font=("Arial",12,"bold"),bg="white",fg="blue")
     search_button.grid(row=0,column=3,padx=4)

     ShowALL_button=Button(Search_frame,text="Show all",width=12,font=("Arial",12,"bold"),bg="white",fg="blue")
     ShowALL_button.grid(row=0,column=4,padx=4)

#-----------Table Frame-
     table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
     table_frame.place(x=5,y=210,width=710,height=350)


     scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
     scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

     self.student_table=ttk.Treeview(table_frame,columns=("department","course","year","sem","id","name","gender","dob","email","div","address","teacher","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y.set)

     scroll_x.pack(side=BOTTOM,fill=X)
     scroll_y.pack(side=RIGHT,fill=Y)
     scroll_x.config(command=self.student_table.xview)
     scroll_y.config(command=self.student_table.yview)


     self.student_table.heading("department",text="Department")
     self.student_table.heading("course",text="Course")
     self.student_table.heading("year",text="Year")
     self.student_table.heading("sem",text="Semester")
     self.student_table.heading("id",text="StudentID")
     self.student_table.heading("name",text="Name")
     self.student_table.heading("gender",text="Gender")
     self.student_table.heading("dob",text="DOB")
     self.student_table.heading("email",text="Email")
     self.student_table.heading("div",text="Division")
     self.student_table.heading("address",text="Address") 
     self.student_table.heading("teacher",text="Teacher")
     self.student_table.heading("photo",text="PhotoSampleStatus")
     self.student_table["show"]="headings"
     
     self.student_table.column("department",width=100)
     self.student_table.column("course",width=100)
     self.student_table.column("year",width=100)
     self.student_table.column("sem",width=100)
     self.student_table.column("id",width=100)
     self.student_table.column("name",width=100)
     self.student_table.column("gender",width=100)
     self.student_table.column("dob",width=100)
     self.student_table.column("email",width=100)
     self.student_table.column("div",width=100)
     self.student_table.column("address",width=100)
     self.student_table.column("teacher",width=100)
     self.student_table.column("photo",width=100)

     self.student_table.pack(fill=BOTH,expand=1)
     self.student_table.bind("<ButtonRelease>",self.get_cursor)
     #self.fetch_data()

     

     
#-----FUnction declaration
     
    def add_data(self):
     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
     else:
          try:
              conn=mysql.connector.connect(host="localhost",username="root",password="pizza#9766958202",database="face_recognizer")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      self.var_dep.get(),
                                                                                      self.var_course.get(),
                                                                                      self.var_year.get(),
                                                                                      self.var_semester.get(),
                                                                                      self.var_std_id.get(),
                                                                                      self.var_std_name.get(),
                                                                                      self.var_div.get(),
                                                                                      self.var_gender.get(),
                                                                                      self.var_dob.get(),
                                                                                      self.var_email.get(),
                                                            
                                                                                      self.var_address.get(),
                                                                                      self.var_teacher.get(),
                                                                                      self.var_radio1.get()


                                                                                    ))
        
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
          except Exception as es:
             messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
          
        


     #      #-------fetch data
     #      self.fetch_data()
     # def fetch_data(self):
       
     #    try:
     #        conn = mysql.connector.connect(
     #            host="localhost", 
     #            username="root", 
     #            password="pizza#9766958202", 
     #            database="face_recognizer"
     #        )
     #        my_cursor = conn.cursor()
     #        my_cursor.execute("SELECT * FROM student")
     #        rows = my_cursor.fetchall()

     #        if len(rows) != 0:
     #            self.student_table.delete(*self.student_table.get_children())
     #            for row in rows:
     #                self.student_table.insert("", END, values=row)
                
     #        conn.commit()
     #        conn.close()
     #    except Exception as e:
     #        print(f"Error fetching data: {e}")


  #-------get cursor
     # def get_cursor(self,event):
     #    cursor_focus=self.student_table.focus()
     #    content=self.student_table.item(cursor_focus)
     #    data=content["values"]


     #    self.var_dep.set(data[0]),
     #    self.var_course.set(data[1]),
     #    self.var_year.set(data[2]),
     #    self.var_semester.set(data[3]),
     #    self.var_std_id.set(data[4]),
     #    self.var_std_name.set(data[5]),
     #    self.var_div.set(data[6]),
     #    self.var_gender.set(data[7]),
     #    self.var_dob.set(data[8]),
     #    self.var_email.set(data[9]),
     #    self.var_address.set(data[10]),
     #    self.var_teacher.set(data[11]),
     #    self.usertype.set(data[12]),
     #    self.var_radio1.set(data[0]),

     #update function

#      def update_data(self):
#          if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
#           messagebox.showerror("Error","All fields are required",parent=self.root)
#          else:
#           try:
#                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
#                if Update>0:
#                   conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
#                   my_cursor=conn.cursor()
#                   my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                              
#                                                                                                                                                       self.var_dep.get(),
#                                                                                                                                                       self.var_course.get(),
#                                                                                                                                                       self.var_year.get(),
#                                                                                                                                                       self.var_semester.get(),
#                                                                                                                                                       self.var_std_name.get(),
#                                                                                                                                                       self.var_div.get(),
#                                                                                                                                                       self.var_gender.get(),
#                                                                                                                                                       self.var_dob.get(),
#                                                                                                                                                       self.var_email.get(),
#                                                                                                                                                       self.var_address.get(),
#                                                                                                                                                       self.var_teacher.get(),
#                                                                                                                                                       self.var_radio1.get(),
#                                                                                                                                                       self.var_std_id.get(),

#                                                                                                                                                  ))
               

#                else:
#                   if not Update:
#                      return
#                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
#                conn.commit()
#                #self.fetch_data()
#                conn.close()                                                                                                                                 
#           except Exception as es:
#              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
 
#  #-------------- delete function
#      def delete_data(self):
#         if self.var_std_id.get()=="":
#            messagebox.showerror("Error","Student is must be required",parent=self.root)
#         else:
#           try:
#              delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
#              if delete>0:
#                  conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="face_recognizer")
#                  my_cursor=conn.cursor()
#                  sql="delete from student where Student_id=%s"
#                  val=(self.var_std_id.get(),)
#                  my_cursor.execute(sql,val)
#              else:
#                 if not delete:
#                    return
                   
#              conn.commit()
#              #self.fetch_data()
#              conn.close()
#              messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
#           except Exception as es:
#              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

  #reset function
    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_semester.set("Select Semester")
       self.var_std_id.set("")
       self.var_std_name.set("")
       self.var_div.set("")
       self.var_gender.set("")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_address.set("")
       self.var_teacher.set("")
       self.var_radio1.set("")

#==========Generate data set or Take photo Samples

def generate_dataset(self):
    if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
    else:
          try:
               Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
               if Update>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="pizza#9766958202",database="face_recognizer")
                  my_cursor=conn.cursor()
                  my_cursor.execute("select * from student")
                  myresult=my_cursor.fetchall()
                  id=0
                  for x in myresult:
                   id+1  
                  my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                              
                                                                                                                                                      self.var_dep.get(),
                                                                                                                                                      self.var_course.get(),
                                                                                                                                                      self.var_year.get(),
                                                                                                                                                      self.var_semester.get(),
                                                                                                                                                      self.var_std_name.get(),
                                                                                                                                                      self.var_div.get(),
                                                                                                                                                      self.var_gender.get(),
                                                                                                                                                      self.var_dob.get(),
                                                                                                                                                      self.var_email.get(),
                                                                                                                                                      self.var_address.get(),
                                                                                                                                                      self.var_teacher.get(),
                                                                                                                                                      self.var_radio1.get(),
                                                                                                                                                      self.var_std_id.get()==id+1

                                                                                                                                                 ))
                  conn.commit()
                  #self.fetch_data()
                  self.reset_data()
                  conn.close()
          except Exception as es:
             print(f"Error",f"Due To:{str(es)}",parent=self.root)     


 #===========Load predefined data on facefrontals from opencv
          face_classifier=cv2.CascadeClassifier("Haarcascade_frontalface_default.xml")
               
          def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLORBGR2GRAY)
                  faces=face_classifier.detectMultiScale(gray,1.3,5)
                  #scaling factor=1.3
                  #Minimum Neighbour=5

                  for(x,y,w,h) in faces:
                     face_cropped=img[y:y+h,x:x+w]
                     return face_cropped
          cap=cv2.VideoCapture(0)
          img_id=0
          while True:
                  ret,my_frame=cap.read()
                  if face_cropped(my_frame) is not None:
                     img_id+=1
                     face=cv2.resize(face_cropped(my_frame),(450,450))
                     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                     file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                     cv2.imrite(file_name_path,face)
                     cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                     cv2.imshow("Cropped Face",face)

                  if cv2.waitKey(1)==13 or int(img_id)==100:
                     break
          cap.release()
          cv2.destroyAllWindows()
          messagebox.showinfo("Result","Generating datas completed successfully")


                     





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
