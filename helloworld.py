import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "bella-donna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

 print [word for word in words if re.search(regex, word)]

get_matching_words('^a*')
