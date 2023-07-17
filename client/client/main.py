"""
version 
@author varlamov.a
@email varlamov.a@rt.ru
@date 03.07.2023
@time 16:27
"""
from flask_app import get_app
from conf import frontend_port

if __name__ == '__main__':
    app=get_app()
    app.run(debug=True, host='0.0.0.0', port=frontend_port)
