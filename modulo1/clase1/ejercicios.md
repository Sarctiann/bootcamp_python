# Ejercicios de la Clase 1

<!--toc:start-->

- [Ejercicios de la Clase 1](#ejercicios-de-la-clase-1)
  - [Ejercicios](#ejercicios) - [Aprender a Navegar en el editor de texto](#aprender-a-navegar-en-el-editor-de-texto)
  <!--toc:end-->

Este es un archivo de markdown. Para quienes no saben que es esto, es un lenguaje
"marcado" que luego se presenta en formato a HTML, y es por convención uno de los
lenguajes mas utilizado para documentar aplicaciones, proyectos, repositorios, etc.

Si están utilizando VSCode pueden probar la combinación de teclas
`Ctrl` + `Shift` + `V` para visualizar este archivo en formato HTML.
En GitHub lo pueden visualizar directamente, en otros editores con seguridad existe
la opción o el plugin para visualizarlo.

Por otra parte el el lenguaje de marcado utilizado para los bloques de texto de
los "Jupyter Notebooks" lamentablemente es un tema que no está dentro del alcance
de este curso. Pero les recomiendo que investiguen al respecto.

- [Markdown](https://www.markdownguide.org/cheat-sheet/)
- [Jupyter Notebooks](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb)

## Ejercicios

Aún no hemos visto nada de Python. Por lo tanto a continuación les voy a dar algunos
consejos mas bien orientados a quines recién están comenzando con la programación
o al menos con Python.

> **Nota**: Voy a asumir que utilizan Windows como sistema operativo, y VSCode
> como editor de texto. Sin embargo yo personalmente no utilizo ni uno ni lo otro.
> por lo que si vos tampoco lo haces, seguramente ya lo sepas, todo lo descrito
> a continuación es aplicable a cualquier sistema operativo y cualquier editor
> de texto. Solo cambian algunos comandos y atajos de teclado.

### Aprender a Navegar en el editor de texto

Los Editores de Texto modernos son la herramienta fundamental que nos resuelve 3
fundamentales:

- El Editor, es donde escribimos nuestro código.
- El Explorador de archivos, donde navegamos creamos, abrimos, modificamos, y
  borramos archivos.
- La terminal del sistema, donde interactuamos con las herramientas de linea de
  comando tanto del sistema como también de las herramientas de desarrollo.

Estas 3 cosas ya están disponibles en nuestras computadoras, por lo que podríamos
programar usando por ejemplo "Bloc de Notas", "PowerShell" o "CMD", y "Explorador
de Archivos" (en Windows). Y en potencia podríamos obtener exactamente los mismo
resultados, pero a un costo impagable de tiempo y esfuerzo.

Así que vamos a practicar algunas cuestiones básicas:

1. Tené siempre a mano su editor de texto, podés configurar un atajo de teclado
   para abrirlo o colocar su acceso directo en tu escritorio o menú de inicio.
1. Practicar sus atajos de teclado, y/o configurarlos a tu gusto.
1. Configurar la terminal por defecto. Preferentemente una terminal de tipo bash.
1. Practicar la diferencia entre abrir un solo archivo, abrir un directorio y un
   espacio de trabajo.
1. Practicar a navegar en la terminal con los comandos:

   - `cd ..` como también `cd nombre_de_directorio` tené presente la diferencia
     entre "rutes relativas" y "rutes absolutas".
   - Las teclas `[UP]` y `[DOWN]` para navegar en el historial de comandos.
   - `ls -la`
   - `mkdir`
   - `code` (si estás utilizando Visual Studio Code)
   - `python` para abrir el interprete de Python (REPL).

   - Recordá que para salir de python puede ejecutar `quit()` o `exit()`. mientras
     que para salir del terminal (cerrar la session de teerminal) podés ejecutar
     `exit`. Tanto en Python como en el shell podés utilizar la combinación de
     teclas `Ctrl + C` o `Ctrl + D` para cancelar/terminal la ejecución de un comando.

1. Familiarizate con el REPL de python, usalo como reemplazo de la calculadora.

   - podés escribir expresiones como `2+2` y luego presionar `[Enter]` para evaluar
     la expresión. El REPL imprimirá el resultado automáticamente.
   - luego podés crear un archivo con extensión `.py` y escribir estas mismas expresiones,
     pero tené en cuenta que esta vez vas a necesitar agregar la función `print`
     para que se muestre en pantalla: `print(2+2)`.
   - Finalmente podés ejecutarlo con el comando `python nombre_del_archivo.py`.

1. Practicá puntualmente una combinación de teclas que le sirva para cambiar el
   foco entre la terminal y el editor de texto.
1. Intentá ejecutar tu/s archivos de python desde la terminal del sistema (no la
   integrada en el editor).
1. Intentá crear un archivo python en el "Block de notas". Y ejecutarlo desde la
   terminal del sistema.
1. (de onda) Si hablas inglés Felicidades, sino, ponete en marcha! Las tecnologías
   que vamos a utilizar en este curso como cualquier otra en este mundo del desarrollo
   de de software, evolucionan todos los días, y puede pasar algún tiempo hasta que
   encuentres documentación o que alguien te lo explique en español. Además si bien
   es cierto que están apareciendo mas herramientas de traducción en "tiempo real",
   hablar inglés te va a facilitar (sino permitir) dedicarte laboralmente a hermosa
   profesión.

Por favor, Anotá cualquier inquietud, dificultad, o comentario que tengas de estos
ejercicios. Y si tenés alguna duda, no dudes en preguntar. Lo revisaremos en la
siguiente clase o de manera asíncrona si es posible.
