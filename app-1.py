# Use a pipeline as a high-level helper
from transformers import pipeline
#import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi
import gradio as gr

# youtube_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

model_path = "Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"

youtube_summarizer = pipeline("summarization", model=model_path)


def get_video_transcript(video_url):
    """
    Retrieves the transcript for a YouTube video given the video URL.

    Args:
        video_url (str): The URL of the YouTube video.

    Returns:
        str: The transcript of the video.
    """
    # Extract the video ID from the URL
    video_id = re.search(r'v=([^&]+)', video_url).group(1)

    try:
        # Fetch the video transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Concatenate the transcript text
        transcript_text = ' '.join([entry['text'] for entry in transcript])

        # Split the transcript into chunks within the maximum sequence length
        max_seq_length = 1024
        transcript_chunks = [transcript_text[i:i+max_seq_length] for i in range(0, len(transcript_text), max_seq_length)]

        return transcript_chunks
    except Exception as e:
        return ["Error retrieving the transcript: " + str(e)]

#if __name__ == '__main__':

#    video_url = input("Enter the YouTube video URL: ")
#    transcript = get_video_transcript(video_url)
#    print(transcript)
#    print(youtube_summarizer(transcript))


gr.close_all()

# Create a Gradio interface
iface = gr.Interface(
    fn=get_video_transcript,
    inputs="text",
    outputs="text",
    title="@IT AI Enthusiast (Mayank Chugh) (https://www.youtube.com/@itaienthusiast/) - Project 2: YouTube Video Transcript Generator",
    description="Enter a YouTube URL to generate and summarize the video transcript.",
    concurrency_limit=8
)

# Launch the Gradio interface
iface.launch(share=False)