# 📊 Chat with Your CSV Using Gemini

Interact with your CSV data just like you're chatting with a data analyst!  
This project lets you **upload any CSV file and ask questions**. Behind the scenes, it uses **Gemini (Google's LLM)** with LangChain agents to understand your query, reason through it, run Python code, and give the result — instantly!

![Homepage](https://github.com/user-attachments/assets/02691ff1-f258-42de-839d-13d784fa088a)


---
## ⚙️ How a Large Language Model (LLM) Works:

![llm_diagram](https://github.com/user-attachments/assets/2f3f7514-7725-42a8-a1ca-5c37144a73a8)

1. At its core, a Large Language Model like Gemini processes a prompt — which is a mix of instructions, examples, and the actual input — and generates a meaningful response. As shown below:

2. Prompt = Instruction + Test Input: The prompt can contain a task description (e.g., "Summarize the data"), a few examples, and your actual input — such as a question about the CSV.

3. LLM Reasoning: The model uses its pre-trained knowledge and the provided prompt to predict what comes next — effectively "thinking" about how to answer.

4. Generated Output: The output might be plain text (a summary or explanation) or executable code (as in this project). The code is then executed to retrieve the final answer.

This mechanism allows the LLM to understand your intent, dynamically generate logic (like Python code), and provide relevant, accurate results from your data.

---

## 🔧 Technologies Used

| Component         | Description |
|------------------|-------------|
| 🧠 **Google Gemini (gemini-1.5-flash)** | The Large Language Model that understands and answers your questions |
| 🔗 **LangChain CSV Agent** | Translates your questions into Python code and runs it |
| 📊 **Pandas (indirect)** | Used internally to analyze CSV files |
| 🎈 **Streamlit** | Frontend to upload files and interact with the model |
| 🔐 **dotenv** | Securely loads your API key from `.env` |

---

## 🧠 How It Works

1. Upload a CSV file through the UI.
2. Ask a natural language question (e.g. "What is the mean area of the malignant tumors?")
3. LangChain wraps the Gemini model with a Python code executor.
4. Gemini thinks in steps: it figures out what to calculate, writes code, runs it, and returns the answer.
5. The answer is shown on your screen with an optional explanation.
   
---

## 🧩 How the Agent Thinks (Step-by-Step)

> It goes through:
> - 🧠 Thought
> - ⚙️ Action (Python code)
> - 📥 Input (code to run)
> - 👀 Observation (what the code returns)
> - ✅ Final Answer

Here’s an actual screenshot showing the thought process of Gemini through LangChain:

![Ques1](https://github.com/user-attachments/assets/09c9c3ba-799f-486b-a7ba-bc1dc6395870)

![Ques2](https://github.com/user-attachments/assets/760d2c25-0da2-4c85-89cf-00c5ec60a744)

---

## 🖥️ How It Appears on Screen

The user sees a simple Streamlit UI where they can upload a CSV and ask questions interactively:

![Ques1](https://github.com/user-attachments/assets/326d1d08-8bc0-4833-aa45-21d6e1b4f95e)

![Ques2](https://github.com/user-attachments/assets/ba51b8da-1378-44d5-98b9-ab0c6a462372)


> Streamlit auto-refreshes results when the question is submitted. Great for rapid exploration.

---

## 🎥 Demo Video

https://github.com/user-attachments/assets/f44b3a52-086c-42a5-8f08-e909077f32de

---

## ⚙️ Setup Instructions

Follow these steps to get the app running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/AsmitaMishra24/Chat_with_CSV_Using_Gemini.git
cd Chat_with_CSV_Using_Gemini
```

### 2. Create a Virtual Environment 

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a ```.env``` file by copying the example:
```bash
cp .env.example .env
```

Then paste your actual Google API Key in ```.env```:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
🔑 Get your key from [Google AI Studio](https://aistudio.google.com/apikey)

### 5. Run the App
```bash
streamlit run app.py
```
Then go to: http://localhost:8501

---

##  .env.example
```env
# .env.example
GOOGLE_API_KEY=your_google_api_key_here
```
---

## ✅ Example Questions to Try
- What is the total profit by category?

- Which month had the highest revenue?

- What’s the average number of orders per region?

- Show top 5 performing products.
---

## 🤝 Contributing
Want to improve the project? Fix bugs? Add features?

1. Fork the repo

2. Create a new branch (git checkout -b feature-name)

3. Commit changes (git commit -am 'Add feature')

4. Push and open a PR

---

## 📬 Contact

Made by **Asmita Mishra**
- 🔗 [LinkedIn](https://www.linkedin.com/in/asmitamishra1/)  
- 💻 [GitHub](https://github.com/AsmitaMishra24)  

🙋‍♀️ **Have a suggestion or found a bug?**  
- Feel free to [**raise an issue**](https://github.com/AsmitaMishra24/Employee-Directory-Application-using-AWS/issues) in this repository.

📩 **Want to connect or collaborate?**
- Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/asmitamishra1/)

