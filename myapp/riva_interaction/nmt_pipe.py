import grpc
import queue

import myapp.riva_api.riva_nmt_pb2_grpc as rnmt_srv
import myapp.riva_api.riva_nmt_pb2 as rnmt

from config import riva_config, nmt_config

VERBOSE = True
SAMPLING_RATE = 16000
LANGUAGE_CODE = "zh-CN"
ENABLE_AUTOMATIC_PUNCTUATION = True
STREAM_INTERIM_RESULTS = True
SOURCE_LANGUAGE = "zh-CN"
TARGET_LANGUAGE = "en-US"


class NMTPipe:
    def __init__(self):
        self.verbose = nmt_config["VERBOSE"] if "VERBOSE" in nmt_config else VERBOSE
        self.sampling_rate = nmt_config["SAMPLING_RATE"] if "SAMPLING_RATE" in nmt_config else SAMPLING_RATE
        self.enable_automatic_punctuation = nmt_config["ENABLE_AUTOMATIC_PUNCTUATION"] if "ENABLE_AUTOMATIC_PUNCTUATION" in nmt_config else ENABLE_AUTOMATIC_PUNCTUATION
        self.stream_interim_results = nmt_config["STREAM_INTERIM_RESULTS"] if "STREAM_INTERIM_RESULTS" in nmt_config else STREAM_INTERIM_RESULTS
        self.source_language = nmt_config["SOURCE_LANGUAGE"] if "SOURCE_LANGUAGE" in nmt_config else SOURCE_LANGUAGE
        self.target_language = nmt_config["TARGET_LANGUAGE"] if "TARGET_LANGUAGE" in nmt_config else TARGET_LANGUAGE
        self.nmt_client = None
        self.channel = None
        self.transcript = ""
        self.request_generator = None
        self._translation = ""
        self._buff = queue.Queue()
        self.closed = False
        self.start()

    def start(self):
        if self.verbose:
            print('[Riva NMT] Creating Stream NMT channel: {}'.format(riva_config["RIVA_SPEECH_API_URL"]))
        self.channel = grpc.insecure_channel(riva_config["RIVA_SPEECH_API_URL"])
        self.nmt_client = rnmt_srv.RivaTranslationStub(self.channel)

    def set_transcript(self, transcript):
        self.transcript = transcript

    def set_translation(self, translation):
        self._translation = translation

    def get_final_translation(self):
        model_name = "megatronnmt_any_en_500m"
        req = rnmt.TranslateTextRequest(
            model=model_name,
            source_language=self.source_language,
            target_language=self.target_language,
            texts=[self._translation], #["欢大足球"]
        )
        resp = self.nmt_client.TranslateText(req)
        _, _, result = resp.translations[0].text.rpartition(':')
        yield result
