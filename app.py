import streamlit as st
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="పల్లె మాటలు", page_icon="🌾", layout="centered")
st.title("🌾 పల్లె మాటలు – తెలుగువారి సామెతల కోశం")
st.markdown("తెలంగాణ గ్రామీణుల మాటలు, సామెతలు, కథలు — మీరు చెప్పండి, మనం కాపాడుకుందాం!")

# File paths
DATA_FILE = "palle_matala_data.csv"
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Default entries (5 proverbs)
default_entries = [
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proverb": "అవ్వ చెప్పిన మాట అక్కిరాజు కంటే మేలు",
        "meaning": "వృద్ధుల అనుభవం పదిపుస్తకాలను మించినది.",
        "usage": "పెళ్లిళ్ల వ్యవహారాల్లో పెద్దల మాట వినడమే మేలు అంటారు.",
        "extra_story": "",
        "audio_path": ""
    },
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proverb": "పులి కనిపించక ముందే బల్లెం తెంపాడు",
        "meaning": "సమస్య రాకముందే పరిష్కారం వెతకడం.",
        "usage": "రాము ఎల్లప్పుడూ ముందే ప్లాన్ చేసుకుంటాడు.",
        "extra_story": "",
        "audio_path": ""
    },
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proverb": "ఎద్దు గడ్డి తింటుందో లేదో, పిట్ట గాలికి వణికింది",
        "meaning": "వచ్చే సమస్యకంటే ముందే భయపడటం.",
        "usage": "నీవెందుకు టెన్షన్ పడుతున్నావు?",
        "extra_story": "",
        "audio_path": ""
    },
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proverb": "వర్షం కురిస్తే, కప్ప మాత్రమే కాకుండా నంది కూడా ఆనందిస్తుంది",
        "meaning": "ఒక మంచి పని వల్ల అందరికీ ఉపయోగం.",
        "usage": "గ్రంథాలయం వల్ల ప్రతి విద్యార్థికి ఉపయోగం.",
        "extra_story": "",
        "audio_path": ""
    },
    {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proverb": "కోయిల కూస్తే కాలం మారింది",
        "meaning": "చుట్టూ పరిస్థితులు మారడం.",
        "usage": "ఇప్పుడు పిల్లలు కూడా పల్లె మాటలు నేర్చుకుంటున్నారు!",
        "extra_story": "",
        "audio_path": ""
    }
]

# Load or initialize data
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(default_entries)
    df.to_csv(DATA_FILE, index=False)
else:
    df = pd.read_csv(DATA_FILE)

# Show proverbs
st.subheader("📚 ఇప్పటికే సమర్పించిన పల్లె మాటలు")
for index, row in df[::-1].iterrows():
    st.markdown(f"### 🗣️ {row['proverb']}")
    st.markdown(f"**💡 అర్థం:** {row['meaning']}")
    st.markdown(f"**📘 ఉదాహరణ:** _{row['usage']}_")
    
    if pd.notna(row['extra_story']) and row['extra_story'].strip():
        st.markdown(f"**📖 ఇంకొక మాట లేదా కథ:** {row['extra_story']}")

    if pd.notna(row['audio_path']) and os.path.exists(row['audio_path']):
        st.audio(row['audio_path'])

    st.markdown("---")

# Ask user if they want to contribute
st.subheader("📥 మీరు కూడా చేర్చాలనుకుంటున్నారా?")
if st.checkbox("👍 అవును, నేను సామెత చేర్చాలనుకుంటున్నాను"):
    with st.form("submit_form"):
        st.subheader("📝 మీ సమాచారం సమర్పించండి")

        proverb = st.text_input("👉 సామెత / మాట")
        meaning = st.text_area("💡 అర్థం")
        usage = st.text_area("📘 ఉదాహరణ వాక్యం")

        extra_story = st.text_area("📖 మీరు చెప్పాలనుకునే మరో సామెత లేదా కథ (ఐచ్ఛికం)", placeholder="ఇక్కడ టైప్ చేయండి...")
        audio_file = st.file_uploader("🔊 ఉచ్ఛారణ ఫైల్ (ఐచ్ఛికం - .mp3 / .wav)", type=["mp3", "wav"])

        submitted = st.form_submit_button("✅ సమర్పించండి")

        if submitted:
            if proverb.strip() == "" or meaning.strip() == "" or usage.strip() == "":
                st.warning("దయచేసి సామెత, అర్థం మరియు ఉదాహరణ తప్పనిసరిగా నమోదు చేయండి.")
            else:
                # Save audio
                audio_filename = ""
                if audio_file is not None:
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    audio_filename = f"{UPLOAD_FOLDER}/{timestamp}_{audio_file.name}"
                    with open(audio_filename, "wb") as f:
                        f.write(audio_file.read())

                new_data = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "proverb": proverb,
                    "meaning": meaning,
                    "usage": usage,
                    "extra_story": extra_story,
                    "audio_path": audio_filename
                }

                df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success("🥳 మీరు పంపిన సమాచారం విజయవంతంగా నమోదు చేయబడింది!")
