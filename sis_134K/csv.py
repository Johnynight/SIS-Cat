import simplejson as json

with open('2341645.json','r', encoding='utf-8') as file:

    lol = json.load(file)
    facets = lol['facets']
    dicscriptions = facets['productFamilyHierarchy']
print(facets)