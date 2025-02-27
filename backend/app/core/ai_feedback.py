from openai import OpenAI
import os
from dotenv import load_dotenv
from . import pylint_checker, ast_checker

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def analyze_and_fix_code(code: str):
    """Runs Pylint & AST analysis, then asks OpenAI to fix issues."""
    try:
        # Get static analysis results
        pylint_feedback = pylint_checker.run_pylint(code)
        ast_feedback = ast_checker.analyze_code_with_ast(code)

        # Format feedback for OpenAI prompt
        full_feedback = f"""
        You are a programming expert who reviews and improves code. 
        Your task is to:
        
        1. **Identify the programming language.**
        2. **Analyze the code for errors, bad practices, and inefficiencies.**
        3. **Fix all detected issues while maintaining functionality.**
        4. **Apply best coding practices** (error handling, structured logging, type hints).
        5. **Return the improved code in Markdown format**, specifying the correct language.
        
        Here is the submitted code:
        ```python
        {code}
        ```
        
        ### Rules:
        - **Replace print-based errors with proper exception handling (`raise Exception(...)`).**
        - **Use structured logging instead of appending history as strings.**
        - **Add Python type hints where applicable.**
        - **Ensure that global execution is inside `if __name__ == "__main__":`.**
        - **Only return the improved code, do not include explanations.**
        """


        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Python expert who reviews and improves code."},
                {"role": "user", "content": full_feedback}
            ]
        )

        # Extract the fixed code
        return response.choices[0].message.content
    except Exception as e:
        return f"OpenAI API Error: {e}"