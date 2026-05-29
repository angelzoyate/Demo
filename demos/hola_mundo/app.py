import web

urls = (
    '/', 'Inicio',
    '/url 2', 'Url 2',
    '/contacto', 'Contacto',
    '/servicios', 'Servicios',
    r'/servicio/(\d+)', 'ServicioDetalle',
    '/ingresar', 'Ingresar',
    '/salir', 'Salir',
    '/crear-cuenta', 'CrearCuenta',
    '/panel', 'Panel',
    '/mi-cuenta', 'MiCuenta',
    '/administrador', 'Administrador',
)

app = web.application(urls, globals())

# Menú de navegación
NAV = """
<a href="/">Principal</a> |
<a href="/nosotros">Quiénes Somos</a> |
<a href="/servicios">Servicios</a> |
<a href="/panel">Panel de Usuario</a> |
<a href="/mi-cuenta">Mi Cuenta</a> |
<a href="/administrador">Administrador</a> |
<a href="/contacto">Escríbenos</a> |
<a href="/ingresar">Acceder</a> |
<a href="/crear-cuenta">Crear Cuenta</a>
<hr>
"""

def html(contenido):
    web.header('Content-Type', 'text/html; charset=utf-8')
    return contenido

# --- Clases y Métodos GET ---

class Inicio:
    def GET(self):
        return html(NAV + "<h1>Página Principal</h1><p>Bienvenido, Hola mundo.</p>")

class Url2:
    def GET(self):
        return html(NAV + "<h1>Información</h1><p>Esta es mi URL 2.</p>")

class Contacto:
    def GET(self):
        return html(NAV + "<h1>Contacto</h1><p>Esta es mi URL 3.</p>")

class Servicios:
    def GET(self):
        return html(NAV + "<h1>Lista de Servicios</h1><p>Esta es mi URL 4.</p>")

class ServicioDetalle:
    def GET(self, id):
        return html(NAV + f"<h1>Elemento #{id}</h1><p>Esta es mi URL 5.</p>")

class Ingresar:
    def GET(self):
        return html(NAV + "<h1>Ingreso al Sistema</h1><p>Esta es mi URL 6.</p>")

class Salir:
    def GET(self):
        return html(NAV + "<h1>Cierre de Sesión</h1><p>Esta es mi URL 7.</p>")

class CrearCuenta:
    def GET(self):
        return html(NAV + "<h1>Formulario de Registro</h1><p>Esta es mi URL 8.</p>")

class Panel:
    def GET(self):
        return html(NAV + "<h1>Panel Principal</h1><p>Esta es mi URL 9.</p>")

class MiCuenta:
    def GET(self):
        return html(NAV + "<h1>Configuración de Cuenta</h1><p>Esta es mi URL 10.</p>")

class Administrador:
    def GET(self):
        return html(NAV + "<h1>Zona de Control</h1><p>Adios.</p>")

if __name__ == "__main__":
    app.run()