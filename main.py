from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>API Funcionando</title></head>
        <body>
            <h1>✅ ¡Funciona Jorge!</h1>
            <p>Tu API ya está en línea.</p>
            <p>Agrega <code>/compare?query=lego</code> para probar la búsqueda.</p>
        </body>
    </html>
    """

@app.get("/compare", response_class=HTMLResponse)
def compare(query: str):
    return f"""
    <html>
        <head><title>Comparador</title></head>
        <body>
            <h1>Comparador de Precios</h1>
            <p>Búsqueda: <strong>{query}</strong></p>
        </body>
    </html>
    """

