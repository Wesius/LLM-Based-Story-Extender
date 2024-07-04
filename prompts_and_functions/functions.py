# Chapter Summaries
def create_chapter_summary(chapter, summary):
    return {"chapter": chapter, "summary": summary}


def update_chapter_summary(chapter, summary):
    return {"chapter": chapter, "summary": summary}


def delete_chapter_summary(chapter):
    return {"chapter": chapter}


# Characters
def create_character(
    name, description, background, traits, significance, first_appearance, relationships
):
    return {
        "name": name,
        "description": description,
        "background": background,
        "traits": traits,
        "significance": significance,
        "first_appearance": first_appearance,
        "relationships": relationships,
    }


def update_character(name, updates):
    return {"name": name, "updates": updates}


def delete_character(name):
    return {"name": name}


# Locations
def create_location(name, description, significance, chapter_last_seen):
    return {
        "name": name,
        "description": description,
        "significance": significance,
        "chapter_last_seen": chapter_last_seen,
    }


def update_location(name, updates):
    return {"name": name, "updates": updates}


def delete_location(name):
    return {"name": name}


# Plot
def create_plot_point(chapter, event, significance, timestamp=None):
    return {
        "chapter": chapter,
        "event": event,
        "significance": significance,
        "timestamp": timestamp,
    }


def update_plot_point(chapter, event, updates):
    return {"chapter": chapter, "event": event, "updates": updates}


def delete_plot_point(chapter, event):
    return {"chapter": chapter, "event": event}


# Themes
def create_theme(name, description, related_characters):
    return {
        "name": name,
        "description": description,
        "related_characters": related_characters,
    }


def update_theme(name, updates):
    return {"name": name, "updates": updates}


def delete_theme(name):
    return {"name": name}


# Unresolved Mysteries
def create_unresolved_mystery(description, introduced_in_chapter, status, significance):
    return {
        "description": description,
        "introduced_in_chapter": introduced_in_chapter,
        "status": status,
        "significance": significance,
    }


def update_unresolved_mystery(description, updates):
    return {"description": description, "updates": updates}


def delete_unresolved_mystery(description):
    return {"description": description}


# Key Items
def create_key_item(name, description, significance, current_location):
    return {
        "name": name,
        "description": description,
        "significance": significance,
        "current_location": current_location,
    }


def update_key_item(name, updates):
    return {"name": name, "updates": updates}


def delete_key_item(name):
    return {"name": name}


# Narrative Style
def update_narrative_style(pov, tense, tone, style):
    return {"pov": pov, "tense": tense, "tone": tone, "style": style}


# Entities
def create_entity(
    name,
    type,
    description,
    key_members,
    affiliations,
    goals,
    significance,
    first_appearance,
):
    return {
        "name": name,
        "type": type,
        "description": description,
        "key_members": key_members,
        "affiliations": affiliations,
        "goals": goals,
        "significance": significance,
        "first_appearance": first_appearance,
    }


def update_entity(name, updates):
    return {"name": name, "updates": updates}


def delete_entity(name):
    return {"name": name}


llm_functions = [
    # Characters
    {
        "type": "function",
        "function": {
            "name": "create_character",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "background": {"type": "string"},
                    "traits": {"type": "array", "items": {"type": "string"}},
                    "significance": {"type": "string"},
                    "first_appearance": {"type": "integer"},
                    "relationships": {"type": "array", "items": {"type": "string"}},
                },
                "required": [
                    "name",
                    "description",
                    "background",
                    "traits",
                    "significance",
                    "first_appearance",
                    "relationships",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_character",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["name", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_character",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    # Locations
    {
        "type": "function",
        "function": {
            "name": "create_location",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "significance": {"type": "string"},
                    "chapter_last_seen": {"type": "integer"},
                },
                "required": [
                    "name",
                    "description",
                    "significance",
                    "chapter_last_seen",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_location",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["name", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_location",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    # Plot
    {
        "type": "function",
        "function": {
            "name": "create_plot_point",
            "parameters": {
                "type": "object",
                "properties": {
                    "chapter": {"type": "integer"},
                    "event": {"type": "string"},
                    "significance": {"type": "string"},
                    "timestamp": {"type": ["string", "null"]},
                },
                "required": ["chapter", "event", "significance"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_plot_point",
            "parameters": {
                "type": "object",
                "properties": {
                    "chapter": {"type": "integer"},
                    "event": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["chapter", "event", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_plot_point",
            "parameters": {
                "type": "object",
                "properties": {
                    "chapter": {"type": "integer"},
                    "event": {"type": "string"},
                },
                "required": ["chapter", "event"],
            },
        },
    },
    # Themes
    {
        "type": "function",
        "function": {
            "name": "create_theme",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "related_characters": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["name", "description", "related_characters"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_theme",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["name", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_theme",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    # Unresolved Mysteries
    {
        "type": "function",
        "function": {
            "name": "create_unresolved_mystery",
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {"type": "string"},
                    "introduced_in_chapter": {"type": "integer"},
                    "status": {"type": "string"},
                    "significance": {"type": "string"},
                },
                "required": [
                    "description",
                    "introduced_in_chapter",
                    "status",
                    "significance",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_unresolved_mystery",
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["description", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_unresolved_mystery",
            "parameters": {
                "type": "object",
                "properties": {"description": {"type": "string"}},
                "required": ["description"],
            },
        },
    },
    # Key Items
    {
        "type": "function",
        "function": {
            "name": "create_key_item",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "significance": {"type": "string"},
                    "current_location": {"type": "string"},
                },
                "required": ["name", "description", "significance", "current_location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_key_item",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["name", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_key_item",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    # Narrative Style
    {
        "type": "function",
        "function": {
            "name": "update_narrative_style",
            "parameters": {
                "type": "object",
                "properties": {
                    "pov": {"type": "string"},
                    "tense": {"type": "string"},
                    "tone": {"type": "string"},
                    "style": {"type": "string"},
                },
                "required": ["pov", "tense", "tone", "style"],
            },
        },
    },
    # Entities
    {
        "type": "function",
        "function": {
            "name": "create_entity",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "description": {"type": "string"},
                    "key_members": {"type": "array", "items": {"type": "string"}},
                    "affiliations": {"type": "array", "items": {"type": "string"}},
                    "goals": {"type": "array", "items": {"type": "string"}},
                    "significance": {"type": "string"},
                    "first_appearance": {"type": "integer"},
                },
                "required": [
                    "name",
                    "type",
                    "description",
                    "key_members",
                    "affiliations",
                    "goals",
                    "significance",
                    "first_appearance",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update_entity",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "updates": {"type": "object"},
                },
                "required": ["name", "updates"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_entity",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
]
