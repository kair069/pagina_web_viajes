# 🌍 Página Web de Viajes

Una aplicación web desarrollada con **Django** y **MySQL** que permite gestionar viajes, clientes, y más, con funcionalidades avanzadas como autenticación de usuarios y operaciones CRUD. Esta página está diseñada para ofrecer una experiencia ágil y moderna tanto para clientes como para administradores.

## 📊 Características principales

- **🔑 Autenticación**: Registro, inicio de sesión y gestión de accesos de usuarios.
- **📄 CRUD de Clientes**: Crear, leer, actualizar y eliminar información de clientes.
- **✈️ CRUD de Viajes**: Administrar información relacionada con los viajes.
- **🏠 Portada**: Diseño atractivo para clientes.
- **🎥 Videos demostrativos**: Muestra del funcionamiento de la aplicación.

## 🎥 Videos de demostración

1. **Configuración en MySQL Workbench**: [Ver video](https://github.com/kair069/pagina_web_viajes/blob/main/MySQL%20Workbench%202024-12-10%2007-24-28.mp4)
2. **Lista de Clientes**: [Ver video](https://github.com/kair069/pagina_web_viajes/blob/main/Lista%20de%20Clientes%20-%20Personal_%20Microsoft%E2%80%8B%20Edge%202024-12-10%2007-25-13.mp4)
3. **Archivo settings.py en Visual Studio Code**: [Video 1](https://github.com/kair069/pagina_web_viajes/blob/main/settings.py%20-%20myproject%20-%20Visual%20Studio%20Code%202024-12-10%2007-22-48.mp4) | [Video 2](https://github.com/kair069/pagina_web_viajes/blob/main/settings.py%20-%20myproject%20-%20Visual%20Studio%20Code%202024-12-10%2007-26-27.mp4)

## 🔧 Tecnologías utilizadas

- **Backend**: Django (Python)
- **Base de datos**: MySQL
- **Frontend**: HTML, CSS, Bootstrap
- **Control de versiones**: Git y GitHub

## 🔎 Instrucciones de instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/kair069/pagina_web_viajes.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd pagina_web_viajes
   ```

3. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate # En Windows: env\Scripts\activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

5. Configura la base de datos en el archivo `settings.py`.

6. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

8. Accede a la página en tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🎨 Capturas de pantalla

(Agrega aquí algunas capturas de pantalla de tu aplicación para mostrar las funcionalidades clave).

## ✨ Funcionalidades futuras

- Integración de pasarelas de pago.
- Reportes avanzados de viajes y clientes.
- Notificaciones automáticas para clientes.

## 🌟 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un *issue* o envía un *pull request* si deseas colaborar.

## ❤️ Agradecimientos

Gracias por visitar este proyecto. Si te gustó, ¡dale una estrella al repositorio! 🌟

---

© 2024 - Página Web de Viajes
