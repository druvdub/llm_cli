# LLM CLI

A command line interface to interact with multiple LLM instances.

Currently, the CLI supports the following LLMS:

- (Gemini)[https://gemini.google.com/app]

## Installation

```bash

pip install llm-cli

```

## Usage

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

```bash

git clone (https://github.com/druvdub/llm_cli)[https://github.com/druvdub/llm_cli]

cd llm_cli

pip install -e .

```

## License

Apache 2.0

```

```
