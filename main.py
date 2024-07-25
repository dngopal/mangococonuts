# This is the basic AI to help screen for postpartum depression
# Uses Llama

import json
from llamaapi import LlamaAPI

#INSERT YOUR OWN API TOKEN
api_token = "API TOKEN"


llama = LlamaAPI(api_token)

# API Requests
api_request_json = {
    "messages": [
        {"role": "user", "content": "What does no color change mean for my test result?"},
        {"role": "user", "content": "What does a color change mean for my test result?"},
        {"role": "user", "content": "What if I can't tell if there's a color change in my test result?"}
    ],
    "functions": [
        {
            "name": "get_test_rests",
            "description": "Describe the meaning of the user's test results",
            "parameters": {
                "type": "object",
                "properties": {
                    "result": {
                        "type": "string",
                        "color change": "if there was a color change, they are more at-risk of postpartum depression",
                        "no color change": "if there was no color change, they were not found to be at-risk for postpartum depression",
                        "Unable to identify color change": "Results are unclear, so re-test!"
                    },
                },
            },
        }
    ],
    "stream": False,
    "function_call": "get_test_results",
}

# Execute the Request
response = llama.run(api_request_json)
print(json.dumps(response.json(), indent=2))

