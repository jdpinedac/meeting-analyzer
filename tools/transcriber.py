#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meeting Analyzer: Audio to Text Transcription and Analysis using
Whisper and ChatGPT APIs with NVIDIA Acceleration.

This script allows users to transcribe audio to text and extract
relevant information using the Whisper and ChatGPT APIs from OpenAI.

The script prompts the user to provide the path to the audio file they
wish to transcribe and analyze. The audio file is then processed using
the Whisper API to transcribe it to text, which is then analyzed using
the ChatGPT API to extract relevant information. If a NVIDIA GPU with
CUDA support is available, the processing time can be accelerated.

Usage:
    $ python main.py <path/to/audio_file>

Args:
    audio_file (str): The path to the audio file that needs to be
    transcribed and analyzed.

Returns:
    The transcript of the audio file and any relevant information extracted
    using the ChatGPT API.

Requirements:
    - Python 3.x
    - NVIDIA GPU with CUDA support
    - NVIDIA cuDNN library
    - Whisper API key
    - ChatGPT API key
"""

import os
import argparse
import torch
import whisper

# import sys
# import openai
# import requests
# from typing import Tuple

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or sys.argv[1]

# openai.api_key = OPENAI_API_KEY

# class AudioTranscription:
#     def __init__(self, api_key: str):
#         self.api_key = api_key

#     def transcribe_audio(self, audio_url: str) -> str:
#         # Implement your Whisper ASR code here
#         pass


def transcribe_audio(audio_f):
    """
    Transcribe an audio file to text using the Whisper API from OpenAI.

    Args:
        audio_file (str): The path to the audio file that needs to be
        transcribed.

    Returns:
        str: The transcribed text.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_f)
    return result["text"]


# class ChatGPTSummary:
#     def __init__(self, api_key: str):
#         self.api_key = api_key

#     def generate_summary(self, text: str) -> Tuple[str, str]:
#         # Implement your ChatGPT summary and important points extraction here
#         pass

def main():
    """
    Transcribe audio to text and extract relevant information
    using the Whisper and ChatGPT APIs from OpenAI.

    Args:
        audio_file (str): The path to the audio file that needs
        to be transcribed and analyzed.

    Returns:
        str: The transcript of the audio file and any relevant
        information extracted using the ChatGPT API.

    Requirements:
        - Python 3.x
        - NVIDIA GPU with CUDA support
        - NVIDIA cuDNN library
        - Whisper API key
        - ChatGPT API key
    """
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        print(f"Number of available GPUs: {device_count}")
        print(f"Device Name: {torch.cuda.get_device_name(device_count-1)}")
    else:
        print("Can't find CUDA Coprocessor")

    parser = argparse.ArgumentParser(description='Transcribe audio and \
        extract information.')
    parser.add_argument('audio_file', type=str, help='The path to the \
        audio file that needs to be transcribed and analyzed.')
    args = parser.parse_args()

    audio_file = args.audio_file

    # Check if audio file exists
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file '{audio_file}' not found.")

    # Load audio file and transcribe to text using the Whisper API
    audio_text = transcribe_audio(audio_file)
    output = f"Transcript:\n{audio_text}\n\n"
    print(output)

    # Transcription
    # transcription = AudioTranscription()
    # transcribed_text = transcription.transcribe_audio(audio_url)
    # print("Transcribed text:", transcribed_text)

    # Analyze audio text using the ChatGPT API
    # audio_analysis = analyze_text(audio_text)

    # Format output
    # output = f"Transcript:\n{audio_text}\n\n \
    #     Analysis:\n{audio_analysis}"

    return output

    # Summary and Important Points Extraction
    # chatgpt_summary = ChatGPTSummary(OPENAI_API_KEY)
    # summary, important_points = chatgpt_summary.generate_summary
    #   (transcribed_text)
    # print("\nSummary:", summary)
    # print("\nImportant Points:", important_points)

    # # Load audio file and transcribe to text using the Whisper API
    # audio_text = transcribe_audio(audio_file)

    # # Analyze audio text using the ChatGPT API
    # audio_analysis = analyze_text(audio_text)

    # # Format output
    # output = f"Transcript:\n{audio_text}\n\nAnalysis:\n{audio_analysis}"

    # return output


if __name__ == "__main__":
    main()
