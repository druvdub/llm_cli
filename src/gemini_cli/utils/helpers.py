from dotenv import load_dotenv
import os


def write_dotenv(env: dict) -> None:
    """Write environment variables to a .env file."""
    with open(".env", "w") as file:
        for key, value in env.items():
            file.write(f"{key}={value}\n")


def load_env() -> None:
    """Load environment variables from a .env file."""
    load_dotenv()


def verify_env(env_vars: list[str]):
    """Verify that required environment variables are set."""
    for var in env_vars:
        if var not in os.environ:
            raise ValueError(
                f"Environment variable {var} not found. Please set it using `gcli configure`.")
