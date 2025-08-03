# 📚 Automated Book Publication Workflow 🚀

This project streamlines the process of preparing book chapters using AI. It automates:

- ✅ Web scraping or file-based content ingestion
- ✍️ Rewriting content using Gemini AI
- 🧠 Reviewing content using GPT-based reviewer
- 🧑‍💻 Human-in-the-loop edits or approval
- 🤖 RL reward scoring to evaluate quality
- 🧠 Version tracking using ChromaDB

---

## 🌟 Features

- AI-powered content rewriting with **Gemini**
- Intelligent review/feedback from **OpenAI GPT**
- Human-in-the-loop decision step (Accept / Edit / Reject)
- Final output scored using **RL reward model**
- Version control stored via **ChromaDB**

---

## 📁 Project Structure

automated-book-workflow/
│
├── main.py # Main pipeline script
├── requirements.txt # Python dependencies
│
├── content/
│ └── chapter1.txt # Sample chapter file to rewrite
│
├── ai_agents/
│ ├── writer.py # Gemini AI content rewriter
│ ├── reviewer.py # OpenAI-based reviewer
│ ├── human_review.py # Simulated human-in-the-loop
│ ├── reward_model.py # RL-style reward evaluator
│ └── chroma_store.py # ChromaDB vector version store

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/tejashree-2002/automated-book-workflow.git
cd automated-book-workflow

### 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

### 3. Set API Keys
Create a .env file in the root:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
Or set them directly:

bash
Copy
Edit
export OPENAI_API_KEY=your_openai_key
export GEMINI_API_KEY=your_gemini_key

### 4. Add Chapter Input
Place your .txt files (e.g., chapter1.txt) inside the /content folder.

🚀 Running the Pipeline
bash
Copy
Edit
python main.py

📝 Output Preview
Rewritten chapter is printed to the console

Human-in-the-loop prompt asks to Accept, Edit, or Reject

RL model gives a score

Final version is saved to ChromaDB

🧠 Tech Stack
Feature	Tool
Content Rewrite	Gemini AI (PaLM / Gemini-Pro)
Review Agent	OpenAI GPT-4 / GPT-3.5
Feedback	Human-in-the-loop
Evaluation	Custom RL reward
Versioning	ChromaDB
