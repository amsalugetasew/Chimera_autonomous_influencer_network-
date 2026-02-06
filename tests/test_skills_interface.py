# def test_skill_input_contract():
#     skill_input = {"platform": "tiktok", "region": "us"}
#     assert "platform" in skill_input
#     assert "region" in skill_input
import pytest

from skills import skill_download_youtube, skill_transcribe_audio

def test_download_youtube_interface():
    with pytest.raises(NotImplementedError):
        skill_download_youtube.download("https://youtube.com/sample")

def test_transcribe_audio_interface():
    with pytest.raises(NotImplementedError):
        skill_transcribe_audio.transcribe("sample_audio.mp3")
