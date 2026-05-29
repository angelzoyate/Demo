import web

urls = (
    '/', 'Inicio',
    '/nosotros', 'Nosotros',
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

class Nosotros:
    def GET(self):
        return html(NAV + "<h1>Información</h1><p>Detalles sobre nuestra empresa.</p>")

class Contacto:
    def GET(self):
        return html(NAV + "<h1>Contacto</h1><p>Formas de comunicarse con nosotros.</p>")

class Servicios:
    def GET(self):
        return html(NAV + "<h1>Lista de Servicios</h1><p>Consulta lo que ofrecemos aquí.</p>")

class ServicioDetalle:
    def GET(self, id):
        return html(NAV + f"<h1>Elemento #{id}</h1><p>Mostrando el detalle del registro seleccionado.</p>")

class Ingresar:
    def GET(self):
        return html(NAV + "<h1>Ingreso al Sistema</h1><p>Por favor, pon tus datos de usuario.</p>")

class Salir:
    def GET(self):
        return html(NAV + "<h1>Cierre de Sesión</h1><p>Has salido del sistema correctamente.</p>")

class CrearCuenta:
    def GET(self):
        return html(NAV + "<h1>Formulario de Registro</h1><p>Regístrate para obtener beneficios.</p>")

class Panel:
    def GET(self):
        return html(NAV + "<h1>Panel Principal</h1><p>Aquí se muestran las estadísticas generales.</p>")

class MiCuenta:
    def GET(self):
        return html(NAV + "<h1>Configuración de Cuenta</h1><p>Modifica tus datos personales en esta sección.</p>")

class Administrador:
    def GET(self):
        return html(NAV + "<h1>Zona de Control</h1><p>Espacio reservado para los administradores.</p>")

if __name__ == "__main__":
    app.run()