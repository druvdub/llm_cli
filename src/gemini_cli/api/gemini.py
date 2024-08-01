import os
import google.generativeai as genai
from dataclasses import dataclass


@dataclass
class Gemini:
    """A class to interact with the Gemini API."""
    api_key = None

    def __post_init__(self):
        # validate if environment variable is set or exists or is not empty
        if "GOOGLE_API_KEY" in os.environ and os.environ["GOOGLE_API_KEY"]:
            self.api_key = os.environ["GOOGLE_API_KEY"]

        else:
            raise ValueError(
                "API key not found. Please set the GOOGLE_API_KEY environment variable.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')
