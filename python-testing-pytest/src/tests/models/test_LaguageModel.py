from src.models.LanguageModel import LanguageModel
# tenemos una lista que sea distinta a none, tambien que la lista tenga elementos y que tambien que cada elemento no sea vacio 


#que no sea none
def test_get_languages_not_none():
    languages = LanguageModel.get_languages()
    assert languages != None 

# que la lista tenga elementos
def test_get_languages_has_elements():
    languages = LanguageModel.get_languages()
    assert len(languages) > 0

# # que no se obtenga elementos vacios
def test_get_languages_check_elements_length():
    languages = LanguageModel.get_languages()
    for language in languages:
        assert len(language) > 0 # ["C#", "", "Python", "Dart", "Kotlin"]
