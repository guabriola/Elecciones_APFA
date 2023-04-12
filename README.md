# Elecciones_APFA
Trabajo final Python Avanzado


Funcionamiento general

    1. Clonar el repositorio de GitLab

git clone https://corp.antel.com.uy/repo/e792919/Elecciones_APFA.git

    2. cd /Elecciones_APFA

    3. Crear el entorno virtual

python3 -m venv entorno
       
    4. Activar el entorno virtual

En windows → entorno\Scripts\activate. Bat.
En linux → source entorno/bin/activate
       
    5. Instalar los modulos necesarios.

pip install -r app/requirements.txt
       
    6. Carga primaria de datos.
Se tiene que correr el script cargadatos.py que está dentro del proyecto. 
       
       Este script realiza las siguientes acciones:

        ◦ Crea los roles admin y std (standard)
        ◦ Crea el usuario admin con password 1234
        ◦ Crea tres usuarios, user1, user2 y user3 también con password 1234 para que puedan ser usados para pruebas rápidas.
        ◦ Crea dos listas una para votos en blanco y otra para anulados. 
        ◦ Carga todos los números de socios del padron del archivo HTML proporcionado. El cuál está en la raiz de la app (padron.html)
          
    7. Archivo .env para uso de datos confidenciales.
Se debe crear un archivo .env en el root de la aplicación con la sieguiente configuración:

	SECRET_KEY = <Una cadena de caracteres compleja>
	MAIL_SERVER = smtp.gmail.com
	MAIL_PORT = 465
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	# gmail authentication
	MAIL_USERNAME = <correo electronico>
	MAIL_PASSWORD = <password>
	SECURITY_PASSWORD_SALT=<Una cadena de caracteres compleja>
	#pass provisto por Gmail
	# mail accounts
	MAIL_DEFAULT_SENDER = <correo electronico>
	
	Son los datos necesarios para que funcione correctamente el envío de correos de verificación 	para cuando se crea un nuevo usuario.
 
    8. Arrancar el servidor FLASK

flask --app main run --port 5000

    9. Uso de la aplicación.
       
        ◦ Usuario no logueado:

Cuallquier persona puede entrar a la página y ver los resultados de la votación, en esta primera instancia solo apareceran las opciones de “Login” y  “Registrarse” en la barra de navegación.
Para registrarse va a tener que ingresar los datos solicitados, el formlario verifica que el usuario, número de socio y correo electronico no estén ya registrados en la base de datos. 
En caso que pase esta instancia y le va a enviar un correo de verificacion para poder terminar de registrar el usuario. La aplicación le da un mensaje de que tiene que cheuqear su casilla de correo. 

Para loguearse tiene que hacer clic en el link del correo y lo redirigirá directamente a la pagina de login donde debera poner su usuario y contraseña.
          
        ◦ Usuario logueado (std):

El usuario standard va a tener acceso desde la barra de navegación a votar, ver resultados y logout. La opción de agregar lista va a estar desabilitada y en un tono más oscuro.

Para votar simplemente es hacer clic en “Votar”, lo re-direcciona a la página donde solo deberá elegir lo que quiera votar (antes pre cargado por el Admin) y hacer clic en votar.
Automáticamente lo re-direcciona a la página de resultados. En caso que quiera votar nuevamente se le dará un mensaje que no puede votar nuevamente.

        ◦ Usuario logueado (admin):

El usuario admin va a tener acceso desde la barra de navegación a la opción de “Agregar Lista” donde va a poder ingresar el nro de lista (alfanumérico) y los candidatos a presidente y vice-presidente. Una vez que de clic en ingresar le dará un mensaje que la lista se cargó correctamente. 
Este usuario también puede votar, en las mismas condiciones que el usuario con rol standard.
