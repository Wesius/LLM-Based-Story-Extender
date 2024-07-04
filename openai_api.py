import json
import os
from openai import AsyncOpenAI
from prompts_and_functions.functions import llm_functions
from prompts_and_functions.prompts import pre_prompt_gpt
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)


def create_assistant():
    assistant = openai_client.beta.assistants.create(
        name="Story Analyzer",
        instructions=pre_prompt_gpt,
        model="gpt-4o-2024-05-13",
        tools=llm_functions,
    )
    return assistant.id


async def process_with_chatgpt(
    assistant_id, chapter_text, chapter_number, current_data
):
    print(f"Processing chapter {chapter_number}...")

    print("Creating thread...")
    thread = await openai_client.beta.threads.create()
    print(f"Thread created with ID: {thread.id}")

    print("Creating message in thread...")
    message = await openai_client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"Chapter {chapter_number} text: {chapter_text}\n\nCurrent story data, in json format: {json.dumps(current_data, indent=2)}",
    )
    print(f"Message created with ID: {message.id}")

    print("Creating run...")
    run = await openai_client.beta.threads.runs.create(
        thread_id=thread.id, assistant_id=assistant_id, instructions=pre_prompt_gpt
    )
    print(f"Run created with ID: {run.id}")

    function_calls = []

    while True:
        run = await openai_client.beta.threads.runs.retrieve(
            thread_id=thread.id, run_id=run.id
        )

        if run.status == "completed":
            break
        elif run.status in ["failed", "cancelled", "expired"]:
            print(f"Run ended with status: {run.status}")
            if run.last_error:
                print(f"Error: {run.last_error}")
            return []
        elif run.status == "requires_action":
            print("Run requires action. Processing tool calls...")
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = []

            for tool_call in tool_calls:
                print(f"Processing tool call: {tool_call.function.name}")
                function_calls.append(
                    {
                        "name": tool_call.function.name,
                        "arguments": json.loads(tool_call.function.arguments),
                    }
                )

                tool_outputs.append(
                    {
                        "tool_call_id": tool_call.id,
                        "output": json.dumps({"status": "acknowledged"}),
                    }
                )

            print("Submitting tool outputs...")
            run = await openai_client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id, run_id=run.id, tool_outputs=tool_outputs
            )

    print(f"Run completed. Total function calls: {len(function_calls)}")
    return function_calls


async def generate_chapter_gpt4(prompt):
    response = await openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a skilled author, tasked with continuing a novel based on the provided story information.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=4000,
        temperature=0.7,
    )
    return response.choices[0].message.content
