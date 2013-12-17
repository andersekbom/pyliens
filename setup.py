try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Aliens',
    'author': 'Anders Ekbom',
    'url': 'ekbom.org',
    'download_url': 'ekbom.org/donwload',
    'author_email': 'anders.ekbom@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pyliens'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)