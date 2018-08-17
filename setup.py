import sys
import webbrowser
from setuptools import setup

web_url = 'http://pythonghana.org'

if 'install' in sys.argv or 'bdist_wheel' in sys.argv:
    webbrowser.open(web_url)

setup(
    name='python-ghana',
    version='1.0.0',
    maintainer='Noah Alorwu',
    maintainer_email='noah@pythonghana.org',
    url="https://github.com/pythonghana/pip-python-ghana.git",
)
