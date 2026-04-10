from transformers import pipeline

ner_pipeline = pipeline(
    "ner", grouped_entities=True
)


text = """
Sundar Pichai is the CEO of Google. He was born in India and studied at Stanford University.
Google is headquartered in California.
"""


results = ner_pipeline(text)



entites = {}

for item in results:
    entitiy_type = item['entity_group']
    entity_word = item['word']

    if entitiy_type not in entites:
        entites[entitiy_type] = []
    
    if entity_word not in entites[entitiy_type]:
        entites[entitiy_type].append(entity_word)

print("\nExtracted Entites: \n")

for entity_type, names in entites.items():
    print(f"{entity_type}:")
    for name in names:
        print(f" - {name}")