from setuptools import setup

def setup(
    name='brotherboat_app',
    packages=['Modules/WebApp/WebApp.py']
    include_package_data=True,
    install_requires=[
        'flask',
        'waitress',
        #'flask-sqlalchemy',
        #'flask-migrate',
        #'flask-login',
        #'flask-wtf',
        #'flask-bootstrap',
        #'flask-mail',
        #'flask-babel',
        #'flask-moment',
        #'flask-whooshalchemy',
        #'flask-whooshalchemyplus',
        #'uvicorn',
        #'fastapi',
        #'python-multipart',
        #'pydantic',
        #'requests',
        #'pytz',
    ],
)