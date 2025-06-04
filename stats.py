def get_num_words(text):
    words = text.split()
    return len(words)

def count_letter(text):
    all_letters = {}
    
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in all_letters:
            all_letters[lower_letter] += 1
        else:
            all_letters[lower_letter] = 1
    return all_letters

def formatted_dict(input_dict):
    count = []
    for key, value in input_dict.items(): 
        count.append({"char": key, "num": value})
    count.sort(reverse=True, key=lambda x: x["num"])
    return count