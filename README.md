# Online Spell Checker

A script to check spelling using google translate.

## Requirements
* Python 2.7
* Selenium (https://pypi.python.org/pypi/selenium)

## USAGE
Import the script
```
import OnlineSpellChecker
```
Get browser handler instance
```
hnd = OnlineSpellChecker.get_handler(<browsertype>)
```
Browser supported: 0 - Chrome, 1 - Firefox, 2 - Safari, 3 - Opera, 4 - Edge
Call the function OnlineSpellChecker.spell_check(handler,list_of_word,language)
```
print OnlineSpellChecker.spell_check(hnd,["belng","rserch"],"en")
```

## Example
With the following script
```
import OnlineSpellChecker

wordId = ["masyrkt","manosia","mskpun","bgimana","menjadekn","mengtakn","harimoa"]
wordEn = ["belng","rserch","apprximtion","whrever","mistke","abdemon","shllw"]

hnd = spellchecker.get_handler(0)
print spellchecker.spell_check(hnd,wordEn,"en")
print spellchecker.spell_check(hnd,wordId,"id")
spellchecker.quit_browser(hnd)
```
The result is:
```
[['belng', u'belong'], ['rserch', u'research'], ['apprximtion', u'approximation'], ['whrever', u'wherever'], ['mistke', u'mistake'], ['abdemon', u'abdomen'], ['shllw', u'shallow']]
[['masyrkt', u'masyarakat'], ['manosia', u'manusia'], ['mskpun', u'meskipun'], ['bgimana', u'bagaimana'], ['menjadekn', u'menjadikan'], ['mengtakn', u'mengatakan'], ['harimoa', u'harimau']]
```

## Accuracy
This technique still yields many mistakes. It is not accurate indeed, but it worths to try at least for the first step of word normalization. I am trying to improve it.

## License
MIT License
