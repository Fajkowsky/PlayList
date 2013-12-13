# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'Django==1.6.0',
    'dj-database-url==0.2.2'.
	'dj-static==0.0.5',
	'gunicorn==18.0',
	'static==0.4',
	'wsgiref==0.1.2',
]

dependency_links = [
]

if __name__ == '__main__':
    setup(name='PlayList',
          version='0.1',
          author=[],
          author_email=[],
          packages=find_packages(),
          install_requires=install_requires,
          dependency_links=dependency_links,
          )
