import json
import time

from prompts_and_functions import prompts
from anthropic_api import process_with_claude
from openai_api import process_with_chatgpt
import asyncio
from prompts_and_functions.functions import *


def load_current_data():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_current_data(data):
    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


async def process_chapter(assistant_id, chapter_text, chapter_number):
    current_data = load_current_data()
    print(f"Processing Chapter {chapter_number}")

    # Create tasks for both API calls
    claude_task = asyncio.create_task(
        process_claude_summary(chapter_text, chapter_number)
    )
    chatgpt_task = asyncio.create_task(
        process_chatgpt_fields(assistant_id, chapter_text, chapter_number, current_data)
    )

    # Wait for both tasks to complete
    claude_result, chatgpt_function_calls = await asyncio.gather(
        claude_task, chatgpt_task
    )

    # Process Claude's chapter summary
    current_data["chapter_summaries"].append(claude_result)

    # Process ChatGPT's function calls
    for call in chatgpt_function_calls:
        function_name = call["name"]
        arguments = call["arguments"]

        try:

            if function_name == "create_character":
                result = create_character(**arguments)
                current_data["characters"].append(result)
            elif function_name == "update_character":
                result = update_character(**arguments)
                for i, char in enumerate(current_data["characters"]):
                    if char["name"] == result["name"]:
                        current_data["characters"][i].update(result["updates"])
                        break
            elif function_name == "delete_character":
                result = delete_character(**arguments)
                current_data["characters"] = [
                    c for c in current_data["characters"] if c["name"] != result["name"]
                ]

            elif function_name == "create_location":
                result = create_location(**arguments)
                current_data["locations"].append(result)
            elif function_name == "update_location":
                result = update_location(**arguments)
                for i, loc in enumerate(current_data["locations"]):
                    if loc["name"] == result["name"]:
                        current_data["locations"][i].update(result["updates"])
                        break
            elif function_name == "delete_location":
                result = delete_location(**arguments)
                current_data["locations"] = [
                    l for l in current_data["locations"] if l["name"] != result["name"]
                ]

            elif function_name == "create_plot_point":
                result = create_plot_point(**arguments)
                current_data["plot"].append(result)
            elif function_name == "update_plot_point":
                result = update_plot_point(**arguments)
                for i, plot in enumerate(current_data["plot"]):
                    if (
                        plot["chapter"] == result["chapter"]
                        and plot["event"] == result["event"]
                    ):
                        current_data["plot"][i].update(result["updates"])
                        break
            elif function_name == "delete_plot_point":
                result = delete_plot_point(**arguments)
                current_data["plot"] = [
                    p
                    for p in current_data["plot"]
                    if not (
                        p["chapter"] == result["chapter"]
                        and p["event"] == result["event"]
                    )
                ]

            elif function_name == "create_theme":
                result = create_theme(**arguments)
                current_data["themes"].append(result)
            elif function_name == "update_theme":
                result = update_theme(**arguments)
                for i, theme in enumerate(current_data["themes"]):
                    if theme["name"] == result["name"]:
                        current_data["themes"][i].update(result["updates"])
                        break
            elif function_name == "delete_theme":
                result = delete_theme(**arguments)
                current_data["themes"] = [
                    t for t in current_data["themes"] if t["name"] != result["name"]
                ]

            elif function_name == "create_unresolved_mystery":
                result = create_unresolved_mystery(**arguments)
                current_data["unresolved_mysteries"].append(result)
            elif function_name == "update_unresolved_mystery":
                result = update_unresolved_mystery(**arguments)
                for i, mystery in enumerate(current_data["unresolved_mysteries"]):
                    if mystery["description"] == result["description"]:
                        current_data["unresolved_mysteries"][i].update(
                            result["updates"]
                        )
                        break
            elif function_name == "delete_unresolved_mystery":
                result = delete_unresolved_mystery(**arguments)
                current_data["unresolved_mysteries"] = [
                    m
                    for m in current_data["unresolved_mysteries"]
                    if m["description"] != result["description"]
                ]

            elif function_name == "create_key_item":
                result = create_key_item(**arguments)
                current_data["key_items"].append(result)
            elif function_name == "update_key_item":
                result = update_key_item(**arguments)
                for i, item in enumerate(current_data["key_items"]):
                    if item["name"] == result["name"]:
                        current_data["key_items"][i].update(result["updates"])
                        break
            elif function_name == "delete_key_item":
                result = delete_key_item(**arguments)
                current_data["key_items"] = [
                    i for i in current_data["key_items"] if i["name"] != result["name"]
                ]

            elif function_name == "update_narrative_style":
                result = update_narrative_style(**arguments)
                current_data["narrative_style"] = result

            elif function_name == "create_entity":
                result = create_entity(**arguments)
                current_data["entities"].append(result)
            elif function_name == "update_entity":
                result = update_entity(**arguments)
                for i, entity in enumerate(current_data["entities"]):
                    if entity["name"] == result["name"]:
                        current_data["entities"][i].update(result["updates"])
                        break
            elif function_name == "delete_entity":
                result = delete_entity(**arguments)
                current_data["entities"] = [
                    e for e in current_data["entities"] if e["name"] != result["name"]
                ]

        except TypeError as e:
            print(f"TypeError in {function_name}: {e}")
            print(f"Arguments: {arguments}")
            # You might want to log this error or handle it in some way
            continue  # Skip this function call and continue with the next one

    save_current_data(current_data)
    print(f"Chapter {chapter_number} processed and data updated.")


async def process_claude_summary(chapter_text, chapter_number):
    prompt = f"""Summarize Chapter {chapter_number} in 200-250 words. Focus on:
    1. Key plot developments
    2. Character introductions or significant character moments
    3. Important revelations or mysteries
    4. Major scene changes or settings introduced

    Provide only the summary, with no additional text or explanations. Do not provide the word count. Include no newlines or anything other than a plain string of text."""
    summary = await process_with_claude(prompt + "\n\n" + chapter_text)
    return {"chapter": chapter_number, "summary": summary}


async def process_chatgpt_fields(
    assistant_id, chapter_text, chapter_number, current_data
):
    chatgpt_data = current_data.copy()
    chatgpt_data.pop("chapter_summaries", None)
    function_calls = await process_with_chatgpt(
        assistant_id, chapter_text, chapter_number, chatgpt_data
    )

    # Correct the typo
    for call in function_calls:
        if call["name"] == "create_character" and "signficance" in call["arguments"]:
            call["arguments"]["significance"] = call["arguments"].pop("signficance")

    return function_calls


async def process_all_chapters():
    assistant_id = "asst_BYdqyXTxZ8C5LC5AoJCqpEin"
    for chapter_number in range(11, 20):
        with open(f"chapters/chapter_{chapter_number}.txt", "r", encoding="utf-8") as f:
            print("reading chapter data for chapter " + str(chapter_number) + "... ")
            chapter_text = f.read()
            print("processing chapter...")
            await process_chapter(assistant_id, chapter_text, chapter_number)
            print("chapter processed.")
            print("sleeping for 60 seconds...")
            time.sleep(60)
            print("awake. beginning chapter " + str(chapter_number + 1))
