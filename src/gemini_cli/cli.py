import click
import os


@click.group()
def cli():
    pass


@click.command('configure')
def configure():
    click.echo("Configuring API key...")

    click.echo(
        click.style(
            "\nNote: This package requires an API key to function. Please visit ", fg="magenta")
        + click.style(
            "https://aistudio.google.com/app/apikey", underline=True, fg="magenta", bold=True)
        + click.style(
            " to get your API key.\n", fg="magenta")
    )

    if click.confirm("Would you like to setup your API key now?", default=True, prompt_suffix=": "):
        api_key = click.prompt("Enter your Gemini API key",
                               prompt_suffix=": ", hide_input=True, confirmation_prompt=True)
        os.environ["GEMINI_API_KEY"] = api_key
        click.echo(
            click.style("\nAPI key has been set successfully.", fg="green")
        )
    else:
        click.echo(
            click.style(
                "API key not configured. Please set the GEMINI_API_KEY environment variable manually.", fg="red"
            )
        )

    click.echo(
        "\nInstallation complete. You can now use the gemini-cli commands."
    )
    click.echo(
        click.style(
            "Get started by running 'gemini-cli --help' to see the available commands.",
            italic=True
        )
    )
