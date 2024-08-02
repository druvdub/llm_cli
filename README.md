# LLM CLI

A command line interface to interact with multiple LLM instances.

Currently, the CLI supports the following LLMs:

- [Gemini AI](https://gemini.google.com/app)

## Installation

To install the CLI, you do need to have Python `>=3.9` installed on your machine.

```bash

pip install llm-cli

```

## Usage

To get started, you can run the following command:

```bash

llm-cli --help

Output:

Usage: llm-cli [OPTIONS] COMMAND [ARGS]...

  A CLI tool for interacting with the Gemini API. can be invoked with 'lcli'
  or 'llm-cli'.

  Examples: $ lcli --version

Options:
  -v, --version  Get the version of the llm-cli package.
  --help         Show this message and exit.

Commands:
  configure  Configure the API key for the Gemini API.
  prompt     Generate content from a prompt and/or other files.
  verify     Check if the API key is set.

```

## Development

For developing the application in a virtual environment, you can install the necessary dependencies by installing them using the requirements file.

```bash

git clone https://github.com/druvdub/llm_cli

cd llm_cli

pip install -r requirements.txt
```

and installing the package in editable mode.

```bash

pip install -e .

```

## License

Apache 2.0 License - see the LICENSE file for details.
