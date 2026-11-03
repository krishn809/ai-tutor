import sys
import os
import html
import streamlit as st

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

st.set_page_config(
    page_title="AI Chatbot | Minimalist AI Tutor",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="expanded",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "xp" not in st.session_state:
    st.session_state.xp = 0

if "quizzes_completed" not in st.session_state:
    st.session_state.quizzes_completed = 0

if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0

if "current_badge" not in st.session_state:
    st.session_state.current_badge = "🌱 AI Novice"

LIGHT_MINIMALIST_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
    background: 
        radial-gradient(circle at 10% 12%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 90% 88%, rgba(52, 211, 153, 0.08) 0%, transparent 40%),
        #f8fafc !important;
    background-attachment: fixed !important;
    color: #1e293b !important;
    min-height: 100vh !important;
}

#MainMenu, footer, .stDeployButton {
    display: none !important;
    visibility: hidden !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    z-index: 1000 !important;
}

[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    display: block !important;
    visibility: visible !important;
    color: #000000 !important;
    z-index: 999999 !important;
    top: 14px !important;
    left: 14px !important;
}

[data-testid="collapsedControl"] button,
[data-testid="stSidebarCollapsedControl"] button {
    color: #000000 !important;
    background: #ffffff !important;
    border: 2px solid #000000 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
    padding: 5px 9px !important;
    transition: all 0.2s ease !important;
}

[data-testid="collapsedControl"] button:hover,
[data-testid="stSidebarCollapsedControl"] button:hover {
    background: #000000 !important;
    color: #ffffff !important;
}

[data-testid="collapsedControl"] button:hover svg,
[data-testid="stSidebarCollapsedControl"] button:hover svg {
    fill: #ffffff !important;
    stroke: #ffffff !important;
}

[data-testid="collapsedControl"] svg,
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="stSidebarCollapseButton"] svg {
    fill: #000000 !important;
    stroke: #000000 !important;
}

[data-testid="stSidebarCollapseButton"] button {
    color: #000000 !important;
    background: #ffffff !important;
    border: 1.5px solid #000000 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1) !important;
}

[data-testid="stSidebarCollapseButton"] button:hover {
    background: #000000 !important;
    color: #ffffff !important;
}

[data-testid="stSidebarCollapseButton"] button:hover svg {
    fill: #ffffff !important;
    stroke: #ffffff !important;
}

[data-testid="stMainBlockContainer"], .block-container {
    max-width: 680px !important;
    width: 95% !important;
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 24px !important;
    box-shadow: 0 12px 35px rgba(14, 165, 233, 0.05), 
                0 2px 8px rgba(0, 0, 0, 0.02) !important;
    padding: 24px 28px !important;
    margin: 20px auto !important;
}

.minimal-header {
    text-align: center;
    padding: 4px 0 14px 0;
    border-bottom: 1px solid #f1f5f9;
    margin-bottom: 16px;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    color: #059669;
    font-size: 0.76rem;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 999px;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #10b981;
    box-shadow: 0 0 6px rgba(16, 185, 129, 0.5);
    display: inline-block;
    animation: pulse-green 2s infinite ease-in-out;
}

@keyframes pulse-green {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.85); }
}

.minimal-title {
    font-size: 1.9rem;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.5px;
    margin: 2px 0 4px 0;
}

.minimal-title span {
    background: linear-gradient(135deg, #0284c7 0%, #10b981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.minimal-subtitle {
    color: #64748b;
    font-size: 0.92rem;
    font-weight: 400;
    margin: 0;
}

.topic-label {
    font-size: 0.74rem;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748b;
    font-weight: 700;
    margin-bottom: 8px;
    text-align: center;
}

div[data-testid="stButton"] > button {
    background: #ffffff !important;
    color: #0f172a !important;
    border: 1px solid #e0f2fe !important;
    border-radius: 12px !important;
    padding: 8px 14px !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    box-shadow: 0 2px 8px rgba(2, 132, 199, 0.04) !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}

div[data-testid="stButton"] > button:hover {
    background: #f0f9ff !important;
    color: #0284c7 !important;
    border-color: #38bdf8 !important;
    box-shadow: 0 4px 14px rgba(14, 165, 233, 0.14) !important;
    transform: translateY(-1.5px) !important;
}

.chat-scroll-frame {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin: 14px 0 18px 0;
    max-height: 480px;
    overflow-y: auto;
    padding-right: 4px;
}

.chat-scroll-frame::-webkit-scrollbar {
    width: 5px;
}
.chat-scroll-frame::-webkit-scrollbar-track {
    background: #f1f5f9;
    border-radius: 8px;
}
.chat-scroll-frame::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 8px;
}
.chat-scroll-frame::-webkit-scrollbar-thumb:hover {
    background: #38bdf8;
}

.bubble-user {
    align-self: flex-end;
    background: #f0f9ff;
    border: 1px solid #bae6fd;
    color: #0369a1;
    padding: 11px 16px;
    border-radius: 18px 18px 4px 18px;
    max-width: 82%;
    font-size: 0.93rem;
    line-height: 1.5;
    box-shadow: 0 2px 8px rgba(2, 132, 199, 0.04);
    margin-left: auto;
    word-break: break-word;
    font-weight: 500;
}

.bubble-bot {
    align-self: flex-start;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #10b981;
    color: #1e293b;
    padding: 16px 20px;
    border-radius: 4px 18px 18px 18px;
    max-width: 92%;
    font-size: 0.92rem;
    line-height: 1.62;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.03);
    word-break: break-word;
}

.bot-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.72rem;
    font-weight: 700;
    color: #059669;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    padding: 2px 8px;
    border-radius: 6px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.bubble-bot b, .bubble-bot strong {
    color: #0f172a !important;
}

.bubble-bot hr {
    border: none;
    border-top: 1px solid #f1f5f9;
    margin: 12px 0;
}

div[data-testid="stForm"] {
    border: 1.5px solid #cbd5e1 !important;
    background: #ffffff !important;
    border-radius: 18px !important;
    padding: 6px 10px !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03) !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stForm"]:focus-within {
    border-color: #0ea5e9 !important;
    box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.12), 0 4px 16px rgba(14, 165, 233, 0.08) !important;
}

div[data-testid="stTextInput"] > div > div > input {
    background: transparent !important;
    border: none !important;
    color: #000000 !important;
    font-size: 0.96rem !important;
    padding: 8px 12px !important;
    font-weight: 500 !important;
    caret-color: #0ea5e9 !important;
}

div[data-testid="stTextInput"] > div > div > input::placeholder {
    color: #94a3b8 !important;
    font-weight: 400 !important;
}

div[data-testid="stTextInput"] > div > div > input:focus {
    box-shadow: none !important;
    outline: none !important;
}

div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #0ea5e9 0%, #10b981 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    height: 42px !important;
    width: 44px !important;
    min-width: 44px !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    box-shadow: 0 2px 10px rgba(14, 165, 233, 0.25) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4) !important;
}

[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e2e8f0 !important;
    color: #1e293b !important;
}

.rewards-box {
    background: linear-gradient(135deg, #f0f9ff 0%, #ecfdf5 100%);
    border: 1px solid #bae6fd;
    border-radius: 16px;
    padding: 14px;
    margin-bottom: 16px;
    text-align: center;
}

.reward-title {
    font-size: 0.78rem;
    text-transform: uppercase;
    font-weight: 800;
    color: #0369a1;
    letter-spacing: 0.8px;
    margin-bottom: 4px;
}

.reward-points {
    font-size: 1.6rem;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.2;
}

.badge-pill {
    display: inline-block;
    background: #ffffff;
    border: 1px solid #a7f3d0;
    color: #059669;
    font-weight: 700;
    font-size: 0.8rem;
    padding: 3px 10px;
    border-radius: 999px;
    margin-top: 6px;
    box-shadow: 0 2px 6px rgba(16, 185, 129, 0.1);
}

.sidebar-section-title {
    font-size: 0.82rem;
    font-weight: 800;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 16px 0 8px 0;
    display: flex;
    align-items: center;
    gap: 6px;
}
</style>
"""
st.markdown(LIGHT_MINIMALIST_CSS, unsafe_allow_html=True)

AI_KNOWLEDGE = {
    "what_is_ai": {
        "title": "Artificial Intelligence (AI)",
        "keywords": ["what is ai", "define ai", "artificial intelligence", "intro to ai", "basics of ai", "explain ai"],
        "content": (
            "<b>Artificial Intelligence (AI)</b> refers to computer systems engineered to simulate human intelligence—such as "
            "learning from experience, reasoning, solving complex problems, and understanding natural language and vision.<br><br>"
            "🚗 <b>Analogy:</b> Traditional software is like a train on fixed railway tracks—it only moves where tracks are laid. "
            "AI is like an autonomous vehicle that reads unexpected road conditions, recalculates, and learns the optimal path.<br><br>"
            "<b>The 3 Stages of AI Development:</b><br>"
            "• <b>Narrow AI (ANI):</b> Specialized for specific tasks (ChatGPT, AlphaFold, Siri). This is current AI.<br>"
            "• <b>General AI (AGI):</b> Human-level cognitive adaptability across any intellectual domain.<br>"
            "• <b>Super AI (ASI):</b> Hypothetical intelligence surpassing collective human capability in scientific discovery and strategy."
        ),
        "quiz": "💡 <b>Quick Question:</b> Is an image recognition model for medical scans considered Narrow AI (ANI) or General AI (AGI)?"
    },
    "machine_learning": {
        "title": "Machine Learning (ML)",
        "keywords": ["machine learning", "what is ml", "how ml works", "learn ml", "types of ml"],
        "content": (
            "<b>Machine Learning</b> is the core branch of AI where algorithms discover patterns in historical data "
            "to make predictions or decisions without being explicitly hand-coded with rule logic.<br><br>"
            "🍳 <b>Analogy:</b> Traditional coding is following a strict recipe book. Machine Learning is a master chef "
            "tasting thousands of dishes and mathematically identifying the exact balance of flavors.<br><br>"
            "<b>The 3 Core Paradigms:</b><br>"
            "1. <b>Supervised Learning:</b> Training with labeled pairs (Input X ➔ Target Y). e.g., Spam detection, housing price regression.<br>"
            "2. <b>Unsupervised Learning:</b> Finding latent clusters in unlabeled data. e.g., Customer segmentation, anomaly detection.<br>"
            "3. <b>Reinforcement Learning:</b> Agents maximizing reward signals via trial and error. e.g., AlphaGo, autonomous driving."
        ),
        "quiz": "💡 <b>Quick Question:</b> If you train a model to forecast stock prices using historical price data, is that Supervised or Unsupervised?"
    },
    "deep_learning": {
        "title": "Deep Learning (DL)",
        "keywords": ["deep learning", "what is dl", "ann", "deep neural network"],
        "content": (
            "<b>Deep Learning</b> is a specialized subset of Machine Learning powered by multi-layered Artificial Neural Networks. "
            "The term 'deep' refers to having multiple hidden layers between the input and output.<br><br>"
            "👁️ <b>Analogy:</b> In facial recognition, Layer 1 detects simple edges; Layer 2 combines edges into curves and textures; "
            "Layer 3 forms eyes and noses; and final layers recognize the entire face.<br><br>"
            "<b>Why Deep Learning exploded:</b><br>"
            "• <b>Automatic Feature Extraction:</b> Eliminates manual feature engineering.<br>"
            "• <b>Big Data & GPUs:</b> Massively parallel computation allows training on billions of parameters.<br>"
            "• <b>Versatility:</b> Powers speech recognition, self-driving vision, and generative art."
        ),
        "quiz": "💡 <b>Quick Question:</b> What makes Deep Learning different from traditional Machine Learning?"
    },
    "knn": {
        "title": "K-Nearest Neighbors (KNN)",
        "keywords": ["knn", "k-nearest neighbors", "k nearest neighbor", "knn algorithm"],
        "content": (
            "<b>K-Nearest Neighbors (KNN)</b> is a simple, intuitive, non-parametric Supervised Learning algorithm "
            "used for both <b>Classification</b> and <b>Regression</b>.<br><br>"
            "👥 <b>Analogy:</b> <i>'Birds of a feather flock together.'</i> If you want to know which political party someone supports, "
            "look at the 5 closest friends they hang out with—the majority party among those 5 is your prediction!<br><br>"
            "<b>How KNN Works:</b><br>"
            "1. Calculate mathematical distance (Euclidean, Manhattan) between a new data point and all training points.<br>"
            "2. Select the <b>K</b> closest neighbors.<br>"
            "3. For Classification: Take a majority vote. For Regression: Calculate the average value.<br><br>"
            "💡 <b>Tip:</b> If K is too small (e.g., K=1), the model is sensitive to noise (Overfitting). If K is too large, boundaries blur (Underfitting)."
        ),
        "quiz": "💡 <b>Quick Question:</b> Why is KNN called a 'Lazy Learner' algorithm?"
    },
    "neural_network": {
        "title": "Neural Networks (ANNs)",
        "keywords": ["neural network", "neural networks", "perceptron", "neurons", "layers", "backpropagation"],
        "content": (
            "An <b>Artificial Neural Network (ANN)</b> is a computing architecture inspired by biological neurons in the human brain.<br><br>"
            "🧠 <b>Key Anatomy:</b><br>"
            "• <b>Input Layer:</b> Receives numerical features (pixels, text tokens, tabular numbers).<br>"
            "• <b>Hidden Layers:</b> Nodes compute weighted sums: <code>z = \u2211(w\u1d62 \u00b7 x\u1d62) + b</code> and pass through activation functions.<br>"
            "• <b>Activation Functions:</b> Non-linear functions (ReLU, GELU, Sigmoid) enabling networks to learn complex curves.<br>"
            "• <b>Backpropagation & Gradient Descent:</b> Uses calculus chain rule to calculate prediction errors and update weights iteratively."
        ),
        "quiz": "💡 <b>Quick Question:</b> What is the purpose of the 'bias' (b) term in an artificial neuron?"
    },
    "turing_and_tuning": {
        "title": "Turing Test & Model Tuning",
        "keywords": ["tuning test", "turing test", "model tuning", "fine tuning", "hyperparameter tuning"],
        "content": (
            "This covers two essential AI concepts: <b>The Turing Test</b> and <b>Model Tuning</b>!<br><br>"
            "1️⃣ <b>The Turing Test (Alan Turing, 1950):</b><br>"
            "A test of a machine's ability to exhibit intelligent behavior indistinguishable from that of a human. "
            "If a human evaluator cannot reliably tell whether they are conversing with a human or a machine, the machine passes.<br><br>"
            "2️⃣ <b>Model Tuning & Fine-Tuning:</b><br>"
            "• <b>Hyperparameter Tuning:</b> Finding optimal learning rates, batch sizes, and tree depths (via Grid Search, Bayesian Optimization).<br>"
            "• <b>Fine-Tuning (LLMs):</b> Taking a pre-trained base model and training it further on domain-specific data (e.g., medical or legal texts)."
        ),
        "quiz": "💡 <b>Quick Question:</b> What is the difference between a model parameter (weights) and a hyperparameter (learning rate)?"
    },
    "history_of_ai": {
        "title": "History of Artificial Intelligence",
        "keywords": ["history of ai", "ai history", "timeline of ai", "when was ai founded"],
        "content": (
            "Artificial Intelligence has evolved over seven decades of breakthroughs and 'AI Winters':<br><br>"
            "• <b>1950 - The Spark:</b> Alan Turing publishes <i>'Computing Machinery and Intelligence'</i>, proposing the Turing Test.<br>"
            "• <b>1956 - The Birth:</b> The Dartmouth Summer Research Project officially coins the term 'Artificial Intelligence'.<br>"
            "• <b>1970s & 1980s - AI Winters:</b> Funding dried up when early symbolic systems failed to handle real-world messiness.<br>"
            "• <b>1997 - Deep Blue:</b> IBM's Deep Blue defeats World Chess Champion Garry Kasparov.<br>"
            "• <b>2012 - Deep Learning Era:</b> AlexNet wins ImageNet by a landslide using GPUs and CNNs.<br>"
            "• <b>2017 to Present - Generative AI:</b> Google introduces the Transformer architecture, sparking LLMs (ChatGPT, Gemini, Claude)."
        ),
        "quiz": "💡 <b>Quick Question:</b> What 1956 conference is considered the official birthplace of AI as a field?"
    },
    "founder_of_ai": {
        "title": "Founders and Pioneers of AI",
        "keywords": ["founder of ai", "father of ai", "who created ai", "who invented ai", "founders of ai"],
        "content": (
            "Several legendary visionaries earned the title of AI pioneers:<br><br>"
            "🏛️ <b>The Founding Fathers:</b><br>"
            "• <b>John McCarthy:</b> Known as the <i>'Father of AI'</i>. He coined the term 'Artificial Intelligence' in 1955 and created the LISP programming language.<br>"
            "• <b>Alan Turing:</b> The intellectual godfather who conceived machine intelligence and the Turing Test in 1950.<br>"
            "• <b>Marvin Minsky:</b> Co-founder of the MIT AI Laboratory, pioneering cognitive science, robotics, and early perceptrons.<br>"
            "• <b>Herbert Simon & Allen Newell:</b> Created the Logic Theorist (1956), widely called the first running AI program.<br><br>"
            "🌟 <b>Modern Deep Learning Godfathers:</b><br>"
            "• <b>Geoffrey Hinton, Yann LeCun, & Yoshua Bengio:</b> Won the 2018 Turing Award for pioneering modern Deep Learning."
        ),
        "quiz": "💡 <b>Quick Question:</b> Who coined the exact term 'Artificial Intelligence'?"
    },
    "how_ai_helps": {
        "title": "How AI Helps Humanity & Modern Society",
        "keywords": ["how ai helps", "benefits of ai", "why ai is useful", "ai applications", "how ai can help"],
        "content": (
            "Artificial Intelligence is transforming nearly every domain of human endeavor:<br><br>"
            "🩺 <b>Healthcare & Medicine:</b> Diagnosing cancers and retinal diseases earlier than human eye; AlphaFold solved 200M+ protein structures in days.<br>"
            "🌍 <b>Climate & Agriculture:</b> Optimizing renewable energy grids, predicting weather patterns, and guiding precision crop harvesting.<br>"
            "🚗 <b>Transportation:</b> Self-driving vehicles, logistics route optimization, and collision avoidance systems.<br>"
            "📚 <b>Education:</b> Personalized 24/7 AI tutoring adapted to each student's learning speed and style.<br>"
            "🔬 <b>Scientific Discovery:</b> Accelerating material discovery for clean batteries and simulating complex quantum systems."
        ),
        "quiz": "💡 <b>Quick Question:</b> In which field do you believe AI will have the largest positive impact over the next 10 years?"
    },
    "llms_transformers": {
        "title": "Large Language Models & Transformers",
        "keywords": ["llm", "large language model", "transformer", "chatgpt", "how do llms work", "attention mechanism", "self attention"],
        "content": (
            "<b>Large Language Models (LLMs)</b> are neural networks trained on vast text corpora to predict the most contextually relevant next token.<br><br>"
            "📚 <b>Analogy:</b> Imagine a researcher who has memorized every written book. When you write half a thought, "
            "they instantaneously predict the most cogent and insightful continuation.<br><br>"
            "<b>Key Building Blocks:</b><br>"
            "• <b>Tokenization:</b> Slicing raw text into token IDs.<br>"
            "• <b>Vector Embeddings:</b> Mapping words into continuous semantic vector spaces.<br>"
            "• <b>Self-Attention:</b> Dynamically calculating attention weights between all words in parallel."
        ),
        "quiz": "💡 <b>Quick Question:</b> What fundamental mechanism enables Transformers to process all words in a sentence in parallel?"
    }
}

def query_offline_tutor(user_prompt: str) -> str:
    prompt_clean = user_prompt.lower().strip()

    if prompt_clean in ["b", "k-means", "kmeans", "option b", "b)"]:
        return (
            "🎉 <b>Correct! Option B: K-Means Clustering!</b><br><br>"
            "Unlike Linear Regression, Random Forests, or SVMs (which require labeled ground-truth targets Y), "
            "<b>K-Means Clustering</b> groups unlabeled data points together based purely on spatial distance metrics.<br><br>"
            "🌟 <i>Great job! What AI concept would you like to explore next? (Check the sidebar for quick topics!)</i>"
        )
    elif prompt_clean in ["a", "c", "d", "option a", "option c", "option d"]:
        return (
            "❌ <b>Not quite! The correct answer is B: K-Means Clustering.</b><br><br>"
            "Linear Regression, Random Forests, and SVMs are all <b>Supervised Learning</b> algorithms that rely on labeled ground-truth pairs. "
            "K-Means uncovers clusters on unlabeled datasets without supervision!<br><br>"
            "💡 <i>Check the sidebar 'KNN' or 'Machine Learning' buttons to dive deeper!</i>"
        )

    best_match = None
    highest_score = 0
    for key, data in AI_KNOWLEDGE.items():
        score = 0
        for kw in data["keywords"]:
            if kw in prompt_clean:
                score += len(kw.split()) * 2
        if score > highest_score:
            highest_score = score
            best_match = data

    if best_match and highest_score > 0:
        return f"<b>{best_match['title']}</b><br><br>{best_match['content']}<br><br><hr>{best_match['quiz']}"

    safe_prompt = html.escape(user_prompt)
    return (
        f"<b>AI Insight: \"{safe_prompt}\"</b><br><br>"
        "Artificial Intelligence focuses on solving complex problems by extracting patterns from data rather than hardcoded logic.<br><br>"
        "<b>Core Pillars:</b><br>"
        "• <b>Data Tensors:</b> Encoding raw text, audio, and visual inputs into multi-dimensional matrices.<br>"
        "• <b>Neural Architecture:</b> Passing tensors through parameterized transformation layers (e.g., Attention, Convolutions).<br>"
        "• <b>Optimization:</b> Minimizing loss via Backpropagation and Gradient Descent.<br><br>"
        "💡 <b>Explore topics directly from the Sidebar:</b><br>"
        "• <i>AI, ML, DL, KNN, Neural Networks</i><br>"
        "• <i>History of AI & Founder of AI</i><br>"
        "• <i>Turing & Tuning Test, How AI Helps</i>"
    )

def generate_ai_response(prompt: str, api_choice: str, gemini_key: str, openai_key: str, selected_model: str) -> str:
    if api_choice == "Google Gemini" and gemini_key.strip():
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key.strip())
            system_instruction = (
                "You are an expert, friendly AI Tutor. Your role is to teach and explain "
                "Artificial Intelligence, Machine Learning, Deep Learning, and Data Science concepts clearly. "
                "Use simple language, intuitive analogies, concise bullet points, and end with an interactive question or quiz."
            )
            model = genai.GenerativeModel(
                model_name=selected_model or "gemini-1.5-flash",
                system_instruction=system_instruction
            )
            response = model.generate_content(prompt)
            return html.escape(response.text).replace("\n", "<br>")
        except Exception as e:
            return f"⚠️ <b>Gemini API Notice:</b> {html.escape(str(e))}<br><br>(Falling back to built-in engine below)<br><br>" + query_offline_tutor(prompt)

    elif api_choice == "OpenAI" and openai_key.strip():
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key.strip())
            completion = client.chat.completions.create(
                model=selected_model or "gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an insightful AI Educator who explains AI concepts with clarity, real-world analogies, and interactive questions."},
                    {"role": "user", "content": prompt}
                ]
            )
            content = completion.choices[0].message.content or ""
            return html.escape(content).replace("\n", "<br>")
        except Exception as e:
            return f"⚠️ <b>OpenAI API Notice:</b> {html.escape(str(e))}<br><br>(Falling back to built-in engine below)<br><br>" + query_offline_tutor(prompt)

    return query_offline_tutor(prompt)

def update_xp_and_badge(points: int = 10):
    st.session_state.xp += points
    xp = st.session_state.xp
    if xp >= 100:
        st.session_state.current_badge = "🏆 AI Grandmaster"
    elif xp >= 60:
        st.session_state.current_badge = "⚡ Neural Architect"
    elif xp >= 30:
        st.session_state.current_badge = "🧠 Deep Explorer"
    else:
        st.session_state.current_badge = "🌱 AI Novice"

with st.sidebar:
    st.markdown("## ⚙️ AI Engine & Keys")
    engine_choice = st.selectbox(
        "Intelligence Provider",
        ["Built-in AI Tutor (Offline & Free)", "Google Gemini", "OpenAI"],
        help="Choose offline tutor or enter API keys for live cloud LLMs."
    )

    gemini_api_key = ""
    openai_api_key = ""
    selected_model = ""

    if engine_choice == "Google Gemini":
        gemini_api_key = st.text_input("Gemini API Key", type="password", value=os.environ.get("GEMINI_API_KEY", ""))
        selected_model = st.selectbox("Model", ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"])
        if not gemini_api_key:
            st.caption("🔑 Enter Gemini API key to enable live generation.")
    elif engine_choice == "OpenAI":
        openai_api_key = st.text_input("OpenAI API Key", type="password", value=os.environ.get("OPENAI_API_KEY", ""))
        selected_model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"])
        if not openai_api_key:
            st.caption("🔑 Enter OpenAI API key to enable live generation.")
    else:
        st.caption("⚡ **Built-in Tutor is Active:** Instant responses with zero API key requirement.")

    st.markdown("---")

    st.markdown('<div class="sidebar-section-title">🏆 Learning Rewards</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="rewards-box">
        <div class="reward-title">Total XP Earned</div>
        <div class="reward-points">{st.session_state.xp} XP</div>
        <div class="badge-pill">{st.session_state.current_badge}</div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(min(st.session_state.xp / 100.0, 1.0))

    st.markdown('<div class="sidebar-section-title">🎯 Quick AI Quiz</div>', unsafe_allow_html=True)
    with st.expander("📝 Test Your Knowledge (+15 XP)", expanded=False):
        quiz_q = "Which of the following is an Unsupervised Learning algorithm?"
        quiz_options = ["Linear Regression", "K-Means Clustering", "Random Forest Classifier", "Support Vector Machines"]
        user_choice = st.radio("Question:", quiz_options, index=None, key="sb_quiz_radio")
        if st.button("Check Answer", key="sb_quiz_submit"):
            if user_choice == "K-Means Clustering":
                st.success("🎉 Correct! K-Means discovers clusters without labels. +15 XP!")
                update_xp_and_badge(15)
                st.session_state.quizzes_completed += 1
                st.rerun()
            elif user_choice:
                st.error("❌ Not quite! K-Means Clustering is unsupervised. Try another!")

    st.markdown("---")

    st.markdown('<div class="sidebar-section-title">📚 Short AI Questions</div>', unsafe_allow_html=True)
    st.caption("Click any question to ask and learn instantly (+5 XP):")

    short_questions = [
        ("🤖 What is AI?", "What is Artificial Intelligence and how does it work?"),
        ("🍳 What is ML?", "Explain Machine Learning and its 3 main types."),
        ("👁️ What is DL?", "What is Deep Learning and how does it differ from ML?"),
        ("👥 What is KNN?", "Explain the K-Nearest Neighbors (KNN) algorithm with an analogy."),
        ("🧠 Neural Network", "How do Artificial Neural Networks learn with backpropagation?"),
        ("🧪 Turing & Tuning Test", "Explain the Turing Test and Model Hyperparameter Tuning."),
        ("📜 History of AI", "What is the history and timeline of Artificial Intelligence?"),
        ("🏛️ Founder of AI", "Who is the founder and pioneers of Artificial Intelligence?"),
        ("🩺 How AI Helps", "How does AI help humanity in healthcare, climate, and daily life?")
    ]

    for label, query in short_questions:
        if st.button(label, key=f"sq_{label}", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": query})
            reply = generate_ai_response(query, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            st.session_state.questions_asked += 1
            update_xp_and_badge(5)
            st.rerun()

    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

header_html = """
<div class="minimal-header">
    <div class="status-badge">
        <span class="status-dot"></span> AI Learning Hub Active
    </div>
    <div class="minimal-title">AI Intelligence <span>Hub</span></div>
    <p class="minimal-subtitle">Ask anything about Machine Learning, Neural Networks & Generative AI</p>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

if len(st.session_state.messages) == 0:
    st.markdown('<div class="topic-label">Featured Topics</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("🧠 Machine Learning", key="btn_main_ml", use_container_width=True):
            prompt = "What is Machine Learning and what are its main types?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            reply = generate_ai_response(prompt, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            update_xp_and_badge(5)
            st.rerun()
    with c2:
        if st.button("⚡ Neural Networks", key="btn_main_nn", use_container_width=True):
            prompt = "Explain Deep Learning and how artificial neural networks learn."
            st.session_state.messages.append({"role": "user", "content": prompt})
            reply = generate_ai_response(prompt, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            update_xp_and_badge(5)
            st.rerun()
    with c3:
        if st.button("👥 KNN Algorithm", key="btn_main_knn", use_container_width=True):
            prompt = "Explain K-Nearest Neighbors (KNN) algorithm with an analogy."
            st.session_state.messages.append({"role": "user", "content": prompt})
            reply = generate_ai_response(prompt, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            update_xp_and_badge(5)
            st.rerun()

    c4, c5 = st.columns(2)
    with c4:
        if st.button("🏛️ Founders of AI", key="btn_main_founders", use_container_width=True):
            prompt = "Who is the founder of Artificial Intelligence and who are its pioneers?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            reply = generate_ai_response(prompt, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            update_xp_and_badge(5)
            st.rerun()
    with c5:
        if st.button("🩺 How AI Helps", key="btn_main_helps", use_container_width=True):
            prompt = "How does AI help humanity in healthcare, climate, and daily life?"
            st.session_state.messages.append({"role": "user", "content": prompt})
            reply = generate_ai_response(prompt, engine_choice, gemini_api_key, openai_api_key, selected_model)
            st.session_state.messages.append({"role": "assistant", "content": reply})
            update_xp_and_badge(5)
            st.rerun()

else:
    st.markdown('<div class="chat-scroll-frame">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="bubble-user">{html.escape(msg["content"])}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'''<div class="bubble-bot">
                    <span class="bot-badge">● AI TUTOR</span>
                    <div>{msg["content"]}</div>
                </div>''',
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)

    col_r1, col_r2, col_r3 = st.columns([1, 2, 1])
    with col_r2:
        if st.button("🔄 New Conversation", key="btn_reset_chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

with st.form(key="chat_typing_space", clear_on_submit=True):
    col_input, col_btn = st.columns([8.5, 1.5])
    with col_input:
        user_query = st.text_input(
            label="Type your AI question",
            placeholder="Ask any question about AI, ML, DL, KNN, History...",
            label_visibility="collapsed",
            key="user_query_input"
        )
    with col_btn:
        submit_btn = st.form_submit_button("➔")

    if submit_btn and user_query.strip():
        cleaned_query = user_query.strip()
        st.session_state.messages.append({"role": "user", "content": cleaned_query})
        reply = generate_ai_response(cleaned_query, engine_choice, gemini_api_key, openai_api_key, selected_model)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.session_state.questions_asked += 1
        update_xp_and_badge(5)
        st.rerun()
