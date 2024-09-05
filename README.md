The project is a plagiarism detection system that builds on a combination of rule-based algorithms and AI-enhanced models to offer a more refined solution for detecting code plagiarism. We implemented a web-based interface where users can submit two code snippets, and the system will analyze them for similarities.

Technologies Used:
Frontend:

The interface is built using HTML, CSS, and Flask templates.
The page has two side-by-side text boxes where users input code snippets, and after submission, the result is displayed—either "Plagiarism Detected" or "No Plagiarism Detected."
Backend:

Flask is used to handle requests and interact between the frontend and the plagiarism detection models.
It processes the user input and passes it to the core plagiarism checker.
Core Plagiarism Checker:
The system consists of two main components:

Rule-Based Similarity:

This part compares code structures like loops, variable names, and syntax patterns. The goal is to detect simple transformations such as renaming variables or slightly restructuring loops without affecting the underlying logic.
This helps in catching common tricks used to bypass plagiarism detection systems that rely only on text comparison.
AI-Enhanced Model (BERT):

BERT (Bidirectional Encoder Representations from Transformers), a pre-trained transformer-based model from Hugging Face, is used to capture deeper semantic similarities between the two code snippets.
We leverage BERT to extract contextual embeddings from both code snippets, allowing us to capture not only surface-level syntax but also deeper functional similarities.
By applying cosine similarity between the embeddings of the two code snippets, we quantify the similarity, making the detection more robust than simple keyword matching.
Training and Performance:
The AI model uses BERT embeddings pre-trained on large datasets. While we did not specifically fine-tune the BERT model on code, its pretrained capabilities allow us to capture meaningful similarities.
We evaluated performance by testing against a variety of code snippets including common algorithms like BFS and Kth largest element, ensuring the model identifies genuine plagiarism without flagging common logic used in these algorithms.
Challenges and Key Features:
False Positives: Early versions of the system flagged common algorithms as plagiarized. We improved the rule-based system to handle known code patterns and refined BERT’s similarity thresholds to better distinguish between true plagiarism and commonly shared logic.
User Interface: The website is designed to be simple, with a gradient background, easy navigation, and responsive elements. It also includes a favicon for branding consistency.
Conclusion:
The combination of rule-based methods and BERT’s advanced semantic analysis offers a powerful solution for plagiarism detection in code, improving accuracy and handling subtle transformations. The system is flexible, expandable, and integrates modern AI technologies with traditional comparison approaches, making it a robust tool for real-world plagiarism checking in programming environments.
