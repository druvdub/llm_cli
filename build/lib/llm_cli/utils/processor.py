from google.generativeai.types import GenerateContentResponse


def process_gemini_response(response: GenerateContentResponse, stream: bool = False) -> str:
    """
    Process the response from the Gemini API.
    """

    if not stream:
        return response.text  # return the text response
