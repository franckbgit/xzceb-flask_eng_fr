'''
Translation functions
'''

import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Translate englishText to French
    '''
    #code to translate from english to french
    if english_text != "":
        french_text_dict = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
        french_text = french_text_dict["translations"][0]["translation"]
    else:
        french_text = ""
    return french_text

def french_to_english(french_text):
    '''
    Translate frenchText to English
    '''
    #code to translate from french to english
    if french_text != "":
        english_text_dict = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
        english_text = english_text_dict["translations"][0]["translation"]
    else:
        english_text = ""
    return english_text
