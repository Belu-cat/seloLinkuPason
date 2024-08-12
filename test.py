from selo_linku import apiv1
from selo_linku import wordfilter

linku = apiv1(sandbox=True)
# print(linku.getwordfromtp("aka", sandbox=True).definitions['en'])
filter = wordfilter(book=["pu"])
allwords = linku.getallmatchfilter(filter=filter, includesandbox=True)
for x in allwords:
    print(x.name)
    # if x.name == "yupekosi":
    #     print("YAAAAAAAAAAAAAAAAAAa")