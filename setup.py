from setuptools import setup, find_packages


with open('README.rst') as file:
    long_description = file.read()


setup(
    name="frijoles",
    version="0.1.1",
    author="Pablo SEMINARIO",
    author_email="pablo@seminar.io",
    description="Simple notifications powered by jumping beans",
    long_description=long_description,
    license="GNU Affero General Public License v3",
    url="http://frijoles.antojitos.io/",
    download_url="https://github.com/Antojitos/frijoles/archive/0.1.1.tar.gz",
    keywords=["frijoles", "notifications", "api"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],

    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'Flask==0.12.3',
        'Flask-PyMongo==0.4.0'
    ],
)
