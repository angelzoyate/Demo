import web

urls = (
    '/', 'Index',
)

class Index:
    def GET(self):
        return "Esta en la URL 1"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()