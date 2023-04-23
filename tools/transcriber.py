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


def transcribe_audio(audio_f):
    """
    Transcribe an audio file to text using the Whisper API from OpenAI.

    Args:
        audio_file (str): The path to the audio file that needs to be
        transcribed.

    Returns:
        str: The transcribed text.
    """
    model = whisper.load_model("medium")
    result = model.transcribe(audio_f)
    return result["text"]


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
    output = f"Transcript:\n{audio_text}\n"
    print(output)
    return


if __name__ == "__main__":
    main()
