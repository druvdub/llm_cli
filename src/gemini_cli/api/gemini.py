import os
from typing import Any, Iterable
import google.generativeai as genai
from google.generativeai.types import GenerateContentResponse, File
from dataclasses import dataclass, field


@dataclass
class Gemini:
    """A class to interact with the Gemini API."""
    api_key: str = field(init=False)

    def __post_init__(self):
        # validate if environment variable is set or exists or is not empty
        if "GOOGLE_API_KEY" in os.environ and os.environ["GOOGLE_API_KEY"]:
            self.api_key = os.environ["GOOGLE_API_KEY"]

        else:
            raise ValueError(
                "API key not found. Please set the GOOGLE_API_KEY environment variable or properly configure it using `gcli configure`.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def generate_content_from_text_prompt(self, prompt: str, stream_response: bool = False) -> GenerateContentResponse:
        """Generate content from a text prompt."""
        return self.model.generate_content(prompt, stream=stream_response)

    def generate_content_from_text_image_prompt(self, prompt: str, image_args: list[dict], stream_response: bool = False) -> GenerateContentResponse:
        """
            Generate content from a text prompt and supplied images.

            Supported image types are:
            - image/png
            - image/jpeg
            - image/webp
            - image/heif
            - image/heic
        """
        return self.model.generate_content([prompt, *image_args], stream=stream_response)

    def generate_content_from_text_and_file_prompt(self, prompt: str, file_args: Iterable[Any], stream_response: bool = False) -> GenerateContentResponse:
        """
            Generate content from a text prompt and uploaded files.

            Uses Files API to upload files and supports the following formats:

            - Images
            - Videos
            - Audio
        """
        return self.model.generate_content([prompt, *file_args], stream=stream_response)

    def fetch_files(self) -> Iterable[File]:
        """Get a list of uploaded files."""
        return genai.list_files()

    def delete_file(self, file_name: str):
        """
            Manually delete an uploaded file.

            Note: The API automatically deletes files after 48 hours as well.
        """
        genai.delete_file(file_name)

    def upload_files(self, files: list[str]) -> Iterable[File]:
        """Upload files to the API."""
        for file in files:
            yield self.upload_file(file)

    def upload_file(self, file: str) -> File:
        """Upload a file to the API."""
        return genai.upload_file(file)
