import click
import os

from gemini_cli import __version__


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Get the version of the gemini-cli package.")
@click.pass_context
def cli(ctx, version):
    """A CLI tool for interacting with the Gemini API.
    can be invoked with 'gcli' or 'gemini-cli'.

    Examples: $ gcli --version
    """
    if version:
        _version()
    elif ctx.invoked_subcommand is None:
        click.echo("" + ctx.get_help())


def _version():
    """Get the version of the gemini-cli package."""
    click.echo(f"gemini-cli v{__version__}")


@cli.command("configure")
@click.option("--api-key", "-k", help="Quicker way to setup API for the Gemini API.", default=None)
def configure(api_key):
    """Configure the API key for the Gemini API."""
    click.echo("Configuring API key...")

    try:
        if not api_key:
            click.echo(
                click.style(
                    "\nNote: This package requires an API key to function. Please visit ", fg="magenta")
                + click.style(
                    "https://aistudio.google.com/app/apikey", fg="magenta")
                + click.style(
                    " to get your API key.\n", fg="magenta")
            )

            if click.confirm("Would you like to setup your API key now?", default=True, prompt_suffix=": "):
                api_key = click.prompt("Enter your Gemini API key",
                                       prompt_suffix=": ", hide_input=True, confirmation_prompt=True)
                os.environ["GOOGLE_API_KEY"] = api_key
                click.echo(
                    click.style(
                        "\nAPI key has been set successfully.", fg="green")
                )

                click.echo(
                    "\nInstallation complete. You can now use the gemini-cli commands."
                )
            else:
                click.echo(
                    click.style(
                        "API key not configured. Please set the GOOGLE_API_KEY environment variable manually.", fg="red"
                    )
                )
        else:
            os.environ["GOOGLE_API_KEY"] = api_key
            click.echo(
                click.style("\nAPI key has been set successfully.", fg="green")
            )

            click.echo(
                "\nInstallation complete. You can now use the gemini-cli commands. Please ensure that the API key is correct."
            )

        click.echo(
            click.style(
                "Get started by running 'gcli --help' to see the available commands.\n",
                bold=True
            )
        )
    except Exception as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )
