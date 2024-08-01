import click
import os

from gemini_cli import __version__
from gemini_cli.api.gemini import Gemini


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
@click.option("--api-key", "-k", help="Quicker way to setup API for the Gemini API.")
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


@cli.command("prompt")
@click.option("--text", "-t", help="Text prompt to interact with Gemini")
@click.option("--image", "-i", multiple=True, help="Image path to upload to Gemini. Can upload multiple images")
@click.option("--file", "-f", multiple=True, help="File path to upload to Gemini. Can upload multiple files. Images, Videos, Audio, Documents. Files are stored upto 48 hours before being deleted automatically. Uses files API")
@click.pass_context
def prompt(ctx, text, image, file):
    """Generate content from a prompt and/or other files."""
    if not (text or image or file):
        click.echo(
            click.style(
                "Please provide atleast one of the following options: --text, --image, --file.", fg="bright_red", )
        )
        click.echo(ctx.get_help())

    try:
        gemini = Gemini()

    except ValueError as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )
