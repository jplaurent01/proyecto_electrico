# Proyecto Eléctrico




Dentro de la carpeta **src** se encuentra el código fuente y las dependencias del proyecto eléctrico elaborado para el Centro de Investigación en Ciencias del Movimiento Humano de la Universidad de Costa Rica.




## Acerca del proyecto




El software desarrollado es una aplicación de escritorio capaz de leer archivos **.csv** generados por el sensor FreeStyle Libre Libre, sistema que permite la realización de lecturas de glucosa continuas en tiempo real. Una vez leídos los archivos contenidos en la carpeta **input_file**, se pregunta por la cantidad de pacientes, luego establecidos estos, se permite agregar rangos de tiempo para el estudio del comportamiento de la glucosa, donde se pide el nombre del paciente, la cantidad de rangos de tiempos y por último seleccionar el número de identificación del sensor FreeStyle Libre, luego de generar el gráfico de los datos el usuario tendrá la posibilidad de filtrar los datos y almacenarlos en su computadora mediante la generación de un archivo **.csv**.


## Ejecución del código


Dentro de la carpeta **src** ejecute el siguiente comando:


> py .\main.py


Debe alimentar el programa con el archivo contenido dentro de la carpeta **input_file**.


## Creación de un ejecutable


Ejecutar un comando similar al que se muestra a continuación en la terminal:


>  C:\Users\Administrador\AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter;customtkinter/


> pyinstaller --noconfirm --onefile --windowed --add-data "C:\Users\Administrador\AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter;customtkinter/


Creado el **exe**, agregar en el archivo **main.spec**, lo siguiente en la línea 12:


> hiddenimports=["babel.numbers"]


Lugo correr en terminal:


> pyinstaller main.spec


Se creará un archivo ejecutable sin terminal.
Para agregar una terminal, debe agregar en el archivo **main.spec**, lo siguiente:


> console=True


De nuevo ejecute:


> pyinstaller main.spec


## Versiones de librerías utilizadas


+ numpy (1.23.2)
+ Pillow (9.2.0)
+ pandas (1.4.4)
+ pandastable (0.13.0)
+ customtkinter (5.2.2)
+ tkcalendar (1.6.1)
+ plotly (5.10.0)





