"""Create pypi package."""

import setuptools

setuptools.setup(
    name='sem_ver',
    version='0.0.0',  # version will get replaced by git version tag - do not edit
    author='Peter Linss',
    author_email='peter@linss.com',
    description='Semantic version handler',
    url='https://github.com/plinss/sem_ver/',
    license="XXX",

    packages=['sem_ver'],
    package_data={'sem_ver': ['py.typed']},

    install_requires=[
        # include any dependency packages here
    ],
    extras_require={
        'dev': ['mypy',
                'flake8', 'flake8-import-order', 'flake8-annotations', 'flake8-type-annotations', 'flake8-docstrings',
                'pep8-naming'],
    },
    python_requires='>=3.6'
)
