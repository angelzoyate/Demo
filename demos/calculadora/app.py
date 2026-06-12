import web

urls = (
    '/', 'Index',
    '/calculadora','Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    

class Calculadora:
    def GET(self):
        numero_1 = ""
        numero_2 = ""
        resultado = ""
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero_1 = int(formulario['numero_1'])
        numero_2 = int(formulario['numero_2'])
        operacion = formulario['operacion']
        print (operacion)
        if operacion == "sumar":
    
             resultado = numero_1 + numero_2
             return render.calculadora(numero_1, numero_2,resultado)
        elif operacion == "restar":
            resultado = numero_1 - numero_2
            return render.calculadora(numero_1,numero_2,resultado)
        elif operacion == "multiplicar":
            resultado = numero_1 * numero_2
            return render.calculadora(numero_1, numero_2, resultado)
        elif operacion == "dividir":
            resultado = numero_2 != 0 and numero_1 / numero_2 or "Error"
            return render.calculadora(numero_1, numero_2, resultado)
        elif operacion == "raiz cuadrada al numero_1":
            resultado = numero_1 ** 0.5
            return render.calculadora(numero_1, numero_2, resultado)
        elif operacion == "potencia numero_1 ** numero_2":
            resultado = numero_1 ** numero_2
            return render.calculadora(numero_1, numero_2, resultado)
        elif operacion == "modulo":
            resultado = numero_1 % numero_2
            return render.calculadora(numero_1, numero_2, resultado)
        elif operacion == "limpiar los valores":
            numero_1, numero_2, resultado = "", "", ""
            return render.calculadora(numero_1, numero_2, resultado)

if __name__ == "__main__":
    app.run()