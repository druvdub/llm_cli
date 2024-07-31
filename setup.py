from setuptools import setup, find_packages
import importlib.metadata

setup(
    name='gemini-cli',
    description='A CLI tool for interacting with the Gemini API',
    version=importlib.metadata.version('gemini_cli'),
    packages=find_packages(),
    install_requires=[
        'click>=8.1.0',
        'google-generativeai>=0.7.2'
    ],
    entry_points={
        'console_scripts': [
            'gemini-cli=gemini_cli.cli:cli'
        ]
    },
    author='ddos',
)
