from tkinter import*
from module import*
from tkinter.messagebox import*
from tkinter.ttk import*
userr=loe_failist_listisse("users.txt")
passww=loe_failist_listisse("passwords.txt")
log=Tk()
log.geometry("300x100")
log.title("Авторизация")
def sps():
    global reg
    global login2
    global psw2
    global passww
    global userr
    user=login2.get()
    passw=psw2.get()
    #
    userr.append(user)
    passww.append(passw)
    #
    userr=open("users.txt","a")
    userr.write(user)
    userr.close()
    #
    passww=open("passwords.txt","a")
    passww.write(passw)
    passww.close()
    #
    showinfo(title="OK",message="Пароль принят и добавлен в базу данных!")  
def append():
    global reg
    global login2
    global psw2
    global passww
    global userr
    Label(text="Придумайте\nЛогин:").grid(row=0,column=0)
    login2=Entry(width=30)
    login2.grid(row=0,column=1,columnspan=3)
    Label(text="Придумайте\nПароль:").grid(row=1,column=0)
    psw2=Entry(width=30)
    psw2.grid(row=1,column=1,columnspan=3)
    Button(text="Выход",command=Exit2).grid(row=2,column=1)
    Button(text="Подтвердить",command=sps).grid(row=2,column=3)
    userr.append(login2.get())
    passww.append(psw2.get())  
def Reg():
    log.destroy()
    reg=Tk()
    reg.geometry("300x100")
    reg.title("Регистрация")
    Label(text="Придумайте\nЛогин:").grid(row=0,column=0)
    login1=Entry(width=30)
    login1.grid(row=0,column=1,columnspan=3)
    Label(text="Придумайте\nПароль:").grid(row=1,column=0)
    psw1=Entry(width=30)
    psw1.grid(row=1,column=1,columnspan=3)
    Button(text="Выход",command=Exit2).grid(row=2,column=1)
    Button(text="Подтвердить",command=append).grid(row=2,column=3)
    
def Login():
    user=login.get()
    passw=psw.get()
    if (user not in userr) or (passw not in passww):
        showerror(title="Error",message="Пароль или логин неверен!")
        if askyesno(title="",message="Желаете ли вы зарегистрироваться?")==True:
            Reg()
    else:
        showinfo(title="OK",message="Добро пожаловать!")

def Exit2():
    if askyesno("Выход","Выйти?"):
         reg.destroy()
def Exit():
    if askyesno("Выход","Выйти?"):
        log.destroy()
def loe_failist(file:str)->str:
	f=open(file,"r")
	stroka=f.read()#str
	stroka=f.readlines()#list
	f.close()
	return stroka
def loe_failist_listisse(file:str)->list:
	f=open(file,"r")
	list_=[]
	for stroka in f:
		list_.append(stroka.strip())
	f.close()
	return list_
Label(text="Логин:").grid(row=0,column=0)
login=Entry(width=30)
login.grid(row=0,column=1,columnspan=3)
Label(text="Пароль:").grid(row=1,column=0)
psw=Entry(width=30)
psw.grid(row=1,column=1,columnspan=3)
Button(text="Регистрация",command=Reg).grid(row=2,column=0)
Button(text="Выход",command=Exit).grid(row=2,column=2)
Button(text="Вход",command=Login).grid(row=2,column=3)



log.mainloop()
