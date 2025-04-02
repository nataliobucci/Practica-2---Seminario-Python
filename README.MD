README

Descripción

Este es mi proyecto para la entrega del ejercicio 10, donde incluyo las tablas de resultados y los MVPs. El código está organizado para ejecutarse desde un notebook, y las funciones auxiliares están en la carpeta (src).

Instalación de Dependencias

Para que todo funcione correctamente, hay que instalar algunas dependencias. Si tienes un archivo "dependencias.txt", solo ejecuta:

pip install -r dependencias.txt

Si no, instala manualmente los paquetes necesarios.



Cómo Ejecutarlo

Abrir una terminal y ve a la carpeta del proyecto.

Ejecutar:

jupyter notebook

Abre el notebook en la carpeta notebooks y ejecútalo.

Importar el Módulo src

Si necesitas usar funciones de src en el notebook, agrega esto:

import sys

import os

sys.path.append(os.path.abspath("../src"))

import funciones

Con eso ya debería funcionar todo.

