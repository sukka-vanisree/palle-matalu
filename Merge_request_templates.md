🧠 Why Use a Merge Request Template for This Streamlit Project?
For your Telugu cultural app – పల్లె మాటలు, using MR templates will:

Ensure quality and consistency in all updates.

Help contributors explain what changes were made, why, and how to test them.

Promote team collaboration, even in solo projects, for better project hygiene.

📄 Example Merge Request Template for Your Project
Below is a detailed merge request template you can use (.gitlab/merge_request_templates/feature.md or .github/PULL_REQUEST_TEMPLATE/feature.md):

📌 Title: Add <Feature Name> to Pallē Māṭalu App
🧾 Description
Describe what this merge request does.

Example:

This MR adds a new section under "పొడుపుకథలు" with three new riddles and modifies the layout to enhance readability on mobile screens.

✅ Checklist
 Code runs without errors

 Follows Streamlit coding standards

 New page(s) or functionality tested

 UI tested with different inputs (e.g., name, village, wrong answer, etc.)

 No broken images or layout issues

 Translations/labels are in proper Telugu

 Navigation (Next/Back) still works

🔍 Screenshots (If UI Changed)
Please attach screenshots of any new or updated pages.

🧪 How to Test This
Step-by-step instructions to validate the change:

Run streamlit run app.py

Enter your name and village

Select "పొడుపుకథలు"

Test each riddle by entering answers

Click "మీ మాట చెప్పండి" and submit feedback

🗣️ Related Issues / Feature Requests
If this MR fixes or relates to an issue:

Closes #12 – Add more riddles

🔁 Additional Notes
Any limitations, known bugs, or pending enhancements:

Layout on very small screens (mobile) needs padding adjustment.

📁 Where to Place This Template?
For GitHub:

Create .github/PULL_REQUEST_TEMPLATE.md in your repo.

For GitLab:

Create .gitlab/merge_request_templates/feature.md

GitLab will allow selecting this template when creating a merge request.

🧩 Example Scenario Using Your Code
Suppose you add a new proverb category called "తెలుగు నానుడులు" in your selection_page():

python
Copy
Edit
st.session_state.type = st.radio("మీకు ఏమి చూడాలనిపిస్తోంది?", ["సామెతలు", "పొడుపుకథలు", "తెలుగు నానుడులు"], index=0)
You would use a merge request template to explain:

You added a new option.

What content you added under it.

Any images or UI changes.

That you tested all navigation paths still work.

