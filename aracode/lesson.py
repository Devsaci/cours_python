# -----------------------Start---------------------------#
# تعلم لغة البرمجة بايثون :
# تعلم الاساسيات وتحويلها بشكل مباشر لواجهة وتحويلها لتطبيق تنفيذي exe
# https://www.youtube.com/watch?v=AtgN44i4WZE&t=215s

# https://docs.python.org/fr/3/library/tkinter.html#a-hello-world-program

from tkinter import *
pro = Tk()
pro.geometry('300x400')
pro.title('Name-age : Program')
title = Label(
    pro,
    text='Name & age Program',
    bg='red',
    fg=('white'),
    font=('tajawal', 17, 'bold'),
).pack(fill=X)
L1 = Label(
    pro,
    text='Enter Your Name'
).pack()

pro.mainloop()

#  python -m tkinter
# Version : Tcl/Tk 8.6
