from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/transcript")
def get_transcript(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {"video_id": video_id, "transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
