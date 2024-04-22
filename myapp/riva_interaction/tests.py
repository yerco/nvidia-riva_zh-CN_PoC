import time

import myapp.riva_api.riva_asr_pb2 as rasr


def mock_request_generator():
    # Mock data simulating audio content; you might use simple strings or binary data depending on your use case
    mock_audio_contents = ["audio_data1", "audio_data2", "audio_data3", "audio_data4"]
    for audio_content in mock_audio_contents:
        yield audio_content
        time.sleep(1)  # Optional: simulate real-time audio data arrival


def continuous_mock_responses():
    mock_data = ['Hello', 'How are you?', 'This is a test', 'Thank you!', 'Another']
    while True:
        for data in mock_data:
            # Correctly nesting the response to match the protobuf definition
            response = rasr.StreamingRecognizeResponse(
                results=[rasr.StreamingRecognitionResult(
                    alternatives=[rasr.SpeechRecognitionAlternative(
                        transcript=data,
                        confidence=0.9  # Optional confidence value
                    )],
                    is_final=True
                )]
            )
            yield response
            time.sleep(3)  # Simulate delay