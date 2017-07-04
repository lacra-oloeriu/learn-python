try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'I learn python',
    'author': 'Lora',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'lacramioara.oloeriu@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME1'],
    'scripts': [pro1.py],
    'name': 'project1'
}

setup(**config)
