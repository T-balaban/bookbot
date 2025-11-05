def count_words(content):
    content_list = content.split()
    count = len(content_list)
    return count

def text_to_character_number(text_content):
    text_content = text_content.lower()
    result = {}

    for char in text_content:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

def structurize(chars):
    structured = [{"char": char, "num": count} for char, count in chars.items()]
    structured.sort(reverse=True, key=lambda x: x["num"])
    return structured
