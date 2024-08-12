# For API version 1

class word: # Note: this should only be created by the __init__.apiv1 class
    def __init__(self, wordjson, issandbox):
        self.name = None
        self.isdepricated = None
        self.category = None
        self.era = None
        self.year = None
        self.creators = None
        self.book = None
        self.related = None
        self.sources = None
        self.sitelen_suwi = None
        self.ucsur = None
        self.etymology = None
        self.audio = None
        self.usage = None
        self.translations = None
        self.definitions = None
        self.issandbox = None

        try:
            self.name = wordjson["word"]
        except KeyError:
            pass
        try:
            self.isdepricated = wordjson["deprecated"]
        except KeyError:
            pass
        try:
            self.category = wordjson["usage_category"]
        except KeyError:
            pass
        try:
            self.era = wordjson["coined_era"]
        except KeyError:
            pass
        try:
            self.year = wordjson["coined_year"]
        except KeyError:
            pass
        try:
            self.creators = wordjson["creator"]
        except KeyError:
            pass
        try:
            self.book = wordjson["book"]
        except KeyError:
            pass
        try:
            self.ku_data = wordjson["ku_data"]
        except KeyError:
            self.ku_data = None
        try:
            self.related = wordjson["see_also"]
        except KeyError:
            pass
        try:
            self.sources = wordjson["resources"]
        except KeyError:
            pass
        try:
            self.sitelen_suwi = wordjson["representations"]["sitelen_sitelen"]
        except KeyError:
            pass
        try:
            self.ucsur = chr(int(wordjson["representations"]["ucsur"][2:], 16))
        except KeyError:
            pass
        try:
            self.etymology = {"source": wordjson["source_language"], "words": wordjson["etymology"]}
        except KeyError:
            pass
        try:
            self.audio = wordjson["audio"]
        except KeyError:
            pass
        try:
            self.pu_data = wordjson["pu_verbatim"]
        except KeyError:
            self.pu_data = None
        try:
            self.usage = wordjson["usage"]
        except KeyError:
            pass
        try:
            self.translations = wordjson["translations"]
        except KeyError:
            pass
        try:
            definitions = {}
            for k, v in self.translations.items():
                definitions[k] = v["definition"]
            self.definitions = definitions
        except KeyError:
            pass
        try:
            self.issandbox = issandbox
        except KeyError:
            pass