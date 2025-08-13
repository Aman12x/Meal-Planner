import streamlit as st
from help import ask_chef
# Import the chatbot function from your Gemini-based chef module


def calculate_protein_needs(weight, age, gender, activity_level):
    """Calculate daily protein needs based on user parameters"""
    # Base protein needs (g/kg body weight)
    if activity_level == "Sedentary":
        protein_per_kg = 0.8
    elif activity_level == "Lightly Active":
        protein_per_kg = 1.0
    elif activity_level == "Moderately Active":
        protein_per_kg = 1.2
    elif activity_level == "Very Active":
        protein_per_kg = 1.4
    else:  # Extremely Active
        protein_per_kg = 1.6

    # Adjust for age
    if age >= 65:
        protein_per_kg += 0.2  # Older adults need more protein

    # Calculate total protein needs
    daily_protein = weight * protein_per_kg

    return round(daily_protein, 1)


def get_meal_prep_prompt(user_profile, protein_needs):
    """Generate a detailed prompt for meal prep based on user profile"""
    prompt = f"""
    Please create a personalized daily meal prep plan for me with the following requirements:
    
    **Personal Information:**
    - Age: {user_profile['age']} years
    - Weight: {user_profile['weight']} kg
    - Height: {user_profile['height']} cm
    - Gender: {user_profile['gender']}
    - Activity Level: {user_profile['activity_level']}
    - Dietary Preference: {user_profile['diet_preference']}
    
    **Nutritional Goals:**
    - Daily Protein Target: {protein_needs}g
    
    Please provide:
    1. A complete daily meal plan (breakfast, lunch, dinner, and 2 snacks)
    2. Protein content breakdown for each meal
    3. Preparation instructions for each meal
    4. Shopping list for all ingredients
    5. Any tips for meal prep and storage
    
    Make sure all meals align with my {user_profile['diet_preference']} dietary preference and help me reach my daily protein goal of {protein_needs}g.
    """
    return prompt


def main():
    # Streamlit UI setup
    st.set_page_config(page_title="Chef Maestro", page_icon="🍳", layout="wide")
    st.title("👨‍🍳 Chef Maestro: Your Culinary Tutor")

    # Create tabs for different functionalities
    tab1, tab2 = st.tabs(["💬 Ask Chef Maestro", "🥗 Personalized Meal Prep"])

    with tab1:
        # Sidebar for general questions
        with st.sidebar:
            st.header("About Chef Maestro")
            st.write("""
            Chef Maestro is your personal culinary tutor! 
            Ask questions about cooking techniques, recipes, ingredient substitutions, 
            or food science, and get detailed, step-by-step answers.
            """)
            st.write(
                "Type your question in the box below and let Chef Maestro guide you!"
            )
            st.markdown("**Examples of questions:**")
            st.write("- How do I make a perfect soufflé?")
            st.write("- What's the science behind caramelization?")
            st.write("- How can I replace eggs in baking?")

        # Initialize session state for general questions
        if "user_input" not in st.session_state:
            st.session_state.user_input = ""
        if "response" not in st.session_state:
            st.session_state.response = ""
        # Form for input and buttons
        with st.form(key="chef_form", clear_on_submit=False):
            # Input area for user questions
            user_input = st.text_input(
                "Ask Chef Maestro your culinary question:",
                value=st.session_state.user_input,
                key="user_input_box",
            )
            # Submit and Clear buttons in a row
            col1, col2 = st.columns([1, 1])  # Equal column widths
            with col1:
                submit = st.form_submit_button("Submit")
            with col2:
                clear = st.form_submit_button("Clear All")

        # Handle button clicks
        if submit:
            if user_input.strip() == "":
                st.warning("Please enter a question before submitting.")
            else:
                with st.spinner("Chef Maestro is cooking up an answer..."):
                    st.session_state.response = ask_chef(user_input)
                    st.session_state.user_input = (
                        user_input  # Store input in session state
                    )

        if clear:
            # Clear the session state variables directly
            st.session_state["user_input"] = ""
            st.session_state["response"] = ""

        # Display the response
        if st.session_state.response:
            st.success("Here's your answer:")
            st.markdown(st.session_state.response)

    with tab2:
        st.header("🥗 Get Your Personalized Meal Prep Plan")
        st.write(
            "Provide your details below to get a customized meal prep plan with calculated protein needs."
        )

        # Initialize session state for meal prep
        if "meal_prep_response" not in st.session_state:
            st.session_state.meal_prep_response = ""

        # User profile form
        with st.form(key="profile_form"):
            col1, col2 = st.columns(2)

            with col1:
                age = st.number_input("Age", min_value=16, max_value=100, value=30)
                weight = st.number_input(
                    "Weight (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1
                )
                gender = st.selectbox("Gender", ["Male", "Female"])

            with col2:
                height = st.number_input(
                    "Height (cm)", min_value=120, max_value=250, value=170
                )
                activity_level = st.selectbox(
                    "Activity Level",
                    [
                        "Sedentary",
                        "Lightly Active",
                        "Moderately Active",
                        "Very Active",
                        "Extremely Active",
                    ],
                )
                diet_preference = st.selectbox(
                    "Dietary Preference",
                    [
                        "Omnivore",
                        "Vegetarian",
                        "Vegan",
                        "Pescatarian",
                        "Keto",
                        "Paleo",
                        "Mediterranean",
                    ],
                )

            # Submit button
            get_meal_plan = st.form_submit_button("🍽️ Generate My Meal Prep Plan")

        # Handle meal prep form submission
        if get_meal_plan:
            # Calculate protein needs
            protein_needs = calculate_protein_needs(weight, age, gender, activity_level)

            # Create user profile
            user_profile = {
                "age": age,
                "weight": weight,
                "height": height,
                "gender": gender,
                "activity_level": activity_level,
                "diet_preference": diet_preference,
            }

            # Display calculated protein needs
            st.info(f"📊 Your calculated daily protein needs: **{protein_needs}g**")

            # Generate meal prep plan
            with st.spinner("Chef Maestro is preparing your personalized meal plan..."):
                meal_prep_prompt = get_meal_prep_prompt(user_profile, protein_needs)
                st.session_state.meal_prep_response = ask_chef(meal_prep_prompt)

        # Display meal prep response
        if st.session_state.meal_prep_response:
            st.success("🍽️ Here's your personalized meal prep plan:")
            st.markdown(st.session_state.meal_prep_response)

    # Footer
    st.markdown("""
    ---
    Built with desperation by a broke college student 
    """)


if __name__ == "__main__":
    main()
