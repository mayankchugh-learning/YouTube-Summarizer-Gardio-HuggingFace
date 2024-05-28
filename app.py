# Use a pipeline as a high-level helper
from transformers import pipeline

# youtube_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

model_path = "Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"

youtube_summarizer = pipeline("summarization", model=model_path)
