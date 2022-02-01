# This Python file uses the following encoding: utf-8
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import json
import os


# APP VARIABLES
app_version = '1.0.0'

class ThemeColors:
	# Colors for themes
	dark_bg = '#282923'
	dark_fg = '#F8F8F2'

	light_bg = '#eff0eb'
	light_fg = 'black'

class ClassFile:
	file_open = None
	file = None
	file_extension = 'Good classes'

colors = ThemeColors()
edit_file = ClassFile()



# METHODS
def LoadPreferences():
	with open('preferences.json', 'r', encoding='utf-8') as f:
		PrefJson = json.load(f)

	theme = PrefJson['View']['theme']
	font = PrefJson['View']['font']
	font_size = PrefJson['View']['font-size']
	insertwidth = PrefJson['View']['insertwidth']
	word_wrap = PrefJson['Editor']['word-wrap']

	if theme == "Dark Classic":
		text_editor.configure(bg=f'{colors.dark_bg}', fg=f'{colors.dark_fg}', insertbackground="white", font=(f'{font}', font_size), insertwidth=insertwidth)
	elif theme == "Light":
		text_editor.configure(bg=f'{colors.light_bg}', fg=f'{colors.light_fg}', insertbackground="black", font=(f'{font}', font_size), insertwidth=insertwidth)
	else:
		messagebox.showwarning("Ошибка настроек", "Не удалось загрузить некоторые настройки из preferences.json.")

	if word_wrap == "True" or word_wrap == "true":
		text_editor.configure(wrap="word")
		wordwrap = True
	else:
		text_editor.configure(wrap=NONE)
		wordwrap = False

def LoadSession():
	with open('session.json', 'r', encoding='utf-8') as f:
		SessionJson = json.load(f)

	try:
		if SessionJson['file'] == "None":
			return

		else:
			root.title(os.path.basename(str(SessionJson['file'])) + " - New Editor")
			edit_file.file = open(SessionJson['file'], "r")
			text_editor.insert(1.0, edit_file.file.read())
			edit_file.file.close()
			file = str(SessionJson['file'])
			filename, file_extension = os.path.splitext(f'{file}')

			if file_extension == '.txt':
				file_extension = 'Text File'

			elif file_extension == '.py' or file_extension == '.pyo' or file_extension == '.pyw':
				file_extension = 'Python'

			elif file_extension == '.cpp' or file_extension == '.c++' or file_extension == '.cc'  or file_extension == '.hpp':
				file_extension = 'C++'

			elif file_extension == '.c':
				file_extension = 'C'

			elif file_extension == '.java' or file_extension == '.class' or file_extension == '.jar'  or file_extension == '.jad'  or file_extension == '.jmod':
				file_extension = 'Java'

			else:
				exit_extension = file_extension.replace('.', '', 1) # Cute .
				edit_file.file_extensionl = exit_extension.upper() # Upper for CAPS LOCK

		bottomlabel.configure(text=f"Line 1     Symbols 0       {file_extension}  ")
		#return file_extension

	except FileNotFoundError:
		root.title("File is not found")
	
def MouseResizeFont(event):
	root.bind("<MouseWheel>", lambda event: "break")
	if event.num == 4 or event.delta == 120:
		with open('preferences.json', 'r', encoding='utf-8') as f:
			PrefJson = json.load(f)
		Font = PrefJson['View']["font"]
		FontSize = int(PrefJson['View']["font-size"])
		PrefJson['View']["font-size"] += 1
		if PrefJson['View']["font-size"] == 85:
			return
		with open('preferences.json', 'w') as f:
			json.dump(PrefJson ,f)
		text_editor.configure(font = (f'{str(Font)}', FontSize))

	else:
		with open('preferences.json', 'r', encoding='utf-8') as f:
			PrefJson = json.load(f)
		Font = PrefJson['View']["font"]
		FontSize = int(PrefJson['View']["font-size"])
		PrefJson['View']["font-size"] -= 1
		if PrefJson['View']["font-size"] == 5:
			return
		with open('preferences.json', 'w') as f:	
			json.dump(PrefJson ,f)
		text_editor.configure(font = (f'{str(Font)}', FontSize))

def check_file_extension(*args):
	filename, file_extension = os.path.splitext(f'{edit_file.file_open}')
	if file_extension == '.txt':
		edit_file.file_extensionl = 'Text File'
		bottomlabel.configure(text=f"Line 1     Symbols 0       Text  ")

	elif file_extension == '.py' or file_extension == '.pyo' or file_extension == '.pyw':
		edit_file.file_extensionl = 'Python'
		bottomlabel.configure(text=f"Line 1     Symbols 0       Python  ")

	elif file_extension == '.cpp' or file_extension == '.c++' or file_extension == '.cc'  or file_extension == '.hpp'  or file_extension == '.c':
		edit_file.file_extensionl = 'C++'
		bottomlabel.configure(text=f"Line 1     Symbols 0       C++  ")

	elif file_extension == '.java' or file_extension == '.class' or file_extension == '.jar'  or file_extension == '.jad'  or file_extension == '.jmod':
		edit_file.file_extensionl = 'Java'
		bottomlabel.configure(text=f"Line 1     Symbols 0       Java  ")

	elif file_extension == '.html':
		edit_file.file_extensionl = 'HTML'
		bottomlabel.configure(text=f"Line 1     Symbols 0       HTML  ")

	elif file_extension == '.css':
		edit_file.file_extensionl = 'CSS'
		bottomlabel.configure(text=f"Line 1     Symbols 0       CSS  ")

	elif file_extension == '.php':
		edit_file.file_extensionl = 'PHP'
		bottomlabel.configure(text=f"Line 1     Symbols 0       PHP  ")

	elif file_extension == '.xml':
		edit_file.file_extensionl = 'XML'
		bottomlabel.configure(text=f"Line 1     Symbols 0       XML  ")

	else:
		exit_extension = file_extension.replace('.', '', 1) # Cute .
		edit_file.file_extensionl = exit_extension.upper() # Upper for CAPS LOCK
		bottomlabel.configure(text=f"Line 1     Symbols 0       {edit_file.file_extensionl}  ")


# ALSO METHODS
def open_file(*args):
	with open('session.json', 'r', encoding='utf-8') as f:
		SessionJson = json.load(f)

	edit_file.file_open = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])

	if edit_file.file_open is not None and edit_file.file_open != '':
		root.title(os.path.basename(edit_file.file_open) + " - New Editor")

		text_editor.delete(1.0, END)
		edit_file.file = open(edit_file.file_open, "r")
		text_editor.insert(1.0, edit_file.file.read())
		edit_file.file.close()
		check_file_extension()
		# Load a last file to Json
		SessionJson['file'] = str(edit_file.file_open)
		with open('.session.json','w') as f:
			json.dump(SessionJson ,f)

def save_file_as(*args):
	edit_file.file_open = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])

	edit_file.file = open(edit_file.file_open, "w")
	edit_file.file.write(text_editor.get(1.0, END))
	edit_file.file.close()
	root.title(os.path.basename(edit_file.file_open) + " - New Editor")
	check_file_extension()
	# Load a last file to Json
	with open('session.json', 'r', encoding='utf-8') as f:
		SessionJson = json.load(f)
	SessionJson['file'] = str(edit_file.file_open)
	with open('session.json','w') as f:
		json.dump(SessionJson ,f)


def save_file(*args):
	if edit_file.file_open is None or edit_file.file_open == '' and edit_file.file is None or edit_file.file == '':
		save_file_as()

	elif edit_file.file_open != None and edit_file.file != None:
		edit_file.file = open(edit_file.file_open, "w")
		edit_file.file.write(text_editor.get(1.0, END))
		edit_file.file.close()


def new_file(*args):
	root.title("Untitled - New Editor")
	text_editor.delete(1.0, END)
	edit_file.file_open = None
	edit_file.file = None
	bottomlabel.configure(text=f"Line 1     Symbols 0       Text  ")
	# Change to default a last file
	with open('session.json', 'r', encoding='utf-8') as f:
		SessionJson = json.load(f)
	SessionJson['file'] = "None"
	with open('session.json','w') as f:
		json.dump(SessionJson ,f)


def close_file(*args):
	root.title("New Editor")
	text_editor.delete(1.0, END)
	edit_file.file_open = None
	edit_file.file = None
	edit_file.file_extensionl = "Text"
	bottomlabel.configure(text=f"Line 1     Symbols 0       Text  ")
	# Change to default a last file
	with open('session.json', 'r', encoding='utf-8') as f:
		SessionJson = json.load(f)
	SessionJson['file'] = "None"
	with open('session.json','w') as f:
		json.dump(SessionJson ,f)

def SetThemeLight():
	text_editor.configure(bg="#eff0eb", fg="black", insertbackground="black")
	with open('preferences.json', 'r', encoding='utf-8') as f:
		SettingsJson = json.load(f)
	SettingsJson['View']["theme"] = "Light"
	with open('preferences.json','w') as f:
		json.dump(SettingsJson ,f)

def SetThemeDark():
	text_editor.configure(bg="#282923", fg="#F8F8F2", insertbackground="white")
	with open('preferences.json', 'r', encoding='utf-8') as f:
		SettingsJson = json.load(f)
	SettingsJson['View']["theme"] = "Dark Classic"
	with open('preferences.json','w') as f:
		json.dump(SettingsJson ,f)

class WindowAbout(Tk):
	def __init__(self, *arg, **kwarg):
		super().__init__(*arg, **kwarg)

		self.title("New Editor")
		w = self.winfo_screenwidth()
		h = self.winfo_screenheight()
		w = w//2 # Center Window
		h = h//2 
		w = w - 200
		h = h - 200
		self.geometry('450x210+{}+{}'.format(w, h))
		self["bg"] = "#e1e1e3"
		self.resizable(width=False, height=False)

		label = Label(self, text='New Editor', font=('Arial', 20), fg="black", background="#e1e1e3")
		label.place(x=130, y=10)

		label = Label(self, text='Version: 1.0.0', font=('Arial', 12), fg="#19191a", background="#e1e1e3")
		label.place(x=151, y=88)
		label1 = Label(self, text='@Innokentie -  GitHub 2022 :)', font=('Arial', 12), fg="#5fc347", background="#e1e1e3")
		label1.place(x=40, y=140)


def about():
	WindowAbout().mainloop()




# INTERFACE
root = Tk()
root.title("New Editor")
root.geometry('1200x680')
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1)

#Widgets
top_menu = Menu(root)
file_items = Menu(top_menu, tearoff=0)
file_items.add_command(label='New File                         Ctrl+N', command=new_file)
file_items.add_command(label='Open File                        Ctrl+O', command=open_file)
file_items.add_command(label='Close File                        Ctrl+W', command=close_file)
file_items.add_command(label='Close All                                ', command=close_file)
file_items.add_command(label='Save                               Ctrl+S', command=save_file)
file_items.add_command(label='Save All                                 ')
file_items.add_separator()
file_items.add_command(label='All Hot Keys                             ')
file_items.add_separator()
file_items.add_command(label='About                            ', command=about)
file_items.add_command(label='Exit                             ', command=quit)

view_items = Menu(top_menu, tearoff=0)
wordwrap = BooleanVar()
view_items.add_radiobutton(label="Word Wrap", variable=wordwrap, value=1, command=None)#SetWordWrap
view_theme = Menu(view_items, tearoff=0)
view_theme.add_command(label="Dark Classic", command=SetThemeDark)
view_theme.add_command(label="Light", command=SetThemeLight)

settings_items = Menu(top_menu, tearoff=0)
settings_items.add_command(label='Settings', command=None)

top_menu.add_cascade(label='File', menu=file_items)
top_menu.add_cascade(label="View", menu=view_items)
view_items.add_cascade(label="Theme", menu=view_theme)
top_menu.add_cascade(label='Settings', menu=settings_items)
root.config(menu=top_menu)

#Editor
text_editor = Text(root, bg=f'{colors.dark_bg}', fg=f'{colors.dark_fg}', font=('Consolas', 13), insertbackground="white", insertwidth=3, wrap=NONE)
text_editor.grid(column=1, row=0, sticky='nsew')

#Scrollbar y
scrollbary = Scrollbar(root, orient=VERTICAL)
text_editor.configure(yscrollcommand=scrollbary.set)
scrollbary.config(command=text_editor.yview, cursor="arrow")# sb_v_double_arrow
scrollbary.grid(column=2, row=0, sticky='ns')
#Scrollbar x
scrollbarx = Scrollbar(root, orient=HORIZONTAL)
text_editor.configure(xscrollcommand=scrollbarx.set)
scrollbarx.config(command=text_editor.xview, cursor="arrow")# sb_h_double_arrow
scrollbarx.grid(column=1, row=1, sticky='we')

#Bottom status
bottomlabel = Label(root, text=f"Line 1     Symbols 0       Text  ", fg="#303030", font=('Consolas', 9), bg="#b3b3b3", anchor='e', highlightthickness=2)
bottomlabel.grid(column=0, columnspan=2, row=2, sticky='wes')


# Binds
root.bind("<Control-MouseWheel>", MouseResizeFont)
root.bind("<Control-KeyPress-o>", open_file)
root.bind("<Control-KeyPress-n>", new_file)
root.bind("<Control-KeyPress-s>", save_file)
root.bind("<Control-KeyPress-w>", close_file)


LoadPreferences()
LoadSession()
root.mainloop()
