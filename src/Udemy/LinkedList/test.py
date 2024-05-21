## LinkedList -> thinking this is a nested dictionary...

Head = {
    "value": 11,
    "next": {
        "value": 12,
        "next": {
            "value": 13,
            "next": {
                "value": 14,
                "next": None
            }
        }
    }

}

print(Head['next']['next']['value'])

