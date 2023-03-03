import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iertools',
    version='0.1.1',
    author=['Guillermo Barrios'],
    author_email=['gbv@ier.unam.mx'],
    description='EnerData tools to play with data visualization',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/EneRDataMx/edtools',
    project_urls = {
        "Bug Tracker": "https://github.com/EneRDataMx/edtools/issues"
    },
    license='MIT',
    packages=['edtools'],
    install_requires=['requests','pandas','numpy','datetime'],
)
