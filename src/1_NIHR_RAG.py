import streamlit as st
import pandas as pd
import vector_store as vs

# Set a tab title
st.set_page_config(page_title="NIHR RAG")
#st.set_page_config(page_title="NIHR Awards Data", page_icon="📈")

# Set a title for your app
st.title("NIHR: Semantic Search using RAG")
#st.sidebar.success("Select a demo above.")

#App logo:
logo_img = "https://s3-eu-central-1.amazonaws.com/aws-ec2-eu-central-1-opendatasoft-staticfileset/nihr/logo?tstamp=16492314190455942"
st.logo(logo_img, link="https://sense.odp.nihr.ac.uk/public/", icon_image=None)

#sidebar image
# st.sidebar.image("https://s3-eu-central-1.amazonaws.com/aws-ec2-eu-central-1-opendatasoft-staticfileset/nihr/logo?tstamp=16492314190455942", use_column_width=True)

# Add background image
# st.markdown(
#     """
#     <style>
#     header[data-testid="stHeader"]{
#         background-image: url(https://s3-eu-central-1.amazonaws.com/aws-ec2-eu-central-1-opendatasoft-staticfileset/nihr/logo?tstamp=16492314190455942);
#         background-repeat: none;
#         background-size: contain;
#         height: 5%;
#     }
    
#     section[data-testid="stSidebar"] {
#         top: 10%; 
#       }
#     </style>""",
#     unsafe_allow_html=True,
# )
# Welcome message
st.markdown("""
Welcome to NIHR RAG - Your repository for NIHR supported research across the UK

**Please Note:**

* For best results, ensure your prompts relevant health data.
* Please do not upload personally identifiable information.

We're here to help you discover healthcare research around the UK. Feel free to ask questions to inform results from the NIHR Open Data.
""")

#experimentally removed to be replaced with background image variant on top of the program
st.markdown("""<hr style="border-color: #e0e0e0; height: 1px; background-image: none;">""", unsafe_allow_html=True)


# Text input for problem with placeholder
st.subheader("What kind of healthcare research are you interested in?")
st.markdown("""For example:

“How many studies are linked to cardiovascular diseases?”

“List different disease areas within cardiovascular research.” 

""")

problem = st.text_input("What question would you want to answer with this data?", key="problem")

button_run_pressed = st.button("load data")

if button_run_pressed:

    st.write(vs.display_info())

# Function to generate prompt feedback (replace with actual API call logic)
def get_better_prompt(original_prompt):
    # Placeholder logic for API call
    better_prompt = "...a suggested improvement based on your prompt"
    return better_prompt

# Generate prompt feedback based on user input (assuming API call)
if problem:  # Assuming 'problem' is a boolean variable
  better_prompt = get_better_prompt(problem)
  prompt_assessment = f"Your prompt could be improved. How about {better_prompt}?"
  link_text = "Learn more abour prompt development [here](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)."

  st.markdown(prompt_assessment)
  st.markdown(link_text)

  # Improved readability with better indentation and variable name
  new_prompt = st.text_input("Would you like to refine your prompt further?")
  if new_prompt:
      problem = new_prompt  # Update 'problem' with the user's new prompt (if provided)

# Submit button with conditional enabling
submit = st.button('Generate data analysis', disabled=not (problem))

st.markdown("""<hr style="border-color: #e0e0e0; height: 1px; background-image: none;">""", unsafe_allow_html=True)

st.subheader("Here's a summary of the analysis")
if submit:
    with st.spinner(text="This may take a moment..."):
        # Placeholder for API analysis logic
        text2 = "API output (replace with analysis results)"
    st.write(text2)

# Create two empty containers for analysis
data1, data2 = st.columns(2)

text_result = "This is the text result"
graph_result = "This is the graphical result"

# Write text to each container
data1.write(text_result)
data2.write(graph_result)

# Add a background color using CSS style
def grey_background():
  """
  Function to set a grey background style.
  """
  st.markdown(
      """<style>
      .placeholder {
        background-color: #F5F5F5;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 10px;
        display: inline-block;
      }
      </style>""",
      unsafe_allow_html=True,
  )

grey_background()

# Add the class to the containers
data1.empty().className = "placeholder"
data2.empty().className = "placeholder"

st.markdown("""<hr style="border-color: #e0e0e0; height: 1px; background-image: none;">""", unsafe_allow_html=True)

st.subheader("We've checked the data and result for you. This is what we found")

# API response on data assessment
data_assessment = "Data assessment API response"

# API response on data assessment
data_citation = "Data citation to appear when pulling data from Google"

# API response on data assessment
data_reasoning = "Why Google chose this response"


# Create four empty containers
container1, container2, container3 = st.columns(3)


# Write text to each container
container1.write(data_assessment)
container2.write(data_citation)
container3.write(data_reasoning)

st.markdown("""<hr style="border-color: #e0e0e0; height: 1px; background-image: none;">""", unsafe_allow_html=True)

# Section for choosing data source
st.subheader("Find out more about the platform")

st.markdown("""
 _*This is a proof of concept built using Google VertexAI as part of the NIHR AI Hackathon, Sep 2024._

For feedback or more information, please contact us at inforequest@nihr.ac.uk
""")
