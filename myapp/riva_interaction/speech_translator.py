from myapp.riva_interaction.asr_pipe import ASRPipe
from myapp.riva_interaction.tts_pipe import TTSPipe
from myapp.riva_interaction.nmt_pipe import NMTPipe


class SpeechTranslator:

    def __init__(self, user_conversation_index, verbose=True):
        self.thread_asr = None
        self.thread_nmt = None
        self.id = user_conversation_index
        self.asr = ASRPipe()
        self.tts = TTSPipe()
        self.nmt = NMTPipe()
        self.enableTTS = False
        self.pause_asr_flag = False
        self.verbose = verbose
        self.transcript_data = ""

    def get_tts(self):
        return self.tts

    def get_asr(self):
        return self.asr

    def get_nmt(self):
        return self.nmt

    def server_asr(self):
        self.asr.start()
        if self.verbose:
            print(f'[{self.id }] Starting speech translator ASR task')
        self.asr.main_asr()

    def empty_asr_buffer(self):
        self.asr.empty_asr_buffer()
        if self.verbose:
            print(f'[{self.id }] ASR buffer cleared')
    
    def start_asr(self, sio):
        self.thread_asr = sio.start_background_task(self.server_asr)
        if self.verbose:
            print(f'[{self.id }] ASR background task started')

    def wait(self):
        self.thread_asr.join()
        if self.verbose:
            print(f'[{self.id }] ASR background task terminated')
    
    def asr_fill_buffer(self, audio_in):
        if not self.pause_asr_flag:
            self.asr.fill_buffer(audio_in)
    
    def get_asr_transcript(self):
        return self.asr.get_transcript()
    
    def start_tts(self):
        self.enableTTS = True
        if self.verbose:
            print(f'[{self.id }] TTS Enabled')

    def get_tts_speech(self):
        return self.tts.get_speech()

    def get_nmt_final_translation(self):
        return self.nmt.get_final_translation()
