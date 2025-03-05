# Chatbot with ChromaDB and OpenAI  

This project is a simple chatbot that finds relevant answers from stored knowledge using **ChromaDB** and **OpenAI embeddings**.  

## How It Works  
1. You provide a **query** (a question or text input).  
2. The chatbot searches its database (**ChromaDB**) for similar content.  
3. If a relevant match is found (with a confidence score of 0.7 or higher), it returns the best results.  
4. If no good match is found, it tells you that no relevant answers are available.  

## How to Run  
Run the script with a query:  
```sh
python chatbot.py "Your query here"

