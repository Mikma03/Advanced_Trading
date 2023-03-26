def clear_data_json():
    with open("data.json", "w") as f:
        f.write("[]")
