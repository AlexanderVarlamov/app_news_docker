import uvicorn
from fastapp import get_app
from conf import port

app = get_app()

if __name__ == '__main__':
    uvicorn.run(app, port=port, host='0.0.0.0', log_level='debug')