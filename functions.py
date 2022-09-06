class Activity:
    #crear metodo inicializador de la clase
    
    def init_(self):
        #declaracion de variables
        self.editor_name= "visual studio code"
        self.language = 'python'
        self.version=3.0
        
        #3 metodo que imprime los valores de las variables
    def show_info(self):
        print(f'estamos trabajando en',{self.editor_name},'programando en:' ,{self.language},{self.version})
    def say_hi():
        print("hello world")
    def input_data_user():
        user_name = input('ingresa tu nombre')
        while True:
            try:
                age=int(input('Edad'))
            except:
                print('error no es un valor numerico')
                print(f'{user_name},tiene  {age} años') 
    def subcadena(email,password):
        emailValid="@autonoma.edu.co"
        passwordValid="tad1-2022"
        if  email.endswith(emailValid)and passwordValid.find(passwordValid)!=-1:
            print("string found")
        else:
            print("string not found")

#desde el archivo importamos la clase
from functions import functions 

#cuando se llama la clase con los parentersis se ejecuta el metodo init
inst_functions = functions()