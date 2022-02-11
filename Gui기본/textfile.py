from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") #가로x세로(띄워쓰기 x)


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended",  width =90, height=30, yscrollcommand = scrollbar.set)
listbox.pack(side="right")




def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() #구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)

#Edit 메뉴(빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가(radio 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)


# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="view", menu=menu_view)


scrollbar.config(command=listbox.yview)
root.config(menu=menu)
root.mainloop()