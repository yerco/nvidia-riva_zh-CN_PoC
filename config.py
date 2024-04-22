riva_config = {
    "RIVA_SPEECH_API_URL": "127.0.0.1:50051",
    "VERBOSE": True
}

asr_config = {
    "VERBOSE": True,
    "SAMPLING_RATE": 16000,
    "LANGUAGE_CODE": "zh-CN",
    "ENABLE_AUTOMATIC_PUNCTUATION": True,
}

tts_config = {
    "VERBOSE": False,
    "SAMPLE_RATE": 22050,
    "LANGUAGE_CODE": "zh-CN",
    "VOICE_NAME": "Mandarin-CN.Female-1",
}

nmt_config = {
    "SOURCE_LANGUAGE": "zh-CN",
    "TARGET_LANGUAGE": "en-US",
    "SAMPLING_RATE": 16000,
    "VERBOSE": True
}
