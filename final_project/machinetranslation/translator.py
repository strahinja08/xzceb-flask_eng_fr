"""This module does English French translations with watson-translator"""

import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-11-17',
    authenticator=authenticator
)

language_translator.set_service_url(url)
# the bellow line gives warnings
# language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """Convert English to French"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    response = json.dumps(translation, indent=2, ensure_ascii=False)
    french_text = json.loads(response)["translations"][0]['translation']
    return french_text

def french_to_english(french_text):
    """Convert French to English"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    res = json.dumps(translation, indent=2, ensure_ascii=False)
    english_text = json.loads(res)["translations"][0]['translation']
    return english_text

try: 
    #invoke method
    languages = language_translator.list_languages().get_result()
    # print(json.dumps(languages, indent=2))
except ApiException as ex:
    print('Method failed with status code '+ str(ex.code)+": " + ex.message)
