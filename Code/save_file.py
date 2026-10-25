import json

def save_data(video_data):
    data = {
    "label": "accident",
    "landmarks": video_data
    }

    with open(r"D:\\University NSU\\CSE 299\\main_code\\Processed\\accident\\00623.json", "w") as file:
        json.dump(data, file, indent=2)

    print("Landmark data saved successfully!")