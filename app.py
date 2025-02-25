#others
#langchain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, BaseMessage, trim_messages
#langgraph
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
#typing extensions
from typing_extensions import Annotated, TypedDict
from typing import Sequence
#streamlit
import streamlit as st


GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

CHARACTERS = [
    'Friendly Mentor',
    'Survival Expert',
    'History Professor',
    'Custom Character',
]



st.title('Your Chatbot 🤖')
if 'messages' not in st.session_state:
    st.session_state.messages = [] 
    
# Getting Characters
st.sidebar.title('Characters')
character = st.sidebar.selectbox('Select Character', CHARACTERS)

if character == 'Custom Character':
    character = None
    custom_character = st.sidebar.text_input('Enter Custom Character Name')
    if custom_character:
        character = custom_character
        

st.sidebar.text(f'Character: {character}')

# Initializing Chat Model
# @st.cache_resource
# def get_model()
model = init_chat_model(
    'deepseek-r1-distill-llama-70b',
    model_provider='groq',
)
# initiatializing the whisper model for speech to text
whisper_model = init_chat_model(
    'distil-whisper-large-v3-en',
    model_provider='groq',
)

# Creating the parser
class Output(BaseModel):
    answer: str = Field(..., title='Answer to the prompt')


# Managing the Prompt Template
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "You are a helpful {character}. Answer all the questions to the best of your ability in the way a {character} would. "
                
            )
        ),
        MessagesPlaceholder(variable_name='messages')
    ]
)

class State(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    character: str


# Storing Messages in Session
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Defining Workflow To Persist Memory Of Messages
workflow = StateGraph(state_schema=State)

trimmer = trim_messages(
    max_tokens=3000,
    strategy='last',
    token_counter=model,
    include_system=True,
    allow_partial=True,
    start_on='human',
)

def call_model(state: State):
    trimmed_messages = trimmer.invoke(state['messages'])
    # prompt = prompt_template.invoke({
    #     'messages': trimmed_messages,
    #     'character': state['character']
    # })
    prompt= prompt_template.invoke(state)
    print(trimmed_messages)
    response = model.invoke(prompt)
    return {'messages': [response]}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

if 'memory' not in st.session_state:
    st.session_state.memory = MemorySaver()

memory = st.session_state.memory
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc123"}}

# Creating The Prompt Streamlit Component and Managing The Chat

st.sidebar.title('Input Type')
input_type = st.sidebar.radio('Select Type', ['Text', 'Speech'])

query = ''
# audio_query = st.audio_input(label='Record Your Prompt')

if input_type == 'Speech':
    audio_query = st.audio_input(label='Record Your Prompt')
    if audio_query:
        query = whisper_model.invoke(audio_query)
else:
    query = st.chat_input('Pass Your Prompt 🫠')
    

# Getting The Output
def get_output(app):
    
    try:
        output = app.invoke(input={
            'messages': past_messages,
            'character': character,
        }, config=config)
        current_output = output['messages'][-1].content
    except Exception as e:
        return None
    return current_output
    
    
def format_output(ans):
    return ans.split('</think>')[-1]

if query:
    st.chat_message('user').markdown(query)
    st.session_state.messages.append({'role': 'user', 'content': query})
    
    input_message = [HumanMessage(query)]
    past_messages = st.session_state.messages + input_message
    
    current_output = get_output(app)
    formated_output = format_output(current_output)
    
    if current_output:
        st.chat_message('assistant').markdown(formated_output)
        st.session_state.messages.append({'role': 'assistant', 'content': formated_output})
    else:
        st.error('Something went wrong! Please try again.')
    
    



