from modeltranslation.translator import translator, TranslationOptions
from .models import AutherModel, AutherBookModel


# Auther Translations
class Authertranslation(TranslationOptions):
    fields= ('first_name','last_name','place_of_birth','Place_of_death','bio')
    
translator.register(AutherModel,Authertranslation)
    
#  Auther book translations
class AutherbookTranslations(TranslationOptions):
    fields = ('name','bio')
    
translator.register(AutherBookModel,AutherbookTranslations )