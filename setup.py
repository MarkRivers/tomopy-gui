from setuptools import setup, find_packages

setup(
    name='tomopy_gui',
    version=open('VERSION').read().strip(),
    #version=__version__,
    author='Matthias Vogelgesang',
    author_email='matthias.vogelgesang@kit.edu',
    url='https://github.com/ufo-kit',
    packages=find_packages(),
    package_data={'':['gui.ui', 'roi.ui']},
    scripts=['bin/tomopy_gui'],
    description='tomopy GUI',
    install_requires=['pyqtgraph'],
    zip_safe=False,
)

