import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from operator import itemgetter

# --- Configuration and LangChain Setup ---

# The GROQ_API_KEY should be set in the Colab environment (e.g., in a previous cell).
# This checks if it's available.
if "GROQ_API_KEY" not in os.environ or not os.environ["GROQ_API_KEY"]:
    st.error("GROQ_API_KEY not found. Please set it in your environment variables.")
    st.stop()

llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

output_parser = StrOutputParser()

pname = PromptTemplate(
    input_variables=['cuisine'],
    template="""
    I want to open a restaurant for {cuisine} food.
    Suggest only one restaurant name.
    """
)

name_generation_runnable = pname | llm | output_parser

pmenu = PromptTemplate(
    input_variables=['res_name'],
    template="""
    Suggest a restaurant menu for {res_name}.
    """
)

menu_generation_runnable = pmenu | llm | output_parser

chain = (
    RunnablePassthrough.assign(res_name=name_generation_runnable)
    |
    RunnableParallel(
        menu=menu_generation_runnable,
        res_name=itemgetter("res_name")
    )
)

# --- Streamlit Application Layout ---

st.set_page_config(
    page_title="Restaurant Idea Generator",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("🍽️ Restaurant Idea Generator")
st.markdown("### Get creative restaurant names and menus powered by Groq and LangChain!")
st.write("Enter a cuisine below and let our AI suggest a unique restaurant name and a delicious menu.")

# Input field for cuisine
cuisine_input = st.text_input("What cuisine are you thinking of?", placeholder="e.g., Mexican, Italian, Indian", help="Type in your desired cuisine and hit 'Generate'.")

# Button to trigger generation
if st.button("✨ Generate Restaurant Ideas", type="primary"):
    if cuisine_input:
        with st.spinner("Generating your restaurant ideas... this might take a moment!"):
            try:
                # Invoke the LangChain chain
                response = chain.invoke({"cuisine": cuisine_input})

                st.success("Ideas generated!")

                # Display Restaurant Name
                st.subheader("🎉 Your Restaurant Name Idea:")
                st.markdown(f"## {response['res_name']}")

                # Display Menu
                st.subheader("📜 Suggested Menu:")
                st.markdown(response['menu'])

            except Exception as e:
                st.error(f"An error occurred during generation: {e}")
                st.warning("Please ensure your GROQ_API_KEY is correctly set up.")
    else:
        st.warning("Please enter a cuisine to get restaurant ideas!")

st.markdown("---")
st.info("Powered by LangChain and Groq LLMs. Made with Streamlit.")
