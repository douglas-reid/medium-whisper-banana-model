# In this file, we define download_model
# It runs during container build time to stage the model into the container

import whisper


def download_models():
    whisper.load_model('medium')


if __name__ == "__main__":
    download_models()
