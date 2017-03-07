# Extracts an official page from wikipedia article and puts it into
# corresponding wikidata page as an attribute
import mwparserfromhell
import pywikibot
import webbrowser
import sys

gtitle = ""
gpage = ""


def parse(title):
    global gtitle
    global gpage

    gtitle = title

    site = pywikibot.Site()
    gpage = pywikibot.Page(site, title)
    text = gpage.get()

    return mwparserfromhell.parse(text)


def findOfficialPage(parsed):
    offPage = ""
    # Trying to find template:
    templates = parsed.filter_templates()
    for template in templates:
        if (template.name.lower() == "oficiali svetainė"):
            offPage = gtitle

    # Trying to find links:
    for link in parsed.filter_external_links():
        print(link.url)

        url = link.url

        webbrowser.open(str(url), new=2)

        status = input('Accept this page? [Y/N]: ')

        if (status == "Y"):
            return str(url)
        else:
            print('Continuing..')

    status = input('Enter custom webpage? [Y/N]: ')

    if (status == "Y"):
        offPage = input('Custom: ')

    return offPage

# Parse command line args
arg = "\n".join(sys.argv[1:])

# Example
text = parse(arg)

offPage = findOfficialPage(text)

if (offPage != ""):
    item = pywikibot.ItemPage.fromPage(gpage)

    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    claim = pywikibot.Claim(repo, 'P856')
    # P856 - official website
    # claims = item.get()['claims']['P856']
    # target = pywikibot.ItemPage(repo, offPage)

    claim.setTarget(offPage)
    item.addClaim(claim)

    # item.editEntity(summary='pyWikibot test edit')
else:
    print('Done nothing.')
