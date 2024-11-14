# setup.py
from setuptools import setup, find_packages

setup(
    name="my_app",  # Name of your application
    version="0.1",
    packages=find_packages(),  # Automatically finds packages in your project
    install_requires=[
        "flask",        # List your dependencies here
        "pytest",
        # Add any other dependencies your app needs
    ],
    entry_points={
        'console_scripts': [
            'my_app=app:main',  # Optional: allows running `my_app` in the console
        ],
    },
)
