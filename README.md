# Chatbot with ChromaDB and OpenAI
This project is a simple chatbot that finds relevant answers from stored knowledge using ChromaDB and OpenAI embeddings.

How It Works:
1.You provide a query (a question or text input).
2.The chatbot searches its database (ChromaDB) for similar content.
3.If a relevant match is found (with a confidence score of 0.7 or higher), it returns the best results.
4.If no good match is found, it tells you that no relevant answers are available.
How to Run:
``` python chatbot.py "Your query here" ```
Requirements:
1.Python
2.argparse, langchain, ChromaDB, OpenAI API
Use Cases:
1.Quickly retrieving relevant information
2.Building a chatbot that understands natural language
3.Storing and searching large text datasets
