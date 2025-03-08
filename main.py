from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student


class Face_Recognition_System:
   def __init__(self,root):
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face Recognition For Attendance")
    

    #bg image
    img=Image.open(r"E:\Face recognition\UI images\blank img.jpg")
    img=img.resize((1920,1080),Image.Resampling.LANCZOS)
    self.photoimg=ImageTk.PhotoImage(img)
    
    bg_img=Label(self.root,image=self.photoimg)
    bg_img.place(x=0,y=0,width=1920,height=1080)
    
    
    title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Arial",12,"bold"))#,bg="white",fg="blue")
    title_lbl.place(x=0,y=0,width=400,height=200)


    #student button

    b1_1=Button(text="Student details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b1_1.place(x=200,y=300,width=220,height=40)


     #Detect face button

    b2_2=Button(text="Face Detection",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b2_2.place(x=500,y=300,width=220,height=40)


     #Attendance button

    b3_3=Button(text="Attendance",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b3_3.place(x=800,y=300,width=220,height=40)


     #Help Desk button

    b4_4=Button(text="Help Desk",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b4_4.place(x=1100,y=300,width=220,height=40)


    #Help Desk button

    b5_5=Button(text="Train data",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b5_5.place(x=200,y=580,width=220,height=40)


    #Images button

    b6_6=Button(text="Images",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b6_6.place(x=500,y=580,width=220,height=40)

    #...... button

    b7_7=Button(text=".....",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b7_7.place(x=800,y=580,width=220,height=40)

    #Exit button

    b8_8=Button(text="Exit",cursor="hand2", font=("times new roman",15,"bold"),bg="white",fg="blue")
    b8_8.place(x=1100,y=580,width=220,height=40)


    #-----Function buttons-----

   def student_details(self):
     self.new_window=Toplevel(self.root)
     self.app=Student(self.new_window)


    

   







 







if __name__=="__main__":
  root=Tk()
  obj=Face_Recognition_System(root)
  root.mainloop()





  

    