from setuptools import setup, find_packages


def get_version() -> str:
    rel_path = "src/llm_cli/__init__.py"
    with open(rel_path, "r") as file:
        for line in file.read().splitlines():
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name='llm-cli',
    description='A CLI tool for interacting with the Gemini API',
    version=get_version(),
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        'click>=8.1.0',
        'google-generativeai>=0.7.2',
        'python-dotenv>=1.0.1'
    ],
    entry_points={
        'console_scripts': [
            'lcli=llm_cli.cli:cli',
            'llm-cli=llm_cli.cli:cli'
        ]
    },
    author='ddos',
)
