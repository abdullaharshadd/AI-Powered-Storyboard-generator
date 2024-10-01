from dotenv import dotenv_values
from openai import OpenAI
import json

config = dotenv_values(".env")  

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.get("OPENAI_API_KEY"),
)

def segment_text(text, num_scenes):
    try:
        content = f"Divide the following story into the specified number of scenes. Make sure each scene is coherent and meaningful:\n Story: {text}\n No of Scenes: {num_scenes}\n\nReturn the result as an array like ['scene 1', 'scene 2', ...].\nNote: You might receive an unordered story. So make sure to divide it and sort it properly"
        
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
        print(f"Error segmenting text: {str(e)}")
        return None  # You can return None or an error message based on your preference
