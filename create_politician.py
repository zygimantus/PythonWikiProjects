# https://gist.github.com/k-nut/0240051a47663d5a128e6fa9dfc80170
import pywikibot

def create_bavarian_politician(name):
    """
    Creates a new entry in test.wikdata.org
    :return:
    """
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()

    data = {
        'labels': {
            'en': {
                'language': 'en',
                'value': name,
            },
            'de': {
                'language': 'de',
                'value': name,
            }
        }
    }
    item = pywikibot.ItemPage(site)

    claim = pywikibot.Claim(repo, u'P39')
    target = pywikibot.ItemPage(repo, u"Q17586301")
    claim.setTarget(target)
    item.editEntity(data)

    item.addClaim(claim)

create_bavarian_politician("Florian Hölzl")
