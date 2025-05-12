from openai import OpenAI

client = OpenAI(
    api_key=PUT_API_KEY_HERE
)

# This is a client of bpy
import http.client

import argparse
import sys
import ast

def demo_call(prompt):
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
        
    )

    text = response.output_text
    
    return text

def isolate_python(raw_text):
    text_components = raw_text.split('```')
    dialogue1 = text_components[0]
    code_block = text_components[1]
    
    py_str = code_block.removeprefix("python")    
    
    py_code = ast.literal_eval(f"'''{py_str}'''")
    return py_code

def request(message):
    conn = http.client.HTTPConnection('localhost', 8000)
    conn.request('POST', '/', body=message.encode('utf-8'))
    
    response = conn.getresponse().read().decode()
    conn.close()
    return response
   
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--np', type=str, default='2m radius sphere')
    args = parser.parse_args(sys.argv[1:])
    prompt = "Write me code that makes a geometry node tree with the Blender Python API (version 4.4.3). Make geometry nodes that form a " + args.np + "." 
    
    error_list = []
    
    response, n = None, 0
    while not response == "OK":
        n += 1
        print(n, ". ", end="")
        raw_text = demo_call(prompt)
        py_code = isolate_python(raw_text)
        response = request(py_code)
        print(response)
        error_list.append(response)
        prompt_ad = "\nYou gave me this code:\n" + py_code + "\nThe most recent error is " + response + ", but the list of errors is " + str(error_list)
        prompt += prompt_ad
    print("\nwith...\n", py_code)
        
if __name__ == "__main__":
    main()
