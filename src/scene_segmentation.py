# import spacy
# import numpy as np
# from sklearn.cluster import KMeans
# from nltk.tokenize import sent_tokenize
from dotenv import dotenv_values
from openai import OpenAI
import json

config = dotenv_values(".env")  

client = OpenAI(
    # This is the default and can be omitted
    api_key=config.get("OPENAI_API_KEY"),
)

# Load the spaCy model
# nlp = spacy.load("en_core_web_sm")

# def segment_text(text, num_scenes):
#     """
#     Segment text into the specified number of scenes using sentence embeddings and clustering.

#     :param text: Input story or scene description.
#     :param num_scenes: Desired number of scenes.
#     :return: List of segmented scenes in the correct order.
#     """
#     # Tokenize text into sentences
#     sentences = sent_tokenize(text)

#     # Extract sentence embeddings using spaCy
#     sentence_embeddings = np.array([nlp(sentence).vector for sentence in sentences])

#     # Apply KMeans clustering to group sentences into scenes
#     kmeans = KMeans(n_clusters=num_scenes, random_state=0)
#     kmeans.fit(sentence_embeddings)

#     # Create clusters of sentences based on the KMeans result
#     scene_clusters = {i: [] for i in range(num_scenes)}

#     # Track the original index of each sentence to maintain order
#     for i, sentence in enumerate(sentences):
#         cluster_index = kmeans.labels_[i]
#         scene_clusters[cluster_index].append((i, sentence))  # Store (index, sentence)

#     # Sort each scene cluster by the original sentence order (based on index)
#     for cluster_index in scene_clusters:
#         scene_clusters[cluster_index].sort(key=lambda x: x[0])  # Sort by original index

#     # Sort the clusters based on the first sentence index in each cluster
#     sorted_scenes = sorted(scene_clusters.values(), key=lambda cluster: cluster[0][0])

#     # Convert clusters into coherent scene segments, ignoring the indices
#     segmented_scenes = [" ".join([sentence for _, sentence in cluster]) for cluster in sorted_scenes]

#     return segmented_scenes

def segment_text(text, num_scenes):
    content = f"Divide the following story into the specified number of scenes. Make sure each scene is coherent and meaningful:\n Story: {text}\n No of Scenes: {num_scenes}\n\nReturn the result as an array like ['scene 1', 'scene 2', ...].\nNote: You might receive an unordered story. So make sure to divide it and sort it properly"
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content
