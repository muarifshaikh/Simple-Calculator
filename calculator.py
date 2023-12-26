from tkinter import*
from PIL import Image, ImageTk

class calc:
	def getandreplace(self):
		self.expression=self.e.get()
		self.newtext=self.expression.replace('÷', '/').replace('×', '*')
	def equals(self):
		self.getandreplace()
		try:
			self.value=eval(self.newtext)
		except Exception as r:
			self.e.delete(0, END)
		else:
			self.e.delete(0, END)
			self.e.insert(0, self.value)
	def clearall(self):
		self.e.delete(0, END)
	def clear1(self):
		self.text=self.e.get()[:-1]
		self.e.delete(0, END)
		self.e.insert(0, self.text)
	def action(self, arg):
		self.e.insert(END, arg)
	def __init__(self, master):
		master.title('Calculator')
		master.geometry("420x500")
		master.resizable(0, 0)
		f1 = Frame(master, relief=RIDGE, bd=5)
		f1.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.e=Entry(f1, bd=3, font=('arial', 25), bg="lightyellow", relief=RIDGE)
		self.e.place(relx=0, rely=0, relwidth=1, relheight=0.15)

		img1 = Image.open("Images/backbtn.png")
		img2=img1.resize((40, 40))
		img3=ImageTk.PhotoImage(img2)
		
		Button(f1, text="C", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.clearall()).place(relx=0, rely=0.15, relheight=0.15, relwidth=0.25)
		clrb = Button(f1, image=img3, bg="gold", bd=3, command=lambda:self.clear1())
		clrb.image=img3
		clrb.place(relx=0.25, rely=0.15, relheight=0.15, relwidth=0.25)

		Button(f1, text="7", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('7')).place(relx=0, rely=0.3, relheight=0.15, relwidth=0.25)
		Button(f1, text="8", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('8')).place(relx=0.25, rely=0.3, relheight=0.15, relwidth=0.25)
		Button(f1, text="9", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('9')).place(relx=0.5, rely=0.3, relheight=0.15, relwidth=0.25)

		Button(f1, text="4", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('4')).place(relx=0, rely=0.45, relheight=0.15, relwidth=0.25)
		Button(f1, text="5", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('5')).place(relx=0.25, rely=0.45, relheight=0.15, relwidth=0.25)
		Button(f1, text="6", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('6')).place(relx=0.5, rely=0.45, relheight=0.15, relwidth=0.25)
		
		Button(f1, text="1", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('1')).place(relx=0, rely=0.6, relheight=0.15, relwidth=0.25)
		Button(f1, text="2", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('2')).place(relx=0.25, rely=0.6, relheight=0.15, relwidth=0.25)
		Button(f1, text="3", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('3')).place(relx=0.5, rely=0.6, relheight=0.15, relwidth=0.25)
		
		Button(f1, text="+", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('+')).place(relx=0.75, rely=0.15, relheight=0.15, relwidth=0.25)
		Button(f1, text="-", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('-')).place(relx=0.75, rely=0.3, relheight=0.15, relwidth=0.25)
		Button(f1, text="×", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('×')).place(relx=0.75, rely=0.45, relheight=0.15, relwidth=0.25)
		Button(f1, text="/", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('÷')).place(relx=0.75, rely=0.6, relheight=0.15, relwidth=0.25)
		Button(f1, text="=", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.equals()).place(relx=0.75, rely=0.75, relheight=0.15, relwidth=0.25)
		Button(f1, text=".", font=('arial', 20, 'bold'), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('.')).place(relx=0.5, rely=0.75, relheight=0.15, relwidth=0.25)
		Button(f1, text="0", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action('0')).place(relx=0.5, rely=0.15, relheight=0.15, relwidth=0.25)

		Button(f1, text="(", fg="#0062B0", font=('arial', 20), bg="gold", bd=3, command=lambda:self.action('(')).place(relx=0, rely=0.75, relheight=0.15, relwidth=0.25)
		Button(f1, text=")", font=('arial', 20), fg="#0062B0", bg="gold", bd=3, command=lambda:self.action(')')).place(relx=0.25, rely=0.75, relheight=0.15, relwidth=0.25)
		
		Label(f1, text="DEVELOPED BY MUARIF SHAIKH", fg="#0062B0", bg='lightyellow', font=('courier', 15)).place(rely=0.9, relwidth=1, relheight=0.1)
root=Tk()
obj=calc(root)
root.mainloop()

