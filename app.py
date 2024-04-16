import streamlit as st
from openai import OpenAI, APIConnectionError

try:
    f = open("keys/.api_key.txt")
    key = f.read()
    client = OpenAI(api_key=key)

    st.title("💭AI Code Reviewer")

    ## input
    prompt = st.text_area("Enter your code")

    ## responses
    if st.button("Check"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": """You are a Code Reviewer.
                                                Note down all the bugs and error. 
                                                Display the correct code.
                                              """},
                {"role": "user", "content": prompt}
            ]
        )
        ## response on web
        st.write(response.choices[0].message.content)

except APIConnectionError as e:
    st.error("Connection Error: Unable to connect to the OpenAI API. Please check your network connection and API key.")