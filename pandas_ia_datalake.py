import json
import os
import shutil

import pandas as pd
from pandasai import SmartDatalake
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
    sdf_1 = pd.read_excel("report_1.xlsx")
    sdf_2 = pd.read_excel("report_2.xlsx")
    lake = SmartDatalake([sdf_1, sdf_2], config={"llm": llm})
    response = lake.chat(question)
    print(response)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pai.clear_cache()
    if os.path.exists('cache'):
        shutil.rmtree('cache')
    if os.path.exists('exports'):
        shutil.rmtree('exports')

    q1 = "What should I study to make the most money"

    response = process_query(q1, gpt=False)
