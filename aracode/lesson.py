# -----------------------Start---------------------------#
# تعلم لغة البرمجة بايثون :
# تعلم الاساسيات وتحويلها بشكل مباشر لواجهة وتحويلها لتطبيق تنفيذي exe
# https://www.youtube.com/watch?v=AtgN44i4WZE&t=215s

# https://docs.python.org/fr/3/library/tkinter.html#a-hello-world-program

from tkinter import *
pro = Tk()
pro.geometry('400x400')

############## Name-age : Program  ##################
pro.title('Name-age : Program')
title = Label(
    pro,
    text='Name & age Program',
    bg='red',
    fg=('white'),
    font=('tajawal', 17, 'bold'),
).pack(fill=X)

##############  Enter Your Name  ##################
L1 = Label(
    pro,
    text='Enter Your Name',
    font=('tajawal', 17, 'bold'),
).pack()
inputName = Entry(
    pro,
    width=35,
    font=('tajawal', 12, 'bold'),
    justify='center'
).pack()


############## Enter Your Age ##################

L1 = Label(
    pro,
    text='Enter Your Age',
    font=('tajawal', 17, 'bold'),
).pack()
inputName = Entry(
    pro,
    width=35,
    font=('tajawal', 12, 'bold'),
    justify='center'
).pack()

############## Button Print ##################
buttonprint = Button(
    pro,

).pack()


pro.mainloop()

#  python -m tkinter
# Version : Tcl/Tk 8.6
