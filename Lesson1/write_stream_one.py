import streamlit as st
import numpy as np
import time as tt
import pandas as pd

bye_bye_bye = """I know that I can't take no more It ain't no lie
    I want to see you out that door
    Baby bye bye bye
    Don't want to be a fool for you
    Just another player in your game for two
    You may hate me but it ain't no lie
    Baby bye bye bye
    Bye bye
    Don't really want to make it tough
    I just want to tell you that I've had enough
    It might sound crazy but it ain't no lie
    Baby bye bye bye"""

def stream_data():
    for word in bye_bye_bye.split(" "):
        yield word + "  "
        tt.sleep(0.02)

if st.button("Stream Bye Bye Bye"):
    st.write_stream(stream_data)
    #Note, write-stream is just a generator with a typewriter effect

