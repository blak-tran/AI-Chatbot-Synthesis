# Vietnamese AI Chatbot with Transformer

This is an AI chatbot powered by a transformer model, designed to interact with users in Vietnamese. The chatbot can handle various tasks, such as answering questions, providing recommendations, and analyzing users based on their age, gender, and interests. It also integrates with speech-to-text and text-to-speech models for seamless communication.

## Project Overview

The goal of this project is to create an intelligent and interactive chatbot capable of understanding and generating human-like responses in Vietnamese. We leverage the transformer model, a cutting-edge deep learning architecture in the field of Natural Language Processing (NLP), to achieve this objective. The chatbot is trained on a diverse dataset to ensure accurate and contextually relevant responses.

## Getting Started

### Clone the Repository
To use the Transformer chatbot:

clone https://github.com/blak-tran/vietnamese_chatbot_research.git

![Chatbot using Transformer Architecture](https://github.com/blak-tran/AI-Chatbot-Synthesis/blob/da19064f92e8aa2da7d6dfacc4bf236ac38a18fb/assets/transformer_architect.png)


## Features

User interaction
Multi-task handling, including answering questions, providing recommendations, and more
Context-aware responses, resulting in more natural interactions
User analysis
Integration with speech-to-text and text-to-speech models

## Technologies Used

- **Python:** The core programming language used for building the chatbot.
- **Tensorflow:** Deep learning framework utilized for implementing the transformer model.
- **Transformers Library:** Leveraged for accessing pre-trained transformer models.
- **FastAPI:** Web framework used for building the chatbot's user interface.

## Getting Started

### Usage
To use the chatbot, follow these steps:
1. **Setup**
 We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions. The codebase also depends on a few Python packages, most notably OpenAI's tiktoken for their fast tokenizer implementation.
pip install -r requirement.txt

2. **Inference**
   ```bash
   uvicorn t2s:app --host 172.17.12.221 --port 8000
   uvicorn s2t:app --host 172.17.12.221 --port 8000
   uvicorn user_analyst_api:app --host 172.17.12.221 --port 8000
   python main_flow_inference.py 
