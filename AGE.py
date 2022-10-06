import tkinter
import datetime
def calc(b,c,f,dayss):
    if c>=0:
            if f>=0:
                pass
            elif c!=0:
                    c=c-1
                    f=dayss+f
    else:
            b=b-1
            c=12+c
            if f>=0:
                pass
            elif c!=0:
                c=c-1
                f=dayss+f
    
    if f==dayss:
        c+=1
        f=0
    if c==12:
        b+=1
        c=0
    return b,c,f
def calc1(Month,Day,Year):
    dayss=0
    if Month in [1,3,5,7,8,10,12]:
        dayss=31
    elif Month in[4,6,9,11]:
        dayss=30
    elif Month==2:
        if (Year%4==0 and Year%100!=0)or Year%400==0:
            dayss=29
        else:
            dayss=28
    if Day<=dayss and Month<=12:
        return dayss,True
    else:
        return dayss,False

window=tkinter.Tk()
window.configure(background="skyblue")
window.geometry("365x400")
window.resizable(0,0)
label1=tkinter.Label(window,borderwidth=50)
window.title("AGE_CALCULATOR")
icon=tkinter.PhotoImage(file="age2.png")
label=tkinter.Label(window,image=icon)
label.grid(columnspan=2,row=1)
Name=tkinter.Label(text="NAME",font=("Copperplate Gothic Bold",12)).grid(column=0,row=4)
Year=tkinter.Label(text="YEAR OF BIRTH",font=("Copperplate Gothic Bold",12)).grid(column=0,row=5)
Month=tkinter.Label(text="MONTH OF BIRTH",font=("Copperplate Gothic Bold",12)).grid(column=0,row=6)
Day=tkinter.Label(text="DAY OF BIRTH",font=("Copperplate Gothic Bold",12)).grid(column=0,row=7)
NameEntry=tkinter.Entry(width=30)
NameEntry.grid(column=1,row=4)
YearEntry=tkinter.Entry(width=30)
YearEntry.grid(column=1,row=5)
MonthEntry=tkinter.Entry(width=30)
MonthEntry.grid(column=1,row=6)
DayEntry=tkinter.Entry(width=30)
DayEntry.grid(column=1,row=7)
def clicked():
    try:
        Name=NameEntry.get()
        Year=int(YearEntry.get())
        Month=int(MonthEntry.get())
        Day=int(DayEntry.get())
    except:
        textArea=tkinter.Text(window,height=3,width=30,font=("Copperplate Gothic Bold",12))
        textArea.grid(columnspan=2,row=9)
        textArea.insert(tkinter.END,"Insufficient/Invalid Inputs")
    else:
        present=datetime.date.today()
        b=present.year-Year
        c=present.month-Month
        f=present.day-Day
        dayss,boolv=calc1(Month,Day,Year)
        if b>=0 and boolv:
            b,c,f=calc(b,c,f,dayss)
            if b>=0:
                b=str(b)+"Year(s)"
                c=str(c)+"Month(s)"
                f=str(f)+"Day(s)"
                age="{x} your age is {y},{m},{d}".format(x=Name,y=b,m=c,d= f)
            else:
                age="Date out of range"
        else:
            if not boolv:
                age="Invalid date"
            else:
                age="Date out of range"
        textArea=tkinter.Text(window,height=3,width=30,font=("Copperplate Gothic Bold",12))
        textArea.grid(columnspan=2,row=9)
        textArea.insert(tkinter.END,age)
button=tkinter.Button(window,text="CALCULATE AGE",command=clicked,fg="blue",bg="pink",font=("Copperplate Gothic Bold",12)).grid(columnspan=2, row=8)   
window.mainloop()
