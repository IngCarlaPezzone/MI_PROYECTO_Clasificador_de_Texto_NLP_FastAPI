from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from utils import clasificar_texto, presentacion

app = FastAPI()

@app.get("/", 
         response_class=HTMLResponse)
def home():
    return presentacion()

# Ruta de la API para la clasificación de texto
@app.post(path = '/clasificador',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el texto que quiera clasificar en el box abajo.<br>
                        3. Scrollear a "Resposes" para ver el resultado de la clasificación.
                        </font>
                        """)
async def clasificador(texto: str):
     return clasificar_texto(texto)
