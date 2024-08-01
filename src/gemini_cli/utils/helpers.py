from dotenv import load_dotenv
import os
from gemini_cli import __version__
from .constants import SUPPORTED_IMAGE_MIME_TYPES, SUPPORTED_VIDEO_MIME_TYPES, SUPPORTED_AUDIO_MIME_TYPES


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


def version_() -> str:
    """Get the version of the gemini-cli package."""
    return f"gemini-cli v{__version__}"


def validate_image_type(image_path: str) -> bool:
    """Validate if the image type is supported."""
    mime_type = extract_mime_type(image_path)
    return mime_type in SUPPORTED_IMAGE_MIME_TYPES


def validate_video_type(video_path: str) -> bool:
    """Validate if the video type is supported."""
    mime_type = extract_mime_type(video_path, format="video")
    return mime_type in SUPPORTED_VIDEO_MIME_TYPES


def validate_audio_type(audio_path: str) -> bool:
    """Validate if the audio type is supported."""
    mime_type = extract_mime_type(audio_path, format="audio")
    return mime_type in SUPPORTED_AUDIO_MIME_TYPES


def extract_mime_type(path: str, format: str = "image") -> str:
    """Extract the MIME type of an file (image/audio/video)."""
    extension = path.split(".")[-1]

    return f"{format}/{extension}"
