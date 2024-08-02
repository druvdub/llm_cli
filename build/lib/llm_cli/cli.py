import click

from llm_cli import __version__
from llm_cli.api.gemini import Gemini
from llm_cli.utils.constants import COMMAND_COMPLETION_INSTRUCTIONS
from llm_cli.utils.helpers import peek, version_, load_env, verify_env, write_dotenv, format_file_info
from llm_cli.utils.processor import process_gemini_response


load_env()


@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Get the version of the llm-cli package.")
@click.pass_context
def cli(ctx, version):
    """A CLI tool for interacting with the Gemini API.
    can be invoked with 'lcli' or 'llm-cli'.

    Examples: $ lcli --version
    """
    if version:
        click.echo(version_())
    elif ctx.invoked_subcommand is None:
        click.echo("" + ctx.get_help())


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

                env_map = {"GOOGLE_API_KEY": api_key}
                write_dotenv(env_map)

                click.echo(
                    click.style(
                        "\nAPI key has been set successfully.", fg="green")
                )

                click.echo(
                    "\nInstallation complete. You can now use the llm-cli commands."
                )

            else:
                click.echo(
                    click.style(
                        "API key not configured. Please set the GOOGLE_API_KEY environment variable manually.", fg="red"
                    )
                )
        else:
            env_map = {"GOOGLE_API_KEY": api_key}
            write_dotenv(env_map)
            click.echo(
                click.style("\nAPI key has been set successfully.", fg="green")
            )

            click.echo(
                "\nInstallation complete. You can now use the llm-cli commands. Please ensure that the API key is correct."
            )

        click.echo(
            click.style(
                "Get started by running 'lcli --help' to see the available commands.\n",
                bold=True
            )
        )

    except Exception as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )


@cli.command('verify', help="Check if the API key is set.")
def verify():
    try:
        verify_env(["GOOGLE_API_KEY"])
        click.echo(
            click.style(
                "API key found. You are ready to use the API.", fg="green")
        )
    except ValueError as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )


@cli.command("prompt")
@click.option("--text", "-t", help="Text prompt to interact with Gemini")
@click.option("--image", "-i", multiple=True, help="Image path to upload to Gemini. Can upload multiple images")
@click.option("--file", "-f", multiple=True, help="File path to upload to Gemini. Can upload multiple files. Images, Videos, Audio, Documents. Files are stored upto 48 hours before being deleted automatically. Uses files API", type=click.Path(exists=True))
@click.option("--stream", "-s", is_flag=True, default=False, help="Get the response in chunks.")
@click.pass_context
def prompt(ctx, text, image, file, stream):
    """Generate content from a prompt and/or other files."""
    if not (text or image or file):
        click.echo(
            click.style(
                "Please provide atleast one of the following options: --text, --image, --file.", fg="bright_red", )
        )
        click.echo(ctx.get_help())
    else:
        try:
            gemini = Gemini()

            if text:
                response = gemini.generate_content_from_text_prompt(text)

                result = process_gemini_response(response)

                click.echo(
                    click.style(
                        f"\n{result}", fg="bright_blue"
                    )
                )

        except ValueError as e:
            click.echo(
                click.style(f"An error occurred: {str(e)}", fg="red")
            )


@cli.command("chat")
@click.option("--start", "-s", is_flag=True, help="Start a chat session with Gemini.")
def chat(start):
    """Start a chat session with Gemini."""
    try:
        gemini = Gemini()
        if start:
            click.echo(
                click.style(
                    "Starting chat session with Gemini...", fg="bright_blue"
                )
            )

            while True:
                message = click.prompt(
                    click.style("You"), prompt_suffix=": ")

                response = gemini.send_chat_message(message)

                result = process_gemini_response(response)

                click.echo(
                    click.style(
                        f"Gemini: {result}", fg="bright_blue"
                    )
                )

    except click.Abort:
        click.echo(
            click.style("\nChat session ended.", fg="bright_yellow")
        )

    except Exception as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )


@cli.command("files")
@click.option("--list", "-l", is_flag=True, help="List all files uploaded to Gemini.")
@click.option("--upload", "-u", help="Upload a file to Gemini by providing the file path and a display name in that order", nargs=2, type=(click.Path(exists=True), str))
@click.option("--delete", "-d", help="Delete a file from Gemini by providing the file name.")
@click.option("--fetch", "-f", help="Fetch a file from Gemini by providing the file display name.")
def files(list, upload, delete, fetch):
    """Basic file management commands for Gemini."""
    try:
        gemini = Gemini()

        if list:
            response = gemini.list_files()

            file = peek(response)

            if file:
                click.echo(
                    f"Display Name\t - \tMime Type\t - \tByte Size\t - \tURI"
                )

                for f in file[1]:
                    click.echo(
                        click.style(
                            f"\n{format_file_info(f)}", fg="magenta"
                        )
                    )
            else:
                click.echo(
                    click.style(
                        "No files found.", fg="bright_yellow"
                    )
                )

        if upload:
            response = gemini.upload_file(upload[0], display_name=upload[1])

            click.echo(
                click.style(
                    f"Uploaded file: {response.display_name} with {response.uri}", fg="bright_blue"
                )
            )

        if delete:
            # confirm deletion
            if click.confirm(f"Are you sure you want to delete file with display name" + click.style(f" {delete}", fg="green", blink=True) + "?", default=True, prompt_suffix=": "):
                try:
                    file = gemini.get_file(delete)
                except ValueError as e:
                    click.echo(
                        click.style(f"An error occurred: {str(e)}", fg="red")
                    )
                    return

                gemini.delete_file(file.display_name)

                click.echo(
                    click.style(
                        f"Deleted file: {file.name} with display name: {file.display_name}", fg="bright_blue"
                    )
                )

        if fetch:
            try:

                file = gemini.get_file(fetch)

                click.echo(
                    click.style(
                        f"{file}", fg="magenta"
                    )
                )
            except:
                click.echo(
                    click.style(
                        f"File not found or you may not have permissions to access it", fg="bright_yellow"
                    )
                )
    except click.ClickException as e:
        click.echo(
            click.style(f"Interrupted by user: {str(e)}", fg="red")
        )

    except Exception as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )


@cli.command("completion")
@click.option("--command", "-c", help="Input command to complete.", required=True)
@click.option("--context", "-ctx", help="Context for the command.", required=True)
def completion(command, context):
    """Complete a command based on the context provided."""
    try:
        gemini = Gemini(system_instruction=COMMAND_COMPLETION_INSTRUCTIONS)

        response = gemini.generate_content_from_text_prompt(
            f"`{command}` {{{context}}}"
        )

        text = process_gemini_response(response)

        click.echo(
            click.style(
                f"\n{text}", fg="bright_blue"
            )
        )

    except ValueError as e:
        click.echo(
            click.style(f"An error occurred: {str(e)}", fg="red")
        )
