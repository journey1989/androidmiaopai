import random,yaml,json

file = open('resourceid.yaml')
data =yaml.load(file)

print(data['text_view'])
