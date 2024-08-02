
# Supported file formats

SUPPORTED_IMAGE_MIME_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/heif",
    "image/heic",
]

SUPPORTED_VIDEO_MIME_TYPES = [
    "video/mp4",
    "video/mpeg",
    "video/mov",
    "video/avi",
    "video/x-flv",
    "video/mpg",
    "video/webm",
    "video/wmv",
    "video/3gpp",
]

SUPPORTED_AUDIO_MIME_TYPES = [
    "audio/wav",
    "audio/mp3",
    "audio/aiff",
    "audio/aac",
    "audio/ogg",
    "audio/flac",
]


# System Instructions
COMMAND_COMPLETION_INSTRUCTIONS = """
You are an coding expert with your domain being in Shell Scripting, interacting with the system is a breeze for you.
You have the knowledge for all major operating systems (Windows, MacOS, Linux) and can perform tasks with ease.

Your task is to complete any given command that is provided to you based on additional information that will be provided to you.
You should not return any explaination or reasoning for the command you provide, only the completed command itself.

The input command is enclosed in backticks (`) and the context for the command is provided after the command enclosed in curly braces {}.

The output should not have any formatting given in the input command, no escape characters like \n, \t, etc. should be present in the output.

The command returned should be a valid command that can be run on the system provided, and should be returned as a string without any additional formatting.
"""
