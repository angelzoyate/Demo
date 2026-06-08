import web

urls = (
    "/", "Index"
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        titulo = "Página con parámetros"
        descripcion = """
                     Lorem ipsum dolor sit amet consectetur adipiscing elit placerat augue, eros auctor vestibulum arcu mi vulputate nisi dictum, nostra sem viverra ornare suscipit nulla venenatis duis. Fringilla rutrum iaculis semper sapien sem orci fermentum arcu himenaeos nisi, vivamus suspendisse sociosqu platea penatibus congue at nullam nunc dictum pharetra, porta et accumsan ac condimentum curae lacinia nascetur tincidunt. Pretium platea orci dui porta quisque curae gravida massa tellus taciti, felis penatibus venenatis conubia hac ridiculus vulputate aptent enim.
                     Lacus felis suscipit tincidunt venenatis in arcu urna luctus lobortis sagittis nostra ornare, ante nibh nunc placerat porttitor morbi enim faucibus bibendum aliquam semper. Consequat ornare nascetur pretium sapien laoreet orci nostra, quis sem dictum morbi commodo gravida. Accumsan aenean nec dis enim iaculis morbi tortor et potenti eleifend quam cubilia etiam porttitor neque, nulla proin dictum purus senectus ornare duis arcu urna libero nam gravida tristique.
                     """
        return render.parametros(titulo,descripcion)

if __name__ == "__main__":
    app.run()