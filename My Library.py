books = [
    {"name": "Poets", "writer": "Ahmad Shamloo", "translator": None ,"publisher": "Negah"},
    {"name": "Zemestan", "writer": "Mehdi AkhavanSales", "translator": None, "publisher": "Zemestan"},
    {"name": "Palace", "writer": "Frantce Kafka", "translator": "AmirJalalaldin Aalam", "publisher": "Nilofar"},
    {"name": "Maloy", "writer": "Samoel Becet", "translator": "Soheil Somi", "publisher": "Sales"},
    {"name": "aaa", "writer": "aaa", "translator": "aaa", "publisher": "aaa"}
]

for book in books:
    print(book["name"], book["writer"], book["translator"], book["publisher"], sep=" ,")