from gpt_j.Basic_api import simple_completion
import openai

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

def gpt_j(prompt, temp):
    resp = simple_completion(prompt, 
            length=2048, 
            temp=temp, 
            top=3.0)

    return resp


def gpt_3(prompt, temper, engine):
    response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=temper,
    max_tokens=1800,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    #best_of =1,
    stop=["Input"]
    )

    return response
