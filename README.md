
# Configurable Whisper Transcription Model (using 🍌)

This repo provides a server for the Whisper model, based on a banana template.

## Inputs

The server takes JSON configuration per request that controls the behavior of the model.

```json
{
  "get_segments": "true"
}
```

## Outputs

```json
{
  "segments": [
    {"start": 5.34, "end":  8.4, "text": "<segment text>"},
    {"start": 9.6, "end":  14.5, "text": "<segment text>"}
  ]
}
```
