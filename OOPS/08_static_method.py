class chaiUtlis:
    def chaiIngredient(text):
        return [item.strip() for item in text.split(",") ]
raw = "banana       ,        cinnamon , masala"
cleaned = chaiUtlis.chaiIngredient(raw)
print(cleaned)
    