# Batmud Tool, beadmap text cleaner. Takes in a dirty text file, cleans it up and prints a copy&paste version ready to be used.
def map_cleaner(input_text):
    cleaned_map = []
    with open(input_text, 'r') as file:
        for line in file:
            # The replace methods should be applied to the line being read from the file, not the input_text (which is the file path)
            normal_text = line.replace("/", "").replace("\\", "").replace("|", "")
            no_white_text = normal_text.strip()
            if no_white_text:  
                cleaned_map.append(no_white_text) 
    return cleaned_map

file_path = 'search_text.txt'
cleaned_text = map_cleaner(file_path)
for line in cleaned_text:
    print(line)
