from json_dictionary_reader import get_en_definition
from json_dictionary_reader import de_deconjugate

while True:
    print("\nType out word:")
    resposta = input()

    print("\nTranslation:")
    print(get_en_definition(de_deconjugate(resposta)))
