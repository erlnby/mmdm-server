from uvicorn import run

if __name__ == '__main__':
    run('app.app:app', reload=True)
