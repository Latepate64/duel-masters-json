import collections
import json

def sort_by_name(card):
	return card["name"]

def main():
	data = json.load(open('DuelMastersCards.json'))
	cards = data['cards']
	cards = [collections.OrderedDict(sorted(card.items())) for card in cards]
	cards.sort(reverse=False, key=sort_by_name)
	data['cards'] = cards
	print(json.dumps(data))

if __name__ == "__main__":
    main()