import json
import asyncio
import os
from chapter_planner import create_plan_prompt, generate_chapter_plan
from generate_chapter import create_chapter_prompt, generate_chapter_gpt4, generate_chapter_claude
from process_chapters import process_chapter
from openai_api import create_assistant


async def generate_and_process_chapters(start_chapter, num_chapters, use_planner=True):
    assistant_id = "asst_BYdqyXTxZ8C5LC5AoJCqpEin"

    if use_planner:
        # Generate chapter plan
        story_data = load_story_data()
        prompt = create_plan_prompt(story_data, start_chapter, start_chapter + num_chapters - 1)
        plan = await generate_chapter_plan(prompt)
        chapter_plan = json.loads(plan)
    else:
        with open("chapter_plan_20_29_copy.json", "r", encoding="utf-8") as f:
            f = str(f.read())
            chapter_plan = json.loads(f)

    for chapter in chapter_plan:
        chapter_number = chapter["chapter_number"]
        print(f"Generating Chapter {chapter_number}...")

        # Generate chapter
        story_data = load_story_data()
        prompt = create_chapter_prompt(story_data, chapter_number)
        prompt = "The following JSON is what the following chapter is to be composed of. Follow it closely\n" + str(chapter_plan[chapter_number - start_chapter]) + prompt
        print(prompt)
        claude_chapter = await generate_chapter_claude(prompt)

        # Save generated chapters
        os.makedirs("chapters", exist_ok=True)
        with open(f"chapters/chapter_{chapter_number}_claude.txt", "w", encoding="utf-8") as f:
            f.write(claude_chapter)

        print(f"Chapter {chapter_number} generated and saved.")

        # Process chapter
        print(f"Processing Chapter {chapter_number}...")
        await process_chapter(assistant_id, claude_chapter, chapter_number)
        print(f"Chapter {chapter_number} processed.")


def load_story_data():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)


async def main():
    start_chapter = 20  # Adjust this to your current chapter number
    num_chapters = 10  # Number of chapters to generate and process
    use_planner = False  # Set to False if you don't want to use the chapter planner

    await generate_and_process_chapters(start_chapter, num_chapters, use_planner)


if __name__ == "__main__":
    asyncio.run(main())