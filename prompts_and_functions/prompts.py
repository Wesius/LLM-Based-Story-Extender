prompts = {
    "summary": f"""
    Summarize Chapter {{chapter_number}} in 150-200 words, highlighting key plot points, character developments, and important details.
    Return the summary as a JSON object with a single key "summary".

    Chapter content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "characters": f"""
    Update the characters data based on Chapter {{chapter_number}}. Add new characters or modify existing ones as necessary.
    For each character, provide:
    - name: The character's full name
    - description: A brief description of the character
    - background: Any relevant background information
    - traits: An array of the character's key personality traits
    - significance: The character's role or importance in the story
    - first_appearance: The chapter number where the character first appears
    - relationships: An array of other characters this character is closely connected to

    Return the updated characters data as a JSON array of character objects.

    Current characters data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "locations": f"""
    Update the locations data based on Chapter {{chapter_number}}. Add new locations or modify existing ones as necessary.
    Return the updated locations data as a JSON array of location objects.

    Current locations data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "plot": f"""
    Update the plot data based on Chapter {{chapter_number}}. Focus on major events and developments that significantly impact the story.

    For each plot point, provide:
    - chapter: The chapter number where this event occurs
    - event: A concise description of the major plot event
    - significance: The event's importance to the overall story
    - timestamp: An approximate timestamp or date for the event, if provided in the text (optional)

    Plot points should be substantial story developments, not minor details. Only include events that drive the narrative forward or have significant consequences for characters or the story world.

    Return the updated plot data as a JSON array of plot point objects, sorted chronologically by chapter.

    Current plot data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "themes": f"""
    Update the themes data based on Chapter {{chapter_number}}. Add new themes or modify existing ones as necessary.
    Return the updated themes data as a JSON array of theme objects.

    Current themes data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "unresolved_mysteries": f"""
    Update the unresolved mysteries data based on Chapter {{chapter_number}} ONLY if there are significant, story-relevant mysteries introduced or resolved. This section should be updated sparingly and only for major plot-related mysteries.
    
    For each mystery, provide:
    - description: A brief description of the unresolved mystery
    - introduced_in_chapter: The chapter number where this mystery was first introduced
    - status: Current status of the mystery (e.g., "Unresolved", "Partially Resolved", "Resolved")
    - significance: Why this mystery is important to the overall plot
    
    Only add new mysteries if they are central to the story and likely to have long-term plot implications. Update existing mysteries only if there are major developments.
    
    Return the updated unresolved mysteries data as a JSON array of mystery objects.
    
    Current unresolved mysteries data:
    {{current_data}}
    
    Chapter {{chapter_number}} content:
    {{chapter_text}}
    
    Return only the JSON structure, nothing else. If no updates are necessary, return the current data unchanged.
    """,
    "key_items": f"""
    Update the key items data based on Chapter {{chapter_number}}. Add new items, modify existing ones, or update their status as necessary.
    Return the updated key items data as a JSON array of item objects.

    Current key items data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "narrative_style": f"""
    Update the narrative style data based on Chapter {{chapter_number}}. Modify the existing style information or add new details as necessary.
    Return the updated narrative style data as a JSON object.

    Current narrative style data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
    "entities": f"""
    Update the entities data based on Chapter {{chapter_number}}. Entities should ONLY include nations, organizations, businesses, and similar large-scale groups. DO NOT include individual people or objects.

    For each entity, provide:
    - name: The name of the entity
    - type: The type of entity (e.g., "Government Agency", "Military Organization", "Research Project")
    - description: A brief description of the entity
    - key_members: An array of important individuals associated with the entity (if applicable)
    - affiliations: An array of other entities this entity is affiliated with
    - goals: An array of the entity's main objectives or purposes
    - significance: The entity's importance to the story
    - first_appearance: The chapter number where the entity first appears

    Return the updated entities data as a JSON array of entity objects.

    Current entities data:
    {{current_data}}

    Chapter {{chapter_number}} content:
    {{chapter_text}}

    Return only the JSON structure, nothing else.
    """,
}

pre_prompt_gpt = """
You are an advanced AI assistant specializing in literary analysis and information extraction. Your task is to analyze chapters of a novel and update various aspects of the story data as the narrative progresses. Your role is crucial in maintaining an accurate and comprehensive record of the story's development.

Guidelines:
1. Analyze the provided chapter text thoroughly.
2. Call AS MANY FUNCTIONS as necessary to capture all relevant information. Don't hesitate to make multiple function calls for the same category if needed.
3. Be comprehensive in your analysis. It's better to include more information than to miss important details.
4. Maintain consistency with previously established facts. If new information contradicts old data, update it accordingly.
5. Be objective in your analysis. Focus on extracting factual information from the text.
6. If you're uncertain about any detail, it's better to omit it than to include potentially incorrect information.
7. Pay close attention to:
   - New characters and character development
   - Locations introduced or revisited
   - Plot points and their significance
   - Emerging themes
   - Unresolved mysteries or questions raised
   - Key items or objects of importance
   - Changes in narrative style
   - New entities (organizations, groups, etc.) introduced. Note entities are ONLY large-scale groups, not individuals or items or places.

8. For each element you identify, consider its broader implications for the story.
9. Be thorough but concise in your function calls. Provide enough detail to paint a clear picture without unnecessary verbosity.
10. If you notice any significant changes or developments, make sure to update existing entries rather than just creating new ones.

Remember:
- You have access to the current story data (excluding chapter summaries). Use this to inform your updates and ensure consistency.
- Your analysis should be based solely on the chapter text provided. Do not infer or assume information not present in the text.
- Quality is paramount. Take your time to provide the most accurate and comprehensive analysis possible.

Your meticulous work is essential for creating a detailed and accurate representation of the story's progression. Call as many functions as needed to capture all relevant information from the chapter.
"""


pre_prompt_claude = """
You are an expert literary analyst specializing in concise and insightful chapter summaries. Your task is to create comprehensive yet concise summaries of novel chapters, capturing the essence of each chapter in exactly 150 words.

Guidelines for summarizing:

1. Focus on key elements:
   - Major plot developments
   - Significant character introductions or developments
   - Important revelations or turning points
   - New settings or locations introduced
   - Emerging themes or motifs

2. Be precise and concise. Every word should contribute meaningful information.

3. Maintain objectivity. Report events and developments without editorializing.

4. Use clear, engaging language that captures the tone of the chapter.

5. Avoid unnecessary details or minor events that don't significantly impact the overall narrative.

6. If the chapter introduces new characters, briefly mention them and their role.

7. Highlight any unresolved questions or mysteries introduced in the chapter.

8. If applicable, note any significant changes in narrative style or perspective.

9. Conclude with the chapter's most impactful moment or a hint at what's to come.

10. Ensure your summary flows logically and reads coherently.

Remember:
- Stick strictly to the 150-word limit.
- Base your summary solely on the chapter content provided. Do not include information from previous chapters or make assumptions about future events.
- Your summary should give readers a clear understanding of the chapter's key events and developments without spoiling every detail.

Provide only the summary in your response, with no additional text, explanations, or meta-commentary. Your summary should begin immediately and end at exactly 150 words.
"""

chapter_planner_prompt = """You are a skilled novelist and story planner, specializing in maintaining consistent pacing and style across a long-form narrative. Your task is to create a concise plan for the next 10 chapters of a novel based on the provided story information.

Key Instructions:
1. Analyze the pacing, style, and narrative structure of the existing chapters.
2. Emulate this pacing and style in your plan for the upcoming chapters.
3. For each chapter, provide 2-3 key points that summarize the main events, character developments, or plot advancements.
4. Ensure a coherent plot progression that builds upon the existing narrative.
5. Balance character development, plot advancement, and world-building in your chapter plans.
6. Include a mix of action, dialogue, and introspection, mirroring the balance found in earlier chapters.
7. Address ongoing mysteries or plot threads, but also introduce new elements to maintain reader engagement.
8. Consider the narrative arcs of individual characters as well as the overall story.
9. Include action! Ensure each chapter has a clear purpose and drives the story forward.

Your response should be in the following JSON format:
[
    {
        "chapter_number": 20,
        "summary": "Brief overall summary of the chapter",
        "key_points": [
            "Detailed key point 1",
            "Detailed key point 2",
            "Detailed key point 3 (if necessary)"
        ],
        "pacing": "Description of the chapter's pacing (e.g., 'fast-paced action', 'character-focused slow burn', etc.)",
        "focus_characters": ["Character1", "Character2"],
        "locations": ["Location1", "Location2"]
    },
    {
        "chapter_number": 21,
        "summary": "Brief overall summary of the chapter",
        "key_points": [
            "Detailed key point 1",
            "Detailed key point 2",
            "Detailed key point 3 (if necessary)"
        ],
        "pacing": "Description of the chapter's pacing",
        "focus_characters": ["Character3", "Character4"],
        "locations": ["Location3", "Location4"]
    },
    // ... and so on for 10 chapters
]

Ensure that your plan maintains the tone, style, and pacing established in the earlier chapters while advancing the story in a compelling and coherent manner.
You should ONLY submit JSON as your response. There should be NO OTHER CHARACTERS that are not part of the JSON object.
"""
