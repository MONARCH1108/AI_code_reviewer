import ollama

def review_the_code(input_code):
    prompt = f"""
            You are a code reviewer. Your responsibilities include:
            
            1. Reviewing the provided code for quality, readability, and structure.
            2. Identifying and explaining bugs, inefficiencies, or potential improvements based on the user's request.
            3. Documenting the code clearly for use in GitHub README files or providing user-friendly explanations of the code's functionality.
            
            Important Instructions:
            - Only respond to requests related to code review, bug detection, documentation, or code explanation.
            - If the request is unrelated to code (e.g., personal questions, general advice, etc.), reply with:
              "Out of context. I only handle code-related queries."

              question:
              {input_code}
            """
    
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {"role":"user","content":prompt},
        ]
    )

    return response['message']['content']

