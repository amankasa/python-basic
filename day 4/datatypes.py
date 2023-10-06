persons=[
    {
        'name':'Ram',
        'age':12,
        'gender':'male',
        'languages': ['python','java'],
        'family_member': {
            'father':'Ramesh',
            'uncle':'Haresh',
            'mother':'sita',
            'son':'Umesh',
        }
    },
    {
        'name':'Shyam',
        'age':15,
        'gender':'Male',
        'languages': ['python','java'],
        'family_member': {
            'father':'hitesh',
            'uncle':'karesh',
            'mother':'gita',
            'son':'ganesh',
                          }
    },
    {
        'name':'Hari',
        'age':12,
        'gender':'male',
        'languages': ['python','java'],
        'family_member': {
           'father':'umesh',
            'uncle':'suresh',
            'mother':'rita',
            'son':'ramesh',
                          }
    }
]

print(f"""
My name is {persons[0]['name']} and age is {persons[0]['age']} and gender is {persons[0]['gender']} and I know different languages like:
1. {persons[0]['languages'][0]}
2. {persons[0]['languages'][1]}
My family members are:
1. Father:{persons[0]['family_member']['father']}
2. Mother:{persons[0]['family_member']['mother']}
3. Uncle:{persons[0]['family_member']['uncle']}
4. Son:{persons[0]['family_member']['son']}
""")
print(f"""
My name is {persons[1]['name']} and age is {persons[1]['age']} and gender is {persons[1]['gender']} and I know different languages like:
1. {persons[1]['languages'][0]}
2. {persons[1]['languages'][1]}
My family members are:
1. Father:{persons[1]['family_member']['father']}
2. Mother:{persons[1]['family_member']['mother']}
3. Uncle:{persons[1]['family_member']['uncle']}
4. Son:{persons[1]['family_member']['son']}
""")
print(f"""
My name is {persons[2]['name']} and age is {persons[2]['age']} and gender is {persons[2]['gender']} and I know different languages like:
1. {persons[2]['languages'][0]}
2. {persons[2]['languages'][1]}
My family members are:
1. Father:{persons[2]['family_member']['father']}
2. Mother:{persons[2]['family_member']['mother']}
3. Uncle:{persons[2]['family_member']['uncle']}
4. Son:{persons[2]['family_member']['son']}
""")