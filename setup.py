import sys
import webbrowser
from setuptools import setup

web_url = 'http://pythonghana.org'

if 'install' in sys.argv or 'bdist_wheel' in sys.argv:
    webbrowser.open(web_url)

setup(
    name='pythonghana',
    version='1.0.1',
    maintainer='Noah Alorwu',
    maintainer_email='noah@pythonghana.org',
    url="https://github.com/pythonghana/pip-python-ghana.git",
)
