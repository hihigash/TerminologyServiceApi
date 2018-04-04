#!/usr/bin/env python
# coding: utf-8

import sys
from suds.client import Client  # pip install suds-jurko

args = sys.argv
text = args[1]

url = "http://api.terminology.microsoft.com/Terminology.svc?wsdl"
client = Client(url)

searchOperator = client.factory.create('ns1:SearchOperator')
searchStringComparison = client.factory.create('ns1:SearchStringComparison')

translationSource = client.factory.create('ns0:TranslationSource')
translationSources = client.factory.create('ns0:TranslationSources')
#translationSources.TranslationSource = [translationSource.Terms, translationSource.UiStrings]
translationSources.TranslationSource = [translationSource.Terms]

result = client.service.GetTranslations(
    text,
    "en-us",  # English (United States)
    "ja-jp",  # Japanese (Japan)
    searchStringComparison.CaseInsensitive,
    searchOperator.AnyWord,
    translationSources,
    False,
    20,
    True)

for match in result.Match:
    print("{0} => {1}".format(
        match.OriginalText, match.Translations.Translation[0].TranslatedText))
