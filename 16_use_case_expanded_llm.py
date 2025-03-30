# Interact with OpenAI API
import os
import openai
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from datasets import load_dataset


# Securly save the API key locally
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Model name
llm_model = "gpt-3.5-turbo"

# Initialize the model with required parameter
chat = ChatOpenAI(temperature=0.0, model=llm_model)

# Define the output schema
result_schema = ResponseSchema(name="result",
                             description="Is this text content has any \
                                indication of any crime or confiction?. \
                                If yes, respond with 'yes'. If no, respond \
                                with 'no'")
name_schema = ResponseSchema(name="name",
                              description="If yes who has committed?,\
                              if no, just leave empty space")
entity_type_schema = ResponseSchema(name="entity",
                                    description="If yes, is it a person or organization\
                                    involved in it?")

response_schemas = [result_schema, 
                    name_schema,
                    entity_type_schema]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()


ds = load_dataset("ashraq/financial-news-articles")#Unused

# Input text to process
text_content = """
Traveling to have a business meeting takes the fun out of the trip.\
Especially if you have to prepare a presentation. I would suggest holding \
the business plan meetings here then take a trip without any formal business meetings.\
I would even try and get some honest opinions on whether a trip is even desired or \
necessary. As far as the business meetings, I think it would be more productive to try\
and stimulate discussions across the different groups about what is working and what is not.\
Too often the presenter speaks and the others are quiet just waiting for their turn. \
The meetings might be better if held in a round table discussion format.\
My suggestion for where to go is Austin. Play golf and rent a ski boat and jet ski's. \
Flying somewhere takes too much time. John Mcthy is involved in fraud investigation\
"""

# Prompt template
template_text_processing = """\
For the following text, extract the following information:

result: Is this text content has any \
    indication of any crime or confiction?. \
    If yes, respond with 'yes'. If no, respond \
    with 'no'

name: If yes who has committed?,\
    if no, just leave empty space.

entity: If yes, is it a person or organization\
        involved in it?

text: {text_content}

{format_instructions}
"""

prompt = ChatPromptTemplate.from_template(template=template_text_processing)
messages = prompt.format_messages(text_content=text_content, 
                                format_instructions=format_instructions)
# Return the response
response = chat(messages)
output_dict = output_parser.parse(response.content)
print(output_dict)

# TODO:Retrive multiple input entries from the huggingface database
# TODO: Write processed output entries to the database