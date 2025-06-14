from stats import get_char_summary
import sys

def main(book_path):
	get_char_summary(book_path)	

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	main(sys.argv[1])


