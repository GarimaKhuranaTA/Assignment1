input_data = input("Enter words comma-separated")

words = [word.strip() for word in input_data.split(",")]
unique_sorted_words = sorted(set(words))
print(" ".join(unique_sorted_words))
