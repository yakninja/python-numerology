from distutils.core import setup

setup(
    name='Numerology',
    version='0.1.0',
    author='Andrii Kravchuk',
    author_email='andrii@yakninja.pro',
    packages=['numerology', 'numerology.vedic', 'numerology.tests'],
    url='http://pypi.python.org/pypi/Numerology/',
    license='LICENSE.txt',
    description='Numerology related stuff.',
    long_description=open('README.txt').read(),
)