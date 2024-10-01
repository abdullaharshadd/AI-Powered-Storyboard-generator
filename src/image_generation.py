from dotenv import dotenv_values
from openai import OpenAI
import json

config = dotenv_values(".env")  

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.get("OPENAI_API_KEY"),
)

def generate_images(scenes, size="400x400"):
    images = []
    
    # Initial context for the story
    story_context = ""
    
    for i, scene in enumerate(scenes):
        try:
            # Append current scene to the story context
            story_context += f"Scene {i + 1}: {scene}\n"

            # Create prompt for the image generation
            prompt = f"Generate an image for the following scene in a story (Size of the image should be {size}): {scene}.\n\nHere is the context:\n{story_context}\n"
            
            # Generate the image using OpenAI's image generation API
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
            )

            image_url = response.data[0].url
            images.append(image_url)

        except Exception as e:
            print(f"Error generating image for scene {i + 1}: {str(e)}")
            images.append(None)  # Append None or handle it in another way if an error occurs

    return images
