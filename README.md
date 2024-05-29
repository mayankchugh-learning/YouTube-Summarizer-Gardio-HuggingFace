# YouTube-Summarizer-Gardio-HuggingFace

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p youtubesummarizerenv python -y
```

```bash
source activate ./youtubesummarizerenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```

##### after download move the model to code folder
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--sshleifer--distilbart-cn
n-12-6 /Users/mayankchugh/gitRepos/mayankchugh.learning/HuggingFace-ML-GenerativeAI-Gradio-Streamlit-Apps/TextSummarizer-Gradio/models--sshleifer--distilbart-cnn-12-6

```bash
Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff
```

```

## Prompt
```bash
Write Python code that inputs a YouTube URL and outputs the video's transcript using youtube_transcript_api.
```
```bash
@GPT-4o Write a Python code that would take a youtube URL as input and give the video transcript as output. also include gradio UI and use hugging face model "sshleifer/distilbart-cnn-12-6"
```