import json
import asyncio
import os
import prompts_and_functions.prompts as prompts
from anthropic_api import generate_chapter_plan


def load_story_data():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def create_plan_prompt(data, start_chapter, end_chapter):
    prompt = f"Based on the following story information, create a plan for chapters {start_chapter} to {end_chapter}:\n\n"

    # Add a summary of previous chapters
    prompt += "Chapter Summaries:\n"
    for summary in data["chapter_summaries"]:
        prompt += f"Chapter {summary['chapter']}: {summary['summary']}\n\n"

    # Add information about characters
    prompt += "Characters:\n"
    for character in data["characters"]:
        prompt += f"{json.dumps(character, indent=2)}\n\n"

    # Add information about locations
    prompt += "Locations:\n"
    for location in data["locations"]:
        prompt += f"{json.dumps(location, indent=2)}\n\n"

    # Add plot points
    prompt += "Plot Points:\n"
    for plot_point in data["plot"]:
        prompt += f"{json.dumps(plot_point, indent=2)}\n\n"

    # Add themes
    prompt += "Themes:\n"
    for theme in data["themes"]:
        prompt += f"{json.dumps(theme, indent=2)}\n\n"

    # Add unresolved mysteries
    prompt += "Unresolved Mysteries:\n"
    for mystery in data["unresolved_mysteries"]:
        prompt += f"{json.dumps(mystery, indent=2)}\n\n"

    # Add key items
    prompt += "Key Items:\n"
    for item in data["key_items"]:
        prompt += f"{json.dumps(item, indent=2)}\n\n"

    # Add narrative style information
    prompt += "Narrative Style:\n"
    prompt += f"{json.dumps(data['narrative_style'], indent=2)}\n\n"

    # Add entities
    prompt += "Entities:\n"
    for entity in data["entities"]:
        prompt += f"{json.dumps(entity, indent=2)}\n\n"

    prompt = prompts.chapter_planner_prompt + prompt
    return prompt


async def main():
    story_data = load_story_data()
    start_chapter = len(story_data["chapter_summaries"]) + 1
    end_chapter = start_chapter + 9

    prompt = create_plan_prompt(story_data, start_chapter, end_chapter)

    print(f"Generating plan for Chapters {start_chapter}-{end_chapter}...")

    plan = await generate_chapter_plan(prompt)

    if plan:
        # Save the generated plan
        with open(
            f"chapter_plan_{start_chapter}_{end_chapter}.json", "w", encoding="utf-8"
        ) as f:
            f.write(plan)

        print(
            f"Chapter plan for Chapters {start_chapter}-{end_chapter} has been generated and saved."
        )
    else:
        print("Failed to generate chapter plan.")


if __name__ == "__main__":
    asyncio.run(main())
