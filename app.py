import streamlit as st
import time
import random

def determine_mood(x, y):
    if x > 50 and y > 50:
        return "😄"  # Happy face
    else:
        return "😐"  # Neutral face

def main():
    st.title("Mood Detection Website")
    st.markdown('<link rel="stylesheet" type="text/css" href="https://gist.githubusercontent.com/gentlemanautomaton/3a156e726e3c83aa1f74578d47c5822b/raw/798be1ef5f67231bdaaf32e8857b58d755171ad3/style.css">', unsafe_allow_html=True)

    x_placeholder = st.empty()
    y_placeholder = st.empty()
    mood_placeholder = st.empty()

    while True:
        # Simulating received X and Y parameters
        new_x = random.random() * 100  # Replace this with actual Bluetooth data
        new_y = random.random() * 100  # Replace this with actual Bluetooth data

        x_placeholder.write(f"**X:** {new_x}")
        y_placeholder.write(f"**Y:** {new_y}")

        mood = determine_mood(new_x, new_y)
        mood_placeholder.write(f"**Mood:** {mood}")

        time.sleep(1)

if __name__ == "__main__":
    main()
