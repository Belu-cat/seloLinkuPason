# seloLinkuPason
Python API wrapper for sona Linku

selo Linku Pason is an unoficial API wrapper for [lipu Linku](https://github.com/lipu-linku). lipu Linku is an open-source, collabarative [toki pona](https://tokipona.org/) dictionary. Please note that this code is awful and very much uncommented. This was made in an afternoon and is not intended to be used for anything serious, it’s just for fun. I am not affiliated with the Linku team, kala Asi, mun Kekan San, TheOnlyTails, tbodt, or anyone other contributers to Linku. Full credit goes to them for making such an awesome tool, and making it free for anyone to use.

## Instalation
To install, run:

```
[PLACE COMMAND HERE]
```

## Usage
Import:
```
import selo_linku as selo
linku = selo.apiv1()
```

You can use .reload() to reload cache data:
```
linku.reload()
```
You can use .getwordfromtp() to get a word object from it's toki pona spelling:
```
toki = linku.getwordfromtp(word="toki", sandbox=True)
print(toki.name)
> toki
print(toki.definitions['en'])
> communicate, say, think; conversation, story; language
```

You can find more info at [the docs](docs/README.md)