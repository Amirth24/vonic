import streamlit as st
import tempfile
import ffmpeg
import librosa
from functools import lru_cache
from time import gmtime, strftime
# Load model directly
from transformers import WhisperProcessor, WhisperForConditionalGeneration


processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
model = WhisperForConditionalGeneration.from_pretrained(
        "openai/whisper-tiny").to("cuda")


class Transcription:
    def __init__(self, vid, k, ep=0.09):
        self.transcription = []
        self.vid = vid
        self.k = k
        self.ep = ep

    @lru_cache(maxsize=None)
    def process(self):
        if len(self.transcription) != 0:
            return
        with st.spinner('Preprocessing the Video'):
            with tempfile.NamedTemporaryFile() as tmp:
                tmp.write(self.vid.read())

                with tempfile.NamedTemporaryFile() as audtmp:
                    (
                        ffmpeg
                        .input(tmp.name)
                        .output(
                            audtmp.name,
                            sample_rate=16000,
                            format="flac",
                            acodec='flac')
                        .overwrite_output()
                        .run())

                    aud, sr = librosa.load(
                            audtmp.name, sr=16000)
        aud_frames = librosa.util.frame(
            aud,
            frame_length=int((self.k+self.ep)*16000),
            hop_length=int((self.k-self.ep)*16000),
            axis=-1
        ).T

        def stamp_time(x):
            return strftime("%H:%M:%S", gmtime(x*self.k))

        gen_cap_bar = st.progress(0, text="Generating Captions")
        for i, frame in enumerate(aud_frames):
            inp = processor(
                [frame],
                sampling_rate=sr,
                return_tensors="pt"
            ).input_features.to("cuda")
            generated_ids = model.generate(
                inp
            )
            text = ''.join(
                processor.batch_decode(generated_ids, skip_special_tokens=True)
            )
            self.transcription.append(
                    (i, stamp_time(i), stamp_time(i+1), text)
                    )
            percent = i/len(aud_frames)
            gen_cap_bar.progress(
                percent,
                text=f"Transcription Generation {int(100*percent)}% Completed")
        gen_cap_bar.empty()

    @lru_cache(maxsize=None)
    def get_srt(self):
        return '\n\n'.join(list(map(
            lambda v: f"{v[0]+1}\n{v[1]},000 --> {v[2]},000\n{v[3].strip()}",
            self.transcription
            )))

    @lru_cache(maxsize=None)
    def get_transcription(self):
        return ' '.join(list(map(lambda z: z[-1], self.transcription)))
