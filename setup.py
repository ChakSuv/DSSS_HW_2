from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    description="A simple math quiz package",
    author="Suvrima",
    license="Apache",
    packages=find_packages(),
    install_requires=[],  # add dependencies here if any
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:main',  # executable command
        ],
    },
)
