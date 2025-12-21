import requests, json

def getCatFacts():
    base_url = "https://catfact.ninja/fact"
    headers = {
        'Content-Type': 'Application/json'
    }
    response = requests.get(url=base_url, headers=headers)
    # print(response.json()["fact"])
    with open('processed_data.json', 'w') as f:
        json.dump(response.json()["fact"], f, indent=4)
        print("Data saved to processed_data.json")

getCatFacts()