from deep_translator import GoogleTranslator

input_language = "en"
output_language = "ne"
input_file = "input_file.txt"
output_file = "output_file.txt"

def translated_text(input, output):
    with open(input, 'r', encoding="utf-8") as file:
        text = file.read()

    file2 = GoogleTranslator(input_language, output_language).translate(text)
    with open(output, "w", encoding="utf-8") as file:
        file.write(file2)

translated_text(input_file, output_file)
print("Translated Successfully!!")
