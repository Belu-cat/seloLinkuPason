from selo_linku import apiv1
from selo_linku import wordfilter

linku = apiv1(sandbox=False, langs="tok", cached=True)
# print(linku.getwordfromtp("aka", sandbox=True).definitions['en'])
# linku.addlanguage("tok")
# print(linku.langs)
linku.getwordfromtp("apeja", sandbox=False)
filter = wordfilter(book=["pu"])
allwords = linku.getallmatchfilter(filter=filter, includesandbox=True)
# for x in allwords:
#     print(x.definitions['tok'])
#     # if x.name == "yupekosi":
#     #     print("YAAAAAAAAAAAAAAAAAAa")