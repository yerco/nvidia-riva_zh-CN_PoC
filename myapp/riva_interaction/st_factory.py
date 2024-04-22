from myapp.riva_interaction.speech_translator import SpeechTranslator

sts = {}
user_conversation_cnt = 0


def create_st(instance_index, sio, verbose=False):
    if instance_index not in sts:
        sts[instance_index] = SpeechTranslator(instance_index,
                                               verbose=verbose)
        sts[instance_index].start_asr(sio)
        if verbose:
            print(f'[Riva ST] Speech Translator created with as instance: [{instance_index}]')


def get_st(instance_index):
    if instance_index in sts:
        return sts[instance_index]
    else:
        return None
