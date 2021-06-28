
from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='sep10',
    version='0.0.3',
    description='Stellar Sep10 Modules',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/garantor/StellarSep10',  
    author='Afolabi',
    author_email='afolabisunday31@yahoo.com',
    license='MIT', 
    classifiers=classifiers,
    keywords=['python', 'Stellar', 'Blockchain', 'Sep10'], 
    packages=find_packages(exclude=[".gitignore", "test.py","tomlTest.py", ]),
    install_requires=['stellar_sdk', 'flask', 'validators']
)

