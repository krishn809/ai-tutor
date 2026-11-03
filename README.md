# AI Chatbot - Interactive AI Tutor & Knowledge Engine

A single-file Python Streamlit chatbot application designed to teach and answer questions about **Artificial Intelligence, Machine Learning, Deep Learning, and Data Science**.

Features a **Light Minimalist UI** with **Sky Blue and Sprinkle Green** accents, pure black input text, and a sidebar with API integrations, an interactive quiz, an XP rewards tracker, and a short question library.

---

## 🌟 Key Features

### 1. Dual-Intelligence Architecture
- **Built-in Offline AI Knowledge Engine**: Completely free and functions 100% offline without needing API keys or an internet connection. Pre-loaded with answers, real-world analogies, and quiz checks for core AI topics.
- **Live Cloud LLM Integration (Optional)**: Connect your **Google Gemini** or **OpenAI** API keys via the sidebar for dynamic real-time responses.

### 2. Light Minimalist UI/UX
- **Palette**: Clean off-white canvas with **Sky Blue** (`#0ea5e9`, `#0284c7`) and **Sprinkle Green** (`#10b981`, `#059669`) highlights.
- **Top-Left Sidebar Minimizer/Maximizer**: Visible in **black** (`#000000`) for easy sidebar collapsing and expanding.
- **Focused Typing Space**: Pure black text (`#000000`) on a clean input container with a Sky Blue to Sprinkle Green send button (`➔`).
- **Responsive Layout**: Designed as a modern floating card container.

### 3. Sidebar Learning Center
- **🔑 API Key Entries**: Masked input entries for Google Gemini and OpenAI with model selectors (`gemini-1.5-flash`, `gpt-4o-mini`, etc.).
- **🏆 Learning Rewards & XP Tracker**:
  - Earn `+5 XP` for every question asked.
  - Earn `+15 XP` for answering quiz questions correctly.
  - Dynamic badge unlock progression:
    - 🌱 *AI Novice* (0–29 XP)
    - 🧠 *Deep Explorer* (30–59 XP)
    - ⚡ *Neural Architect* (60–99 XP)
    - 🏆 *AI Grandmaster* (100+ XP)
- **🎯 Quick Quiz**: Interactive multiple-choice challenges with instant feedback and XP rewards.
- **📚 Short Questions Library (One-Click Explorers)**:
  - 🤖 **What is AI?**
  - 🍳 **What is ML?**
  - 👁️ **What is DL?**
  - 👥 **What is KNN?**
  - 🧠 **Neural Networks**
  - 🧪 **Turing & Tuning Test**
  - 📜 **History of AI**
  - 🏛️ **Founder of AI**
  - 🩺 **How AI Helps**

---

## 📂 Project Structure

```text
d:\khalsa\
├── chatbot.py        # Complete single-file Streamlit application
├── question.txt      # Comprehensive list of all offline-supported questions & topics
└── README.md         # Project documentation and guide
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.9+ installed along with the required libraries:

```bash
pip install streamlit
```

*(Optional, only if using live cloud APIs)*:
```bash
pip install google-generativeai openai
```

### Running the Chatbot

Run the application with Streamlit:

```bash
streamlit run chatbot.py
```

The application will launch in your browser at:
```text
http://localhost:8501
```

---

## 📖 Offline Topics Reference

For a complete list of questions that the offline engine answers, refer to [`question.txt`](./question.txt).

