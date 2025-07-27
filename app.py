import streamlit as st
import os
import json
from datetime import datetime

st.set_page_config(page_title="పల్లె మాటలు", page_icon="🌾", layout="centered")

DATA_FILE = "data.json"
UPLOAD_FOLDER = "uploads"

# Create upload folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------- JSON Backend Functions ----------
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# ---------- Optional: Add Default Data ----------
if not os.path.exists(DATA_FILE):
    default_data = [
        {
            "type": "సామెతలు",
            "content": "పుట్టగొడుగుల వర్షం",
            "meaning": "ఒకేసారి చాలా వస్తే ఇలా అంటారు",
            "audio_path": ""
        },
        {
            "type": "సామెతలు",
            "content": "గడ్డపరిచిన పామును చూసి చీమ కూడా కొరుకుతుంది",
            "meaning": "శక్తిని కోల్పోయిన వారిని అందరూ తక్కువ చేస్తారు",
            "audio_path": ""
        },
        {
            "type": "సామెతలు",
            "content": "నిన్ను నువ్వే పొగుడుకోకపోతే మరెవరు పొగుడతారు",
            "meaning": "తానేం చేసినా తానే పొగడుకోవాలి",
            "audio_path": ""
        },
        {
            "type": "పొడుపుకథలు",
            "content": "రెండు కన్నులున్నా చూడలేని పాపం?",
            "meaning": "కత్తెర",
            "audio_path": ""
        },
        {
            "type": "పొడుపుకథలు",
            "content": "నడిచే పాపా – తల నెత్తిన పాలు",
            "meaning": "చిన్న వయసులో పెద్ద బాధ్యతలు తీసుకునే వారు",
            "audio_path": ""
        }
    ]
    save_data(default_data)

# ---------- UI Starts ----------
st.title("🌾 పల్లె మాటలు")
st.markdown("### 🙏 నమస్తే తెలంగాణ ప్రజలారా! మన ఊరి మాటలూ, తెలివి మాటలూ చెరిపిపోకుండా దిద్దుకుందాం!")

# ---------- Category Selection ----------
st.subheader("📂 ఏది చూడాలని ఉంది?")
category = st.radio("కేటగిరీని ఎంచుకోండి:", ["సామెతలు", "పొడుపుకథలు"])

data = load_data()
filtered = [item for item in data if item["type"] == category]

# ---------- Show Proverbs or Riddles ----------
if filtered:
    for item in filtered[::-1]:
        st.markdown(f"### 📝 {item['content']}")
        st.markdown(f"**అర్థం:** {item['meaning']}")
        if item["audio_path"]:
            st.audio(item["audio_path"])
        st.markdown("---")
else:
    st.info("ఈ కేటగిరీలో ఇంకా ఎంట్రీలు లేవు.")

# ---------- Submission Section ----------
st.markdown("## ✍️ మీకు తెలుసా ఇంకో మంచి సామెత లేదా పొడుపుకథ?")
with st.expander("➕ కొత్తదాన్ని జోడించండి"):
    new_type = st.selectbox("వర్గం ఎంచుకోండి:", ["సామెతలు", "పొడుపుకథలు"])
    new_content = st.text_input("మీ సామెత లేదా పొడుపుకథ:")
    new_meaning = st.text_area("అర్థం తెలుగులో:")
    new_audio = st.file_uploader("ఒకవేళ ఆడియో ఉందా? (ఐచ్ఛికం)", type=["mp3", "wav", "m4a"])

    if st.button("జమచేయి"):
        if new_content.strip() and new_meaning.strip():
            audio_path = ""
            if new_audio:
                filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{new_audio.name}"
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                with open(filepath, "wb") as f:
                    f.write(new_audio.read())
                audio_path = filepath

            new_entry = {
                "type": new_type,
                "content": new_content.strip(),
                "meaning": new_meaning.strip(),
                "audio_path": audio_path
            }

            data.append(new_entry)
            save_data(data)
            st.success("👌 జమ అయింది! మీరు తెలంగాణ సంస్కృతికి తోడ్పడుతున్నారు.")
        else:
            st.warning("దయచేసి అన్ని వివరాలు పూరించండి.")
