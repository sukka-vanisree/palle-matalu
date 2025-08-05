import streamlit as st
import os

# Set tab name and icon
st.set_page_config(page_title="పల్లె మాటలు", page_icon="🌾", layout="wide")

# Initialize session state
for key in ["page", "name", "place", "type", "answer", "feedback_given"]:
    if key not in st.session_state:
        st.session_state[key] = ""

if "page_number" not in st.session_state:
    st.session_state.page_number = 0

# Helper to go pages
def next_page():
    st.session_state.page_number += 1

def prev_page():
    if st.session_state.page_number > 0:
        st.session_state.page_number -= 1

# Background layout with side image
def side_by_side_image(image_path):
    col1, col2 = st.columns([1, 2])
    with col1:
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.warning(f"చిత్రాన్ని లొకేట్ చేయలేకపోయాం: {image_path}")
    return col2

# Pages
def welcome_page():
    col = side_by_side_image("front_image.jpg")
    with col:
        st.markdown("<h1 style='color:#4a148c;'>🌾 పల్లె మాటలు 🌾</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='background-color:#fff3e0; padding:10px;'>తెలంగాణ పదాలు, సామెతలు మరియు పొడుపుకథల మజిలీకి స్వాగతం!</h3>", unsafe_allow_html=True)
        st.session_state.name = st.text_input("మీ పేరు:")
        st.session_state.place = st.text_input("మీ ఊరు:")
        if st.button("ముందుకు పోదాం"):
            if st.session_state.name and st.session_state.place:
                next_page()
            else:
                st.warning("దయచేసి పేరు మరియు ఊరు నమోదు చేయండి.")

def selection_page():
    col = side_by_side_image("second_image.jpg")
    with col:
        st.markdown(f"<h3 style='color:#4a148c;'>హలో {st.session_state.name} గారు ({st.session_state.place})!</h3>", unsafe_allow_html=True)
        st.session_state.type = st.radio("మీకు ఏమి చూడాలనిపిస్తోంది?", ["సామెతలు", "పొడుపుకథలు"], index=0)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("వెనక్కి"):
                prev_page()
        with col2:
            if st.button("తెరవండి"):
                next_page()

def content_page():
    col = side_by_side_image("second_image.jpg")
    with col:
        st.markdown(f"<h2 style='color:#2e7d32;'>📚 {st.session_state.type}</h2>", unsafe_allow_html=True)
        if st.session_state.type == "సామెతలు":
            st.markdown("- **కాకికి కేరింత ఎందుకంటే మేత కనిపించింది.**  \nఅర్థం: ఉపయోగం లేకపోయినా ఉత్సాహంగా ఉండటం.")
            st.markdown("- **చెట్టు మీద బండలు వేసినట్టు.**  \nఅర్థం: ఒకరు వినరని వ్యక్తిని కోరటం వృథా.")
            st.markdown("- **అరచేతితో నెయ్యి మింగలేరు.**  \nఅర్థం: అసాధ్యమైన పనికి ప్రయత్నించటం.")

        elif st.session_state.type == "పొడుపుకథలు":
            riddles = [
                {"question": "వేసవి తాపాన్ని తట్టుకుని చలిలో కదిలే వాడు ఎవరు?", "answer": "చెక్క"},
                {"question": "నాకొక కన్ను, కాలేదు నడవటం, మాట్లాడతాను – నేను ఎవరు?", "answer": "రేడియో"},
                {"question": "తన ఊరిని వదలకుండా నలుగురికి తిండి పెడతాడు – ఎవరు?", "answer": "చిమ్మట"}
            ]
            for idx, riddle in enumerate(riddles, 1):
                st.markdown(f"**పొడుపుకథ {idx}:** {riddle['question']}")
                user_answer = st.text_input(f"మీ సమాధానం {idx}:", key=f"riddle_{idx}")
                if user_answer:
                    if user_answer.strip() == riddle["answer"]:
                        st.success("బాగుంది! సరైన సమాధానం 🎉")
                    else:
                        st.error(f"తప్పు సమాధానం. సరైనది: {riddle['answer']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("వెనక్కి"):
                prev_page()
        with col2:
            if st.button("మీ మాట చెప్పండి"):
                next_page()

def feedback_page():
    col = side_by_side_image("second_image.jpg")
    with col:
        st.markdown("<h2 style='color:#6a1b9a;'>🙏 ధన్యవాదాలు!</h2>", unsafe_allow_html=True)
        st.markdown("మీరు 'పల్లె మాటలు' యాప్‌ని ఉపయోగించినందుకు చాలా ఆనందంగా ఉంది.")
        feedback = st.text_area("మీ అభిప్రాయం / కొత్త సామెత లేదా పొడుపుకథను ఇక్కడ నమోదు చేయండి:")
        if st.button("పంపండి"):
            st.success("మీ అభిప్రాయం పంపబడింది. ధన్యవాదాలు! 🙏")
        st.image("second_image.jpg", caption="మళ్ళీ కలుద్దాం!", use_column_width=False)
        if st.button("వెనక్కి"):
            prev_page()

# Page Routing
pages = [welcome_page, selection_page, content_page, feedback_page]
pages[st.session_state.page_number]()
