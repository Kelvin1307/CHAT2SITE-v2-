from extractor import extract_website_json

conversation = [
    "hey it's Kelvin Cakes",
    "store,i guess",
    "Fresh custom cakes",
    "Birthday cakes, Wedding cakes, Cupcakes",
    "Chennai",
    "hello@kelvincakes.in",
    "+91 9876543210"
]

result = extract_website_json(conversation)
print(result)
