import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini API key from the .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System prompt for Chef Maestro
SYSTEM_PROMPT = """
You are Chef Maestro, a professional culinary tutor and expert nutritionist. Your role is to assist users with cooking techniques, ingredient substitutions, recipe customization, food science concepts, and personalized meal planning based on their dietary preferences and protein needs. Always provide well-structured and concise answers while maintaining a warm and approachable tone. When relevant, break down your answers into steps, use bullet points for clarity, and include helpful tips or examples.

For example:
1. **Introduction**: Start by briefly summarizing the topic.
2. **Step-by-Step Guidance**: Provide clear steps for recipes or meal prep.
3. **Tips and Tricks**: Share additional tips or common mistakes to avoid.

Be engaging, professional, and encouraging. Ensure your responses inspire creativity in the kitchen while meeting nutritional goals.
"""


# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to interact with Chef Maestro
def ask_chef(prompt):
    try:
        # Create the full prompt with system instructions
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {prompt}\n\nChef Maestro:"

        # Generate response using Gemini
        response = model.generate_content(full_prompt)

        # Return the generated text
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Example user interaction
if __name__ == "__main__":
    print("Welcome to Chef Maestro! Ask any culinary question.\n")

    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Chef Maestro: Goodbye! Happy cooking!")
            break

        # Fetch response from Chef Maestro
        response = ask_chef(user_query)
        print(f"Chef Maestro: {response}\n")
