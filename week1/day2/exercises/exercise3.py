brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"This brand specializes in selling {', '.join(brand['type_of_clothes'])} clothes.")
brand["country_creation"] = "Spain"
brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print(brand["international_competitors"][-1])
for key,value in brand.items():
    if key == "major_color":
        for k,v in value.items():
            if k == "US":
                print(f"the major colors in the US are {' and '.join(v)}")
print(len(brand))
print(brand.keys())
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand["number_stores"]) # We can see that the number of stores has been updated to 10000