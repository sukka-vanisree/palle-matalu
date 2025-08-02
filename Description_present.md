# 🌾 పల్లె మాటలు – A Cultural Language Experience App

**పల్లె మాటలు** is a Streamlit-based interactive web application designed to preserve and promote Telangana’s rural language heritage, including **local proverbs (సామెతలు)** and **folk riddles (పొడుపుకథలు)**.

---

## 🎯 Objective

To offer users a nostalgic and educational experience of rural Telugu wisdom through an easy-to-use, visually rich web interface.

---

## 🧑‍💻 Features

### 1. Welcome Page
- Collects user's name and village (handled by `st.text_input()`).
- Personalized greeting and validation before proceeding.

### 2. Selection Page
- Asks the user what they want to explore: **సామెతలు** or **పొడుపుకథలు**.
- Uses radio buttons (`st.radio()`) for selection.

### 3. Content Display Page
- Based on selection:
  - **Proverbs** are shown with meanings.
  - **Riddles** allow users to input answers and receive immediate feedback (`st.success()`, `st.error()`).
  
4. Feedback Page
- Users can submit opinions or contribute their own proverbs/riddles via a `text_area`.
- Success message confirms submission.



 🖼 UI Layout

- Clean 2-column layout using `st.columns()`:
  - Left side: Cultural image (`st.image()`).
  - Right side: Interactive content.
  
- Custom styles using `unsafe_allow_html=True` for colored headings and text.



 🗃️ State Management

- Uses `st.session_state` to:
  - Track user's name, village, selected type, answers, and navigation state (`page_number`).
  - Ensure smooth multi-page flow with `next_page()` and `prev_page()` functions.


 🔁 Navigation Flow

1. Welcome (collects name/place) →  
2. Selection (choose category) →  
3. Content (view/respond) →  
4. Feedback (submit opinion)

Navigation buttons at the bottom of each page (`వెనక్కి`, `తెరవండి`, `మీ మాట చెప్పండి`) move between pages.



 📦 Requirements

- Python 3.x
- Streamlit
- Image assets (`front_image.jpg`, `second_image.jpg`) should be in the same directory.



 🚀 Run the App

```bash
streamlit run app.py
