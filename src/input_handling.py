from dotenv import dotenv_values
from openai import OpenAI
import json

config = dotenv_values(".env")  

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.get("OPENAI_API_KEY"),
)

def validate_story_and_scenes(text, num_scenes):
    try:
        content = f"Let me know if the following story can be divided into {num_scenes} scenes while making sure that each scene is coherent and meaningful:\n Story: {text}\nReturn the response as true or false"
        
        # API call wrapped in try-except for error handling
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model="gpt-3.5-turbo",
        )

        # Return the generated scenes
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error validating story and scenes text: {str(e)}")
        return None  # You can return None or an error message based on your preference