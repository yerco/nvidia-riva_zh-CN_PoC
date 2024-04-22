import json
import queue
import time

from flask import stream_with_context, Response

from . import bp
from myapp import socketio
from myapp.riva_interaction.st_factory import get_st

audio_queue = queue.Queue()


# debugging
@bp.route('/events')
def send_events():
    def event_generator():
        while True:
            time.sleep(3)  # an event 3 second
            yield f"data: {json.dumps({'time': time.time(), 'msg': 'Hello world!'})}\n\n"

    return Response(event_generator(), mimetype='text/event-stream')


# Handles ASR audio transcript output
@bp.route('/stream/<int:instance_number>')
def stream(instance_number):
    @stream_with_context
    def audio_stream():
        speech_translator = get_st(1)
        if speech_translator:
            asr_transcript = speech_translator.get_asr_transcript()
            for transcript in asr_transcript:
                yield transcript
                tts = speech_translator.get_tts()
                tts.set_transcript(transcript)
                nmt = speech_translator.get_nmt()
                nmt.set_translation(transcript)
    return Response(audio_stream(), mimetype="text/event-stream")


@bp.route('/audio')
def audio():
    speech_translator = get_st(1)
    if speech_translator:
        return Response(speech_translator.get_tts_speech())
    else:
        return Response("No speech_translator found")


@bp.route('/translation')
def translation():
    speech_translator = get_st(1)
    if speech_translator:
        def generate():
            while True:
                _translation = speech_translator.get_nmt_final_translation()
                for y in _translation:
                    yield f"data: {y}\n\n"
                time.sleep(1)
        return Response(stream_with_context(generate()), content_type='text/event-stream')
    else:
        return Response("No speech translator found", content_type='text/plain')


@socketio.on('connect')
def test_connect():
    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('audioIn')
def handle_stream(audio_data):
    speech_translator = get_st(1)
    if speech_translator:
        speech_translator.asr_fill_buffer(audio_data["data"])


@socketio.on('start_tts', namespace='/')
def start_tts(data):
    print("Start TTS")
    speech_translator = get_st(1)
    if speech_translator:
        speech_translator.start_tts()

# @socketio.on('audioStop')
# def handle_stop_stream(data):
#     print("STOPPING STREAM")
#     do something here
