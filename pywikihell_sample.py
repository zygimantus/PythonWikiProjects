# Sample of pywikibot usage
import mwparserfromhell
import pywikibot

def parse(title):
    site = pywikibot.Site()
    page = pywikibot.Page(site, title)
    text = page.get()
    return mwparserfromhell.parse(text)

# Example
text = parse('Europos parkas')
print(text)

print('---------------')
# parsing templates
templates = text.filter_templates()
print(templates)
template = templates[0]
print(template)
print(template.name)
print(template.params)
print(template.get("įkurtas").value)
