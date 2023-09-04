from modeltranslation.translator import translator,TranslationOptions, register
from .models import BookModel

class BookTranslations(TranslationOptions):
    fields = ('title','auther','bio')

translator.register(BookModel, BookTranslations)