import streamlit as st
import transcription
from summarizer import Summarizer

st.set_page_config(
    page_title="Vonic",
    layout="wide",
)

st.header("Welcome to Vonic")

placeholder = st.empty()

with placeholder.container():
    vid = st.file_uploader(
            "Upload the Video",
            type=['mp4']
            )
summarizer = Summarizer(0.7)

if vid:
    tcrption = transcription.Transcription(
            vid, k=3
            )
    tcrption.process()
    with placeholder.container():
        c1, c2 = st.columns([2, 1])
        with c1:
            st.header("Video")
            st.video(vid, subtitles=tcrption.get_srt())
            st.download_button(
                'Get the srt file',
                tcrption.get_srt(),
                'text/srt',
                )
        with c2:
            st.header("Video Summary")
            with st.spinner("Summarizing the Video"):
                summary = summarizer.summ(tcrption.get_transcription())
            st.write(summary)
