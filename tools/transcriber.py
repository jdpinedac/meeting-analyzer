import os
import sys
import openai
import requests
from typing import Tuple
import torch

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") or sys.argv[1]

openai.api_key = OPENAI_API_KEY

# TODO: Function to check the installation of cuda and the gpu working

class AudioTranscription:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def transcribe_audio(self, audio_url: str) -> str:
        # Implement your Whisper ASR code here
        pass

# class ChatGPTSummary:
#     def __init__(self, api_key: str):
#         self.api_key = api_key

#     def generate_summary(self, text: str) -> Tuple[str, str]:
#         # Implement your ChatGPT summary and important points extraction here
#         pass

def main():
    audio_url = input("Enter the URL of the audio file: ")

    # Check if cuda is working.
    # TODO: Check what happenn if not.
    if torch.cuda.is_available():
        print("Working with CUDA")
    else
        print("Can't find CUDA Coprocessor")

    # Transcription
    # transcription = AudioTranscription(OPENAI_API_KEY)
    # transcribed_text = transcription.transcribe_audio(audio_url)
    # print("Transcribed text:", transcribed_text)

    # Summary and Important Points Extraction
    # chatgpt_summary = ChatGPTSummary(OPENAI_API_KEY)
    # summary, important_points = chatgpt_summary.generate_summary(transcribed_text)
    # print("\nSummary:", summary)
    # print("\nImportant Points:", important_points)


if __name__ == "__main__":
    main()
