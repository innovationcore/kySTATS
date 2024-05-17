

import json
import os
import shutil
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.llm.local_llm import LocalLLM
import pandasai as pai

with open('config.json') as user_file:
    config = json.load(user_file)


llm_api_key = config['llm_api_key']
llm_api_base = config['llm_api_base']
openai_api_key = config['openai_api_key']


def process_query(question, gpt=False):

    adapter_id = ""

    if(gpt):
        llm = OpenAI(api_token=openai_api_key)
        adapter_id = 'GPT'
    else:
        llm = LocalLLM(api_key=llm_api_key, api_base=llm_api_base, model=adapter_id, max_tokens=config['max_tokens'])

    print('Using model:', adapter_id)
    sdf = SmartDataframe("report_1.xlsx", {"enable_cache": False}, config={"llm": llm})

    response = sdf.chat(question)
    print(type(response))
    print(response)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pai.clear_cache()
    if os.path.exists('cache'):
        shutil.rmtree('cache')
    if os.path.exists('exports'):
        shutil.rmtree('exports')

    q1 = "Provide a dataframe with the top 5 postsecondary institutions by enrollment size."
    q2 = "Provide a fancy chart with the top 5 postsecondary institutions by enrollment size."
    q3 = "What are the top postsecondary institutions by enrollment size?"

    response = process_query(q2, gpt=False)

#