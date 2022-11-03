from atexit import register
from tkinter import*
from tkinter import messagebox
import cv2
from deepface import DeepFace
from PIL import ImageTk, Image
import db 
class App():
    base=None
    def __init__(self,base):
        self.base=base
        img=PhotoImage(file='logoimg.png')
        Label(base,image=img,bg='white').place(x=50,y=50)
        frame=Frame(base,width=350,height=350,bg="white")
        frame.place(x=480,y=70)
        heading=Label(frame,text='Sign in',fg='#C70039',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        #########
        def on_enter(e):
            self.user.delete(0,'end')
        def on_leave(e):
            name=self.user.get()
            if name =='':
                self.user.insert(0,'Username')
        self.user=Entry(frame,width=25,fg='black',border=0,bg="white",highlightthickness=0,font=('Microsoft YaHei UI Light',11))
        self.user.place(x=34,y=80)
        self.user.insert(0,'Username')
        self.user.bind('<FocusIn>',on_enter)
        self.user.bind('<FocusOut>',on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
        ###########
        def on_enter(e):
            self.code.delete(0,'end')
        def on_leave(e):
            name=self.user.get()
            if name =='':
                self.code.insert(0,'Password')
        self.code=Entry(frame,width=25,fg='black',border=0,bg="white",highlightthickness=0,font=('Microsoft YaHei UI Light',11))
        self.code.place(x=34,y=150)
        self.code.insert(0,'Password')
        self.code.bind('<FocusIn>',on_enter)
        self.code.bind('<FocusOut>',on_leave)
        Frame(frame,width=295,height=2,bg='black').place(x=25,y=182)
        Button(frame,width=34,pady=7,text='Sign in',bg='#C70039',fg='white',border=0,command=self.signin).place(x=25,y=204)
        label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=75,y=270)
        sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',highlightthickness=0,fg='#C70039',command=self.signup)
        sign_up.place(x=215,y=266)
        base.mainloop()
    def signin(self):
        username=self.user.get()
        password=self.code.get()
        get_user=db.search_data(username,password)
        if get_user:
            self.screen=Toplevel(self.base)
            self.screen.title("App")
            self.screen.resizable(False,False)
            self.screen.geometry('925x500+300+200')
            self.screen.config(bg="white")
            # Label(self.screen,text='Hello Everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True) 
            bgimg= PhotoImage(file = "logoimg.png")
            limg= Label(self.screen, i=bgimg,bg="white")
            limg.pack(fill=BOTH, expand=YES)
            Button(self.screen,width=34,pady=7,text='scan',bg='#C70039',fg='white',highlightthickness=0,border=0,command=self.capture_face).place(x=300,y=420)
            self.screen.mainloop()
        else:
            print("errrr")
            messagebox.showerror("invalid","invalid user name or password")
    def signup(self):
        self.screen2=Toplevel(self.base)
        self.screen2.title("Sign up")
        self.screen2.geometry('925x500+300+200')
        self.screen2.config(bg="white")
        self.screen2.resizable(False,False)
        img2=PhotoImage(file='logoimg.png')
        self.screen2.img2=img2
        Label(self.screen2,image=self.screen2.img2,bg='white').place(x=50,y=50)
        frame2=Frame(self.screen2,width=350,height=350,bg="white")
        frame2.place(x=480,y=70)
        heading=Label(frame2,text='Sign up',fg='#C70039',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=100,y=5)
        #########root
        def on_enter(e):
            self.new_user.delete(0,'end')
        def on_leave(e):
            name=self.new_user.get()
            if name =='':
                self.new_user.insert(0,'Username')
        self.new_user=Entry(frame2,width=25,fg='black',border=0,bg="white",highlightthickness=0,font=('Microsoft YaHei UI Light',11))
        self.new_user.place(x=34,y=80)
        self.new_user.insert(0,'Username')
        self.new_user.bind('<FocusIn>',on_enter)
        self.new_user.bind('<FocusOut>',on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25,y=107)
        def on_enter(e):
            self.new_code.delete(0,'end')
        def on_leave(e):
            name=self.new_user.get()
            if name =='':
                self.new_code.insert(0,'Password')
        self.new_code=Entry(frame2,width=25,fg='black',border=0,bg="white",highlightthickness=0,font=('Microsoft YaHei UI Light',11))
        self.new_code.place(x=34,y=150)
        self.new_code.insert(0,'Password')
        self.new_code.bind('<FocusIn>',on_enter)
        self.new_code.bind('<FocusOut>',on_leave)
        Frame(frame2,width=295,height=2,bg='black').place(x=25,y=182)
        Button(frame2,width=34,pady=7,text='Sign in',bg='#C70039',fg='white',border=0,command=self.register).place(x=25,y=204)
    def register(self):
        username=self.new_user.get()
        password=self.new_code.get()
        if username=="" or not username:
            messagebox.showerror("invalid","please enter username")
        elif password=="" or not password:
            messagebox.showerror("invalid","please enter password")
        else :
            if db.validate_data(username): 
                if db.insert_data(username,password):
                    messagebox.showinfo("success","user registerd succcesfully")
                    self.screen2.destroy()
                else:
                    messagebox.showerror("invalid","somthing wrong")
            else:
                messagebox.showerror("invalid","this user name alredy exist")
                
    def capture_face(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        video = cv2.VideoCapture(0)
        dected_imotions=[]
        last_imotion=''
        while True:
            try:
                _, frame = video.read()
                cv2.imshow('video',frame)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
                for x, y, w, h in face:
                    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
                    analyze = DeepFace.analyze(frame,actions=['emotion'])
                    if analyze['dominant_emotion'] not in dected_imotions:
                        dected_imotions.append(analyze['dominant_emotion'])
                    # print(analyze['dominant_emotion'])
                    cv2.putText(frame, analyze['dominant_emotion'], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                    cv2.imshow('video',frame)
                    last_imotion=str(analyze['dominant_emotion'])
                key=cv2.waitKey(0) & 0xFF
                if key==113:
                    break
                else:
                    continue
            except Exception as e:
                # print("no face",e)
                pass
        video.release()
        cv2.destroyAllWindows()
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
render=App(root)