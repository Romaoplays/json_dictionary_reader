import json
import os


def is_one_json(k):
    if len(k) == 0:
        print("File missing!")
    elif len(k) > 1:
        print("Only one file allowed")


DICTIONARY_PATH = ".\dictionary_folder"
DECONJUGATOR_PATH = ".\deconjugator_folder"


dictionary_file = os.listdir(DICTIONARY_PATH)
deconjugator_file = os.listdir(DECONJUGATOR_PATH)


is_one_json(dictionary_file)
is_one_json(deconjugator_file)

with open(
    DICTIONARY_PATH + "\\" + dictionary_file[0], encoding="utf-8"
) as dict_json_file:
    dict_json_data = json.load(dict_json_file)

with open(
    DECONJUGATOR_PATH + "\\" + deconjugator_file[0], encoding="utf-8"
) as deconj_json_file:
    deconj_json_data = json.load(deconj_json_file)


def get_en_definition(word):
    word_dict = next(item for item in dict_json_data if item["term"] == word)
    return word_dict.get("definition")


def de_deconjugate(word):
    original_word = word
    for i in range(len(deconj_json_data)):
        word = original_word
        ending = deconj_json_data[i].get("inflected")
        true_ending = deconj_json_data[i].get("dict")

        if word.startswith("ge"):
            if "prefix" in deconj_json_data[i]:
                if word.endswith(ending):
                    word = word[2:]
                    word = word[: len(word) - len(ending)]

                    word_list = []

                    for i in range(len(true_ending)):
                        word_list.append(word + true_ending[i])
                    for i in range(len(word_list)):
                        try:
                            get_en_definition(word_list[i])
                            return word_list[i]
                        except StopIteration:
                            pass

        elif word.endswith(ending):
            word = word[: len(word) - len(ending)]

            word_list = []

            for i in range(len(true_ending)):
                word_list.append(word + true_ending[i])
            for i in range(len(word_list)):
                try:
                    get_en_definition(word_list[i])
                    return word_list[i]
                except StopIteration:
                    pass
    return original_word
