import grpc
import myapp.riva_api.riva_audio_pb2 as ra
import myapp.riva_api.riva_tts_pb2 as rtts
import myapp.riva_api.riva_tts_pb2_grpc as rtts_srv
import queue
from config import riva_config, tts_config
import numpy as np

VERBOSE = False
SAMPLE_RATE = 22050
LANGUAGE_CODE = "en-US"
VOICE_NAME = "English-US.Female-1"


class TTSPipe(object):
    """Opens a gRPC channel to Riva TTS to synthesize speech
    from text in batch mode."""

    def __init__(self):
        self.verbose = tts_config["VERBOSE"] if "VERBOSE" in tts_config else VERBOSE
        self.sample_rate = tts_config["SAMPLE_RATE"] if "SAMPLE_RATE" in tts_config else SAMPLE_RATE
        self.language_code = tts_config["LANGUAGE_CODE"] if "LANGUAGE_CODE" in tts_config else LANGUAGE_CODE
        self.voice_name = tts_config["VOICE_NAME"] if "VOICE_NAME" in tts_config else VOICE_NAME
        self.audio_encoding = ra.AudioEncoding.LINEAR_PCM
        self._buff = queue.Queue()
        self.closed = False
        self._flusher = bytes(np.zeros(dtype=np.int16, shape=(self.sample_rate, 1)))  # Silence audio
        self.current_tts_duration = 0
        self.transcript = ""
        self.channel = None
        self.tts_client = None

    def set_transcript(self, transcript):
        self.transcript = transcript

    def get_transcript(self):
        return self.transcript

    def start(self):
        if self.verbose:
            print('[Riva TTS] Creating Stream TTS channel: {}'.format(riva_config["RIVA_SPEECH_API_URL"]))
        self.channel = grpc.insecure_channel(riva_config["RIVA_SPEECH_API_URL"])
        self.tts_client = rtts_srv.RivaSpeechSynthesisStub(self.channel)

    def fill_buffer(self, in_data):
        """To collect text responses from the state machine output, into a buffer."""
        if len(in_data):
            self._buff.put(in_data)

    def close(self):
        self.closed = True
        self._buff.queue.clear()
        self._buff.put(None) # means the end
        del self.channel

    def get_speech(self):
        """Returns speech audio from text responses in the buffer"""
        self.start()
        wav_header = self.gen_wav_header(self.sample_rate, 16, 1, 0)
        yield bytes(wav_header)
        # Hardcoded text for testing
        #test_text = "男人非常喜欢大足球但是中国部队,马马虎虎"
        test_text = self.transcript

        # Simulate creating a TTS request as if text was received
        req = rtts.SynthesizeSpeechRequest()
        req.text = test_text  # Use the hardcoded test text
        req.language_code = self.language_code
        req.encoding = self.audio_encoding
        req.sample_rate_hz = self.sample_rate
        req.voice_name = self.voice_name
        resp = self.tts_client.Synthesize(req)

        # Process response and yield audio
        datalen = len(resp.audio) // 2
        data16 = np.ndarray(buffer=resp.audio, dtype=np.int16, shape=(datalen, 1))
        yield bytes(data16.data)

    def gen_wav_header(self, sample_rate, bits_per_sample, channels, datasize):
        o = bytes("RIFF", 'ascii')  # (4byte) Marks file as RIFF
        o += (datasize + 36).to_bytes(4, 'little')  # (4byte) File size in bytes excluding this and RIFF marker
        o += bytes("WAVE", 'ascii')  # (4byte) File type
        o += bytes("fmt ", 'ascii')  # (4byte) Format Chunk Marker
        o += (16).to_bytes(4, 'little')  # (4byte) Length of above format data
        o += (1).to_bytes(2, 'little')  # (2byte) Format type (1 - PCM)
        o += channels.to_bytes(2, 'little')  # (2byte)
        o += sample_rate.to_bytes(4, 'little')  # (4byte)
        o += (sample_rate * channels * bits_per_sample // 8).to_bytes(4, 'little')  # (4byte)
        o += (channels * bits_per_sample // 8).to_bytes(2, 'little')  # (2byte)
        o += bits_per_sample.to_bytes(2, 'little')  # (2byte)
        o += bytes("data", 'ascii')  # (4byte) Data Chunk Marker
        o += datasize.to_bytes(4, 'little')  # (4byte) Data size in bytes
        return o