from tkinter import *
from tkinter import messagebox
import random
top = Tk()
# Code to add widgets will go here...
top.title("Math Quiz")
top.geometry("600x350")

frm1 = Frame(top,height = 20)
frm1.pack()

frm2 = Frame(top,height = 10)
frm2.pack()

frm3 = Frame(top,height = 20)
frm3.pack()

frm4 = Frame(top,height = 40)
frm4.pack()

frm5 = Frame(top,height = 20)
frm5.pack()

frm6 = Frame(top,height = 20)
frm6.pack()

frm7 = Frame(top,height = 20)
frm7.pack()

frm8 = Frame(top,height = 20)
frm8.pack()

frm9 = Frame(top,height = 20)
frm9.pack()

frm10 = Frame(top,height = 20)
frm10.pack()

frm11 = Frame(top,height = 20)
frm11.pack()

def start():
	random1 = int(random.randint(1,100))
	random2 = int(random.randint(1,100))

	randop = int(random.randint(1,4))



	op = ""

	if (str(randop) == "1"):
		op = "+"
	elif (str(randop) == "2"):
		op = "-"
	elif (str(randop) == "3"):
		op = "*"
	elif (str(randop) == "4"):
		op = "/"





def bt():
	global ran1
	ran1 = int(random.randint(1,4))

	if (ran1 == 1):
		op1.config(text = eval(q.cget("text")))
	elif (ran1 == 2):
		op2.config(text = eval(q.cget("text")))
	elif (ran1 == 3):
		op3.config(text = eval(q.cget("text")))
	elif (ran1 == 4):
		op4.config(text = eval(q.cget("text")))


	random3 = int(random.randint(1,1000))
	random4 = int(random.randint(1,1000))
	random5 = int(random.randint(1,1000))

	if (op1.cget("text") == eval(q.cget("text"))):
		op2.config(text = random3)
		op3.config(text = random4)
		op4.config(text = random5)

	elif (op2.cget("text") == eval(q.cget("text"))):
		op1.config(text = random3)
		op3.config(text = random4)
		op4.config(text = random5)

	elif (op3.cget("text") == eval(q.cget("text"))):
		op2.config(text = random3)
		op1.config(text = random4)
		op4.config(text = random5)

	elif (op4.cget("text") == eval(q.cget("text"))):
		op2.config(text = random3)
		op1.config(text = random4)
		op3.config(text = random5)

global list1
list1 = ["+","-","*","/"]
def b1():
	

	if (op1.cget("text") == eval(q.cget("text"))):
		q.config(text = (random.randint(1,1000),random.choice(list1),random.randint(1,1000)))
		bt()
		
	else:
		messagebox.showinfo("Wrong","Wrong answer")

def b2():
	if (op2.cget("text") == eval(q.cget("text"))):
		q.config(text = (random.randint(1,1000),random.choice(list1),random.randint(1,1000)))
		bt()
		
	else:
		messagebox.showinfo("Wrong","Wrong answer")

def b3():
	if (op3.cget("text") == eval(q.cget("text"))):
		q.config(text = (random.randint(1,1000),random.choice(list1),random.randint(1,1000)))
		bt()
		
	else:
		messagebox.showinfo("Wrong","Wrong answer")

def b4():
	if (op4.cget("text") == eval(q.cget("text"))):
		q.config(text = (random.randint(1,1000),random.choice(list1),random.randint(1,1000)))
		bt()
		
	else:
		messagebox.showinfo("Wrong","Wrong answer")

	

random1 = int(random.randint(1,100))
random2 = int(random.randint(1,100))
randop = int(random.randint(1,4))



op = ""

if (str(randop) == "1"):
	op = "+"
elif (str(randop) == "2"):
	op = "-"
elif (str(randop) == "3"):
	op = "*"
elif (str(randop) == "4"):
	op = "/"



q = Label(frm2,text = (random1,op,random2),font = ('Helvetica',20))
q.pack()



op1 = Button(frm4,bg = "white",width = 100,height = 1,bd = 7,font = "bold",command = b1)
op1.pack()

op2 = Button(frm5,bg = "red",width = 100,height = 1,bd = 7,font = "bold",command = b2)
op2.pack()

op3 = Button(frm6,bg = "blue",width = 100,height = 1,bd = 7,font = "bold",command = b3)
op3.pack()

op4 = Button(frm7,bg = "orange",width = 100,height = 1,bd = 7,font = "bold",command = b4)
op4.pack()

global ran
ran = int(random.randint(1,4))

if (ran == 1):
	op1.config(text = eval(q.cget("text")))
elif (ran == 2):
	op2.config(text = eval(q.cget("text")))
elif (ran == 3):
	op3.config(text = eval(q.cget("text")))
elif (ran == 4):
	op4.config(text = eval(q.cget("text")))


random3 = int(random.randint(1,1000))
random4 = int(random.randint(1,1000))
random5 = int(random.randint(1,1000))

if (op1.cget("text") == eval(q.cget("text"))):
	op2.config(text = random3)
	op3.config(text = random4)
	op4.config(text = random5)

elif (op2.cget("text") == eval(q.cget("text"))):
	op1.config(text = random3)
	op3.config(text = random4)
	op4.config(text = random5)

elif (op3.cget("text") == eval(q.cget("text"))):
	op2.config(text = random3)
	op1.config(text = random4)
	op4.config(text = random5)

elif (op4.cget("text") == eval(q.cget("text"))):
	op2.config(text = random3)
	op1.config(text = random4)
	op3.config(text = random5)




top.mainloop()