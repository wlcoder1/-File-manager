import os 


#Функция регистрации для пользователя
def sign_in():
    global user_input
    user_input = input('Enter your login: ')
    if not os.path.isdir(user_input):
        os.mkdir(user_input)
    os.chdir(user_input)



#Функция создает файл, принимает имя файла и возможный текст
def create_file(filename,text=False):
    with open(filename,'w',encoding='utf-8') as f:
        if text:
            f.write(text)
#Функция создает папку, первый параметр - название папки, если мы хотим перейти в какую-то дириекторию, то второй параметр - ее название
def create_folder(foldername,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.mkdir(foldername)
#Функция удаляет папку, первый параметр - название папки, если мы хотим перейти в какую-то дириекторию, то второй параметр - ее название
def remove_folder(foldername, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.rmdir(foldername)

#Функция удаляет файл, первый параметр - название файла, если мы хотим перейти в какую-то директорию, то второй параметр - ее название  
def remove_file(filename,inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    os.remove(filename)

#Функция меняет директорию 
def change_dir(dirname):
    os.chdir(dirname)
    
#Функция чтения файла, первый параметр - название файла, если мы хотим перейти в какую-то директорию, то второй параметр - ее название
def read_file(filename, inside_folder=False):
    if inside_folder:
        os.chdir(inside_folder)
    with open(filename,'r',encoding='utf-8') as f:
        print(f.read())

            




sign_in()
create_folder('frwrwerwer','whate2ver')
