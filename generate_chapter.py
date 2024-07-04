import json
import asyncio
import os
from dotenv import load_dotenv
from anthropic_api import generate_chapter_claude

load_dotenv()

def load_story_data():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def create_chapter_prompt(data, chapter_number):
    prompt = f"Write Chapter {chapter_number} of the story based on the following information:\n\n"

    # Add a summary of previous chapters
    prompt += "Chapter Summaries:\n"
    for summary in data['chapter_summaries']:
        prompt += f"Chapter {summary['chapter']}: {summary['summary']}\n\n"

    # Add information about characters
    prompt += "Characters:\n"
    for character in data['characters']:
        prompt += f"{json.dumps(character, indent=2)}\n\n"

    # Add information about locations
    prompt += "Locations:\n"
    for location in data['locations']:
        prompt += f"{json.dumps(location, indent=2)}\n\n"

    # Add plot points
    prompt += "Plot Points:\n"
    for plot_point in data['plot']:
        prompt += f"{json.dumps(plot_point, indent=2)}\n\n"

    # Add themes
    prompt += "Themes:\n"
    for theme in data['themes']:
        prompt += f"{json.dumps(theme, indent=2)}\n\n"

    # Add unresolved mysteries
    prompt += "Unresolved Mysteries:\n"
    for mystery in data['unresolved_mysteries']:
        prompt += f"{json.dumps(mystery, indent=2)}\n\n"

    # Add key items
    prompt += "Key Items:\n"
    for item in data['key_items']:
        prompt += f"{json.dumps(item, indent=2)}\n\n"

    # Add narrative style information
    prompt += "Narrative Style:\n"
    prompt += f"{json.dumps(data['narrative_style'], indent=2)}\n\n"

    # Add entities
    prompt += "Entities:\n"
    for entity in data['entities']:
        prompt += f"{json.dumps(entity, indent=2)}\n\n"

    prompt += f"\nWrite Chapter {chapter_number} in approximately 2000-3000 words. Advance the plot, develop characters, and maintain consistency with the existing story elements. Feel free to introduce new elements as needed to create an engaging narrative."

    return prompt