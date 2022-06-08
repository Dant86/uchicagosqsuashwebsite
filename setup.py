from setuptools import setup

requires = (
    'flask',
    'flask-sqlalchemy',
    'python-dotenv',
    'psycopg2',
    'flask-testing',
    'pandas',
    'requests'
)

setup(
    name='uchisquashsite',
    version='0.1',
    description='Website for the UChicago Squash Team',
    url='https://github.com/Dant86/uchicagosqsuashwebsite',
    author='Vedant Pathak, Stephen Pontikes',
    author_email='vedantdpathak@iCloud.com',
    license='MIT',
    packages=['uchisquashsite'],
    zip_safe=False,
    install_requires=requires
)