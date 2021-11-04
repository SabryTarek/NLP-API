# Normal way
def wordEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "verb": item["verb"],
        "noun": item["noun"],
        "plural": item["plural"]
    }


def wordsEntity(entity) -> list:
    return [wordEntity(item) for item in entity]
# Best way


def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'},
            **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
