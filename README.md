Para utilizar el assembler, debemos posicionar en la misma carpeta los
siguientes archivos:

-assembler.py
-input.ass

En input.ass se colocara el assembly a evaluar, o simplemente ir a la linea 43
de "assembler.py": 'f = open("input.ass","r")', y cambiar "input.ass", al
respectivo .ass que se quiera leer.

En caso de no funcionar la lectura, teniendo en cuenta que estamos posicionados
en el lugar indicado previamente, ejecutar en la terminal el comando:
"pip install ass", este comando simplemente es para que se pueda leer el .ass.

Si se cumple todo lo anterior, se generaran: "newfile.out" y "newfile.mem" si
el assembly esta bien escrito, en caso contrario, indicara las lineas que 
contienen errores.
