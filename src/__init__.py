import requests
import json
from src import _apiv1
class UncachedError(BaseException):
    pass
class LinkuError(BaseException):
    pass
class CouldNotFindWord(Warning):
    pass
class LanguageNotEnabled(BaseException):
    pass
class SandboxNotEnabled(BaseException):
    pass

class wordfilter:
    def __init__(self, isdepricated: list = None, category: list = None, era: list = None, year: list = None, creators: list = None, book: list = None, related: list = None, issandbox: list = None):
        self.isdepricated = isdepricated
        self.category = category
        self.era = era
        self.year = year
        self.creators = creators
        self.book = book
        self.related = related
        self.issandbox = issandbox
    def match(self, word: _apiv1.word):
        if self.isdepricated is None:
            pass
        else:
            if word.isdepricated not in self.isdepricated:
                return False
        if self.category is None:
            pass
        else:
            if word.category not in self.category:
                return False
        if self.era is None:
            pass
        else:
            if word.era not in self.era:
                return False
        if self.year is None:
            pass
        else:
            if word.year not in self.year:
                return False
        if self.creators is None:
            pass
        else:
            if word.creators not in self.creators:
                return False
        if self.book is None:
            pass
        else:
            if word.book not in self.book:
                return False
        if self.related is None:
            pass
        else:
            if word.related not in self.related:
                return False
        if self.issandbox is None:
            pass
        else:
            if word.issandbox not in self.issandbox:
                return False
        return True


class apiv1:
    def __init__(self, sandbox: bool = False, cached: bool =True, langs: str|list ="en"):
        self._url = "https://api.linku.la/v1/"
        self._paths = {"words": "words", "sandbox": "sandbox"}
        self.iscached = cached
        self._cache = {}
        self.langs = []
        self.hassandbox = sandbox
        if langs is str:
            self.langs = [langs]
        elif langs is list:
            self.langs = langs
        else:
            self.langs = ["en"]
        if self.iscached:
            self.reload()
    def reload(self):
        if self.iscached:
            r = requests.get(f"{self._url}{self._paths["words"]}?lang={','.join(self.langs)}")
            try:
                if r.json()["ok"] == False:
                    LinkuError(f"Could not load cache because: {r.json()["message"]}")
            except KeyError:
                pass
            self._cache["words"] = r.json()
            if self.hassandbox:
                r = requests.get(f"{self._url}{self._paths["sandbox"]}?lang={','.join(self.langs)}")
                try:
                    if r.json()["ok"] == False:
                        LinkuError(f"Could not load cache because: {r.json()["message"]}")
                except KeyError:
                    pass
                self._cache["sandbox"] = r.json()
                # self._cache["wordstyped"] = self.getallwords()
                # self._cache["sandbox+wordstyped"] = self.getallwords(includesandbox=True)
        else:
            UncachedError("This object is uncached, and thus can not reload it's cache")
    def _getdata(self):
        data = {}
        if self.iscached:
            data = self._cache
        else:
            r = requests.get(f"{self._url}{self._paths["words"]}?lang={','.join(self.langs)}")
            try:
                if r.json()["ok"] == False:
                    LinkuError(f"Could not load cache because: {r.json()["message"]}")
            except KeyError:
                pass
            data["words"] = r.json()
            if self.hassandbox:
                r = requests.get(f"{self._url}{self._paths["sandbox"]}?lang={','.join(self.langs)}")
                try:
                    if r.json()["ok"] == False:
                        LinkuError(f"Could not load cache because: {r.json()["message"]}")
                except KeyError:
                    pass
                data["sandbox"] = r.json()
        return data
    def getwordfromtp(self, word: str, sandbox: bool = False):
        data = self._getdata()
        if word in data["words"]:
            return _apiv1.word(data["words"][word], issandbox=False)
        elif self.hassandbox and sandbox:
            if word in data["sandbox"]:
                return _apiv1.word(data["sandbox"][word], issandbox=True)
        else:
            CouldNotFindWord(f"Could not find {word}! You may have to reload cache or enable the sandbox.")
            return None
    def getallwords(self, includesandbox: bool = False):
        data = self._getdata()
        if includesandbox:
            all = dict(data["words"], **data["sandbox"])
        else:
            all = data["words"]
            all = dict(sorted(all.items()))
        final = []
        for k, v in all.items():
            insandbox = False
            if includesandbox and k in data["sandbox"]:
                insandbox = True
            final.append(_apiv1.word(v, insandbox))
        return final
    def searchbytp(self, query: str, includesandbox: bool = False):
        data = self._getdata()
        if includesandbox:
            words = list(data["words"].keys()) + list(data["sandbox"].keys())
        else:
            words = list(data["words"].keys())
        sortedwords = []
        for x in words:
            if query in x:
                sortedwords.append(x)
        result = []
        # print(sortedwords)
        for x in sortedwords:
            result.append(self.getwordfromtp(x, sandbox=includesandbox))
        return result
    def searchbydef(self, query: str, lang: str = 'en', includesandbox: bool = False):
        words = self.getallwords(includesandbox=includesandbox)
        result = []
        for x in words:
            if query in x.definitions[lang]:
                result.append(x)
        return result
    def getallmatchfilter(self, filter: wordfilter, includesandbox: bool = False):
        data = self.getallwords(includesandbox)
        out = []
        for x in data:
            if filter.match(word=x):
                out.append(x)
        return out