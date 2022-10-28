import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title = 'aulinha 1'
)

cursos = {
    1: {
        'nome': 'python',
        'aulas': 20,
        'horas': 80,
        'nome':'Cleber',
    },
    2: {
        'nome': 'Java',
        'aulas': 15,
        'horas': 10,
        'nome':'Leoncio',
    },
}

@app.get('/')
async def get_cursos():
    return cursos

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)