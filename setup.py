try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Use regex to extract the phone and email from copied text on your clipboard.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/phoneAndEmail_020918_1',
	'download_url': 'https://github.com/sunnylam13/phoneAndEmail_020918_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['pyperclip, re'],
	'scripts': [],
	'name': 'Phone and Email Extraction from Clipboard'
}

setup(**config)