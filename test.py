from src import apiv1
from src import wordfilter

linku = apiv1(sandbox=True)
# print(linku.getwordfromtp("aka", sandbox=True).definitions['en'])
filter = wordfilter(related=["ali"])
allwords = linku.getallmatchfilter(filter=filter, includesandbox=True)
for x in allwords:
    print(x.name)
    # if x.name == "yupekosi":
    #     print("YAAAAAAAAAAAAAAAAAAa")