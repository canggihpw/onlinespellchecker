# -*- coding: utf-8 -*-
"""
OnlineSpellChecker.py
Spell checker using google translate

USAGE:
# import the module
import OnlineSpellChecker
# create instance
hnd = OnlineSpellChecker.get_handler(<browsertype>)
# browsertype:
# 0 - Chrome
# 1 - Firefox
# 2 - Safari
# 3 - Opera
# 4 - Edge
#print OnlineSpellChecker.spell_check(hnd,list_of_word,language)
print OnlineSpellChecker.spell_check(hnd,["belng","rserch"],"en")
---
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_handler(browserType):
    try:        
        # Load driver
        if browserType == 0:
            browser = webdriver.Chrome()
        elif browserType == 1:
            browser = webdriver.Firefox()
        elif browserType == 2:
            browser = webdriver.Safari()
        elif browserType == 3:
            browser = webdriver.Opera()
        elif browserType == 4:
            browser = webdriver.Edge()
        else:
            browser = webdriver.Chrome()
    except Exception:
        print Exception.message
    return browser

def spell_check(handler,data,lang):
    # Use Zulu only to make the page loads
    addr = "https://translate.google.com/#" + lang + "/zu/"
    correctedword = []
    for word in data:
        word = word.strip()
        try:
            # Load page
            handler.get(addr + word)
            
            # Wait until certain element is present
            try:
                checkelem = WebDriverWait(handler,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,"#spelling-correction"))
                )
            except Exception:
                print Exception.message
        
        except Exception:
            print Exception.message
        
        finally:
            if handler.find_element_by_css_selector("#spelling-correction").text == "":
                result = word
            else:
                result = handler.find_element_by_css_selector("#spelling-correction>a").text
            
            correctedword.append([word,result])

            # Open new tab to reset the page
            handler.execute_script("window.open('');")
            
            # Close the previous tab
            # Not so good implementation
            wdh = handler.window_handles
            handler.switch_to_window(wdh[1])
            handler.switch_to_window(wdh[0])
            handler.close()
            wdh = handler.window_handles
            handler.switch_to_window(wdh[0])
    return correctedword

# Close web browser application
def quit_browser(handler):
    handler.quit()