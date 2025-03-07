import os

import streamlit as st
import pandas as pd

from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv

load_dotenv()

# setting the page title + subtitle
st.title("Data Analyst AI Agent 🤖")
st.write("Say hello 👋🏻 to your new Data Analyst!")
st.divider()

user_csv = st.file_uploader("Upload your CSV File", type="csv")

# wait for the user to upload the CSV file
if user_csv is not None:
    user_csv.seek(0)

    #initiate the pandas dataframe
    df = pd.read_csv(user_csv, low_memory=False)

    #inititate the LLM (temp=0)
    llm = ChatOpenAI(model="gpt-4o",temperature=0)

    #initiate the agent
    pandas_agent = create_pandas_dataframe_agent(
        llm=llm,
        df=df,
        verbose=True,
        allow_dangerous_code=True
    )

    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat messages from history on app rerun
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)


    # create the bar where we can type messages
    user_question = st.chat_input("What do you want to know about this dataset?")


    # did the user submit a prompt?
    if user_question:

        # add the message from the user (prompt) to the screen with streamlit
        with st.chat_message("user"):
            st.markdown(user_question)

            st.session_state.messages.append(HumanMessage(user_question))


        # invoking the agent
        result = pandas_agent.invoke({"input": user_question, "chat_history":st.session_state.messages})

        ai_message = result["output"]

        # adding the response from the llm to the screen (and chat)
        with st.chat_message("assistant"):
            st.markdown(ai_message)

            st.session_state.messages.append(AIMessage(ai_message))
