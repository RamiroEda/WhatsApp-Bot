# WhatsApp-Bot Español [DEPRECATED]
Es un bot de variedad para chats de grupo o privado de WhatsApp orientado en mayor medida a un publico otaku.
El bot usa la cuenta y el nombre de WhatsApp de quien lo ejecuta para poder leer y responder a los comandos de manera automática.
## Requisitos previos
> * [Python 3.5+ 64-bit](https://www.python.org/downloads/release/python-352/)
> * [Kivy library 1.10.0+](https://kivy.org/docs/installation/installation-windows.html#install-win-dist)
> * [Selenium library 2+](http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)

## Instrucciones
1. Ejecutar el archivo **bot.py**
1. Esperar a que cargue todas las páginas necesarias
1. Una vez cargada la página WhatsApp Web, iniciar sesión por medio del celular
1. Seleccionar el chat en el que deseas que el bot ejecute comandos
1. **(Opcional)** Puedes activar/desactivar los comandos en el panel de control

> Nota: Para cambiar el caractér con el que detecta los comandos (por defecto es __*!*__) tienes que abrir **bot.py** en un editor de textos y buscar la variable *bot_ext*. Una vez que la encuentres sólo tienes que cambiar su valor al que tú gustes.

## Comandos del bot
* **say** *solicitud* -> Dirá lo que escribas. (ej. !say Soy un bot jeje)
* **search** *solicitud* -> Enviará 5 links a páginas sobre lo que escribas. (ej. !search 7 razones para no suicidarme)
* **dic** *solicitud* -> Buscará la definicion de diccionario sobre lo que escribas. (ej. !dic Computadora)
* **card** *solicitud* -> Mandará información de las tarjetas de Google sobre lo que escribas como bandas, lugares, personas, peliculas, repartos, etc. (ej. !card Cinemex cartelera)
* **chiste** -> Contará un chiste.
* **conf** -> Buscará confesiones anónimas de internet.
* **loli** -> Te dará una loli en adopción.
* **cat** -> Te mandará un gato bien prron.
* **dados** -> Te dará un número entre 1 y 6.
* **mywaifu** -> Buscará a tu verdadera waifu 2d.
* **monachina3d** -> Buscará a una mona china 3d.
* **8ball** *pregunta* -> Te responderá una pregunta (preguntas sí/no) que mandes.
* **cmd** -> Ver todos los comandos activos
