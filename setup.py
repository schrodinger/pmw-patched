from distutils.core import setup

setup(
    name='Pmw',
    version='2.0.1+3',
    package_dir={'': 'modules'},
    py_modules=[
        'Pmw',
        'PmwBlt',
        'PmwColor',
    ],
    url='https://github.com/schrodinger/pmw-patched',
    description='Python megawidgets with essential patches applied',
    license='MIT',
)
