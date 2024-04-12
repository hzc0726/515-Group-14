import streamlit as st
from components import light_control, movement_data, user_info

# A simple function to mimic a chatbot response
def chatbot_response(user_input):
    # This is a very basic example. You can integrate NLP models or predefined responses based on keywords.
    responses = {
        "hello": "Hello! How can I help you today?",
        "light": "You can control the light using the sliders above.",
        "bye": "Goodbye! Have a nice day!"
    }
    # Return a response based on user input or a default message
    return responses.get(user_input.lower(), "Sorry, I didn't understand that. Can you try different words?")

def main():
    st.title("Smart Lighting System")

    # Light control UI
    st.header("Control LED Brightness and Color")
    brightness = st.slider("Select Brightness", min_value=0, max_value=100, value=50)
    color = st.color_picker("Pick a Color", "#00f900")
    if st.button("Set Light"):
        light_control.set_light(brightness, color)

    # Movement data display
    st.header("Movement Data")
    movement = movement_data.get_movement_data()
    st.write("Movement detected:", movement)

    # User information display
    st.header("User Information")
    time, location = user_info.get_user_info()
    st.write("Current time:", time)
    st.write("User location:", location)

    # Chatbot Section
    st.header("Chat with our Bot")
    user_input = st.text_input("Type your message here:")
    if st.button("Send"):
        response = chatbot_response(user_input)
        st.text_area("Bot says:", value=response, height=100, max_chars=None, key="chat_response")

if __name__ == "__main__":
    main()
