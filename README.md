# Pruebas automatizadas de app center
## Instalacion de python
Primero que nada, siguiendo las guias se instala python en la computadora donde se quiere montar el ambiente
- [Windows](https://learn.microsoft.com/en-us/windows/python/beginners)
- [Ubuntu](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html)
>
## Ejecucion del ambiente de pruebas
Lo primero es clonar este repo haciendo un 
~~~
git clone https://github.com/MarttinezJS/Pruebas-app-center.git
~~~
Luego ingresamos a la carpeta del proyecto ejecutamos el comando
~~~
uvicorn app.main:app --reload
~~~
Y por último en consola se mostraran las pruebas programadas
