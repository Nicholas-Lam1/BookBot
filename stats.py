def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents
	return "filepath does not exist"

def get_book_word_count(book_text):
	return len(book_text.split())

def print_word_count(book_path):
	print(f"{get_book_word_count(get_book_text(book_path))} words found in the document")

def get_char_count(book_path):
	char_dict = {}
	book_text = get_book_text(book_path)
	for char in book_text:
		if char.lower() in char_dict:
			char_dict[char.lower()] += 1
		else:
			char_dict[char.lower()] = 1
	return char_dict

def sort_on(dict):
    return dict["count"]

def get_char_summary(book_path):
	sorted_dict = []
	char_dict = get_char_count(book_path)
	for char in char_dict:
		if char.isalpha():
			sorted_dict.append({"char": char, "count": char_dict[char]})
	sorted_dict.sort(reverse=True, key=sort_on)


	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	print(f"Found {get_book_word_count(get_book_text(book_path))} total words")
	print("--------- Character Count -------")
	for i in range(0, len(sorted_dict) - 1):
		print(f"{sorted_dict[i]["char"]}: {sorted_dict[i]["count"]}")
	print("============= END ===============")
