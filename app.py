import requests
import tempfile
import whisper

BASE_SEGMENT_KEYS = ['start', 'end', 'text']


# Init runs on server startup
def init():
    global model
    model = whisper.load_model('medium')


# Inference runs for every server call
def inference(model_inputs: dict) -> dict:
    global model

    audio_file_url = model_inputs.get('url', None)
    if audio_file_url is None:
        return {'message': 'No input provided'}

    use_segments = model_inputs.get('getSegments', True)

    # Download the file and run the model
    try:
        response = requests.get(audio_file_url)
    except Exception as err:
        return {'message': f'Could not download audio file from: {audio_file_url}: {err!s}'}

    if response.status_code != 200:
        return {'message': f'Could not download audio file from: {audio_file_url}'}

    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(response.content)
        result = model.transcribe(tmp.name, max_initial_timestamp=86400)  # assume less than a day of audio

    output = {}
    if use_segments:
        segments = [{k: v for k, v in seg.items() if k in BASE_SEGMENT_KEYS} for seg in result.get('segments', [])]
        output['segments'] = segments
    else:
        output['text'] = result.get('text', '')

    output['getSegments'] = use_segments

    return output
