from tkinter import *
# Создаем главный объект (по сути окно приложения)
root = Tk()
# Настройка команд/вывод

def get_info():
    x = 0.05
    y = 0.14
    count = 0
    frame_bottom2 = Frame(root, bg='#fafafa', bd=5)
    frame_bottom2.place(relx= 0, rely= 0.14, relwidth=1, relheight=1)
    k = 0
    d = 0
    info = open('cha.txt','r')
    name = message.get().upper().strip().replace(' ','')
    for line in info:
        i = 0
        string = line.upper().replace(' ','')
        if d == 3:
            count += 1
            y += 0.03
            frame_bottom2 = Frame(root, bg='#ffb700', bd=5)
            frame_bottom2.place(relx= x, rely=y, relwidth=0.22, relheight=0.05)
            inform2 = Label(frame_bottom2, bg='#ffb700', font = 'Arial 9', text = line.strip().replace(';',''))
            inform2.pack()
            y -= 0.03
            d = 0
        for j in range(len(string)):
            if len(name) == i + 1:
                if (name[i] == string[j]) and (name[i-1] == string[j-1]) and (string[j+1]!='.'):
                    count += 1
                    if count % 3 == 1 and count != 1:
                        x += 0.23
                        y += -0.03
                    if count % 3 == 2:
                        y += 0.03
                    if count % 13 == 0:
                        x = 0.05
                        y += 0.12
                        count = 1
                    frame_bottom2 = Frame(root, bg='#ffb700', bd=5)
                    frame_bottom2.place(relx= x, rely=y, relwidth=0.22, relheight=0.05)
                    inform2 = Label(frame_bottom2, bg='#ffb700', font = 'Arial 9', text = line.strip().replace(';',''))
                    inform2.pack()
                    d += 1
                if d == 2:
                    d += 1
            if len(name) != i + 1:
                if name[i] == string[j]:
                    i += 1

                


    info.close()


# Настройки главного окна
# подредактировать размеры кнопок и вставок


# Указываем фоновый цвет
root['bg'] = '#fafafa'
# Указываем название окна
root.title('Приложения для сравнения цен')
# Указываем размеры окна
root.geometry('1920x1080')
#root.geometry('1280x720')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame_top = Frame(root, bg='#ffb700', bd=5)
# Также указываем его расположение
frame_top.place(relx=0.4, rely=0.05, relwidth=0.2, relheight=0.036)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.4, rely=0.09, relwidth=0.2, relheight=0.045)

# Создаем текстовое поле для получения данных от пользователя
message = StringVar()
name_model = Entry(textvariable = message)
name_model.place(relx=0.5, rely=0.03,relwidth=0.6, relheight=0.03, anchor="c")  # Размещение этого объекта, всегда нужно прописывать

# Создаем кнопку и при нажатии будет срабатывать метод
btn = Button(frame_top, text='Найти товар', command=get_info) # command
btn.pack()

# Создаем текстовую надпись, в которую будет выводиться информация
info = Label(frame_bottom, text='Информация о товаре', bg='#ffb700', font='Arial 14')
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()