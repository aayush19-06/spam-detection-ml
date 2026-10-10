
import streamlit as st
import joblib

# Load your trained model
model = joblib.load("spam_model.pkl")

st.set_page_config(
    page_title="Spam Detection",
    page_icon="📩"
)

st.title("📩 Spam Message Detection")
st.write("Enter a message to check whether it is spam.")

message = st.text_area("Enter your message:")

if st.button("Check Message"):
    if message.strip():
        prediction = model.predict([message])[0]

        if prediction == "spam":
            st.error("🚨 This message is classified as SPAM.")
        else:
            st.success("✅ This message is classified as HAM (not spam).")
    else:
        st.warning("Please enter a message.")
