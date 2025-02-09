﻿# LLM-Based Story Extender

## Project Overview

The LLM-Based Story Extender is an advanced tool designed to assist authors in extending and developing their stories using Large Language Models (LLMs). This project leverages the power of OpenAI's GPT-4 and Anthropic's Claude to analyze existing stories, generate new chapters, and maintain consistency throughout a narrative, even beyond the context window limits of LLMs.

### Key Features:
- Web scraping of existing stories from Royal Road
- Comprehensive story analysis using LLMs
- Structured data extraction using GPT functions for consistent JSON output
- Long-term tracking of story elements across multiple chapters
- Automatic chapter planning for high-level plot development
- Chapter generation based on existing story elements and plans
- Alternating chapter generation and processing for up-to-date story data

### Technologies Used:
- Python 3.x
- OpenAI API with GPT-4
- Anthropic API with Claude
- aiohttp for asynchronous HTTP requests
- asyncio for asynchronous programming
- BeautifulSoup for web scraping
- JSON for structured data storage and manipulation

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Workflow](#workflow)
5. [Code Structure](#code-structure)
6. [Detailed Functionality Explanation](#detailed-functionality-explanation)
9. [Troubleshooting](#troubleshooting)
10. [Performance Considerations](#performance-considerations)
13. [Changelog](#changelog)
14. [License](#license)
15. [Contact Information](#contact-information)

## Installation

Follow these steps to set up the LLM-Based Story Extender:

1. Clone the repository:
   ```
   git clone https://github.com/Wesius/LLM-Based-Story-Extender.git
   cd LLM-Based-Story-Extender
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up API keys:
   - Obtain API keys from OpenAI and Anthropic
   - Create a `.env` file in the project root directory
   - Add your API keys to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ANTHROPIC_API_KEY=your_anthropic_api_key
     ```

## Configuration

The project uses environment variables for configuration. Ensure your `.env` file contains the following:

```
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

You can also configure the following parameters in the code:

- `anthropic_api.py`: Adjust the `model` parameter in the API calls to use different versions of Claude.
- `openai_api.py`: Modify the `model` parameter in the `create_assistant` function to use different GPT models.
- `generate_chapters.py`: Update the `start_chapter`, `num_chapters`, and `use_planner` variables as needed.

## Usage

The LLM-Based Story Extender follows a specific workflow to ensure consistent story development and data management. Here's how to use the system:

### Workflow

1. **Scrape Existing Story**
   ```
   python scraper.py
   ```
   This will download chapters from Royal Road and save them in the `chapters` directory.
   You can change the link in this file to change the story being scraped.

2. **Process Existing Chapters**
   ```
   python main.py
   ```
   This analyzes the scraped chapters and builds the initial story data.

3. **Generate Chapter Plan**
   ```
   python chapter_planner.py
   ```
   This creates a high-level plan for the next set of chapters. To change the amount of chapters to plan (default is 10), look for the line `    end_chapter = start_chapter + 9` and change the number 9 to the desired number of chapters to plan.


4. **Update Generation Parameters**

   Open `generate_chapters.py` and update the following variables:
   - `start_chapter`: Set to the next chapter number
   - `num_chapters`: Number of chapters to generate
   - `use_planner`: Set to `False` to use the plan you just generated or set to True to generate a new plan automatically (buggy).

5. **Generate and Process New Chapters**
   ```
   python generate_chapters.py
   ```
   This script will alternate between generating a new chapter and processing it, ensuring that each new chapter is based on up-to-date story data.

6. **Review Generated Chapters**
   The new chapters will be available in the `chapters` directory.

## Code Structure

The project consists of several Python scripts, each with a specific role in the story extension process:

- `scraper.py`: Scrapes existing stories from Royal Road.
- `main.py`: Entry point for processing existing chapters.
- `chapter_planner.py`: Generates plans for upcoming chapters.
- `generate_chapters.py`: Orchestrates the chapter generation and processing workflow.
- `anthropic_api.py`: Handles interactions with the Anthropic API (Claude).
- `openai_api.py`: Manages interactions with the OpenAI API (GPT-4).
- `process_chapters.py`: Analyzes generated chapters and updates story data.

## Detailed Functionality Explanation

### GPT Functions and JSON Output

One of the key features of this system is its use of OpenAI GPT functions to ensure consistent, structured output in JSON format. This is crucial for several reasons:

1. **Consistency**: By defining specific functions (e.g., `create_character`, `update_plot_point`, which can be found in ```\prompts_and_functions\functions.py```), we ensure that the LLM always provides data in a predictable format.

2. **Long-term Tracking**: JSON output allows us to easily parse and store story elements in a structured way, enabling tracking of these elements across multiple chapters and beyond the context window limits of the LLMs.

3. **Data Integrity**: The structured format makes it easier to validate and sanitize the data, reducing the risk of inconsistencies or errors in the story elements.

Here's an example of how GPT functions are used in the system:

```python
llm_functions = [
    {
        "name": "create_character",
        "description": "Create a new character in the story",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "role": {"type": "string"},
                "background": {"type": "string"}
            },
            "required": ["name", "description", "role"]
        }
    },
    # More functions defined here...
]

async def process_with_chatgpt(assistant_id, chapter_text, chapter_number, current_data):
    # ... (code to set up the API call)

    function_calls = []
    for tool_call in tool_calls:
        function_calls.append({
            "name": tool_call.function.name,
            "arguments": json.loads(tool_call.function.arguments)
        })

    return function_calls
```

This approach allows us to maintain a comprehensive and consistent record of the story's elements in `data/data.json`, which serves as the source of truth for the story's state.

### Workflow Diagram

```
[Scraper] --> [Existing Chapters] --> [Chapter Processor]
                                           |
                                           v
[Story Data] <--> [Chapter Planner] <--> [Chapter Generator]
    ^                                        |
    |                                        v
    +----------------------------------[New Chapter]
```

The workflow diagram illustrates the interaction between the different components of the system. The story data is continuously updated and used to generate new chapters based on the chapter planner's high-level plans.
## Troubleshooting

### Common Issues and Solutions

1. **Scraping Errors**
   - Ensure you have the correct URL for the story on Royal Road.
   - Check your internet connection and Royal Road's availability.
   - Consider adding delays between requests to avoid rate limiting.

2. **API Key Errors**
   - Double-check that your `.env` file contains the correct API keys.
   - Ensure the environment variables are being loaded correctly.

3. **Inconsistent Chapter Generation**
   - Review the `data/data.json` file to ensure story elements are being tracked correctly.
   - Adjust the prompts in `prompts.py` if necessary.

4. **JSON Parsing Errors**
   - Check the GPT function definitions to ensure they match the expected output structure.
   - Review the API responses for any unexpected formats or content.

## Performance Considerations

- The system relies heavily on API calls, which can be time-consuming.
- For large stories, the `data/data.json` file can grow significantly.
- Beware of the balance between performance and API rate limits.

## Contributing

Contributions to the LLM-Based Story Extender are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the following guidelines:
- Follow PEP 8 style guide for Python code.
- Write clear, self-documenting code with appropriate comments.
- Include unit tests for new features or bug fixes.
- Update the documentation to reflect any changes in functionality.

## Changelog

### Version 1.0.0 (2023-6-28)
- Initial release
- Basic scraping, chapter generation, and processing functionality
- Integration with OpenAI and Anthropic APIs

### Version 1.1.0 (2023-07-04)
- Added chapter planning feature
- Implemented GPT functions for structured JSON output
- Improved error handling and logging
- Enhanced story data management

## License

This project is licensed under the MIT License.

## Contact Information

For questions, suggestions, or support, please contact:

- Project Maintainer: Wes Griffin <wesgriffin32@gmail.com>
- GitHub Issues: [https://github.com/Wesius/LLM-Based-Story-Extender/issues](https://github.com/Wesius/LLM-Based-Story-Extender/issues)

Thanks!
