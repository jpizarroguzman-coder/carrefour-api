from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/compare", response_class=HTMLResponse)
def compare(query: str = Query(...)):
    return f"""
    <html>
        <head><title>Prueba</title></head>
        <body>
            <h1>¡Funciona Jorge! 🎉</h1>
            <p>Tu búsqueda fue: <strong>{query}</strong></p>
        </body>
    </html>
    """
