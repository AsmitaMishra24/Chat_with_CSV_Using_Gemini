import streamlit as st
from dotenv import load_dotenv
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import GoogleGenerativeAI
import os

def main():
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("GOOGLE_API_KEY not found. Please set it in a .env file.")
        return

    st.set_page_config(page_title="Ask your CSV 📈")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload your CSV file", type="csv")

    if csv_file is not None:
        user_question = st.text_input("Ask a question about your CSV:")

        llm = GoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0
        )

        try:
            agent = create_csv_agent(
                llm,
                csv_file,
                verbose=True,
                allow_dangerous_code=True
            )
        except Exception as e:
            st.error(f"Error creating agent: {e}")
            return

        if user_question:
            with st.spinner("Processing..."):
                try:
                    response = agent.run(user_question)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
