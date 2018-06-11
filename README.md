# Duel Masters cards in JSON format

The purpose of this project is to provide a list of Duel Masters cards in JSON format. The list can be used in any way people want eg. in game development or collection tracking. All cards from TCG (Trading Card Game, refers to English cards) are included (from DM-01: Base Set to DM-12: Thrash of the Hybrid Megacreatures) along with the English promotional cards. The goal of this project is to also include all cards from OCG (Original Card Game, refers to Japanese cards). As there are thousands of OCG cards, all contribution towards the completion of this project is greatly appreciated.

## Use

Most programming languages contain libraries which make it possible to deserialize JSON. That way you can instantiate your own card objects which could be used in duels or deck management. Naturally, it is also possible to use the file as a personal collection tracking tool by adding properties such as eg. "owned" and "wanted" to indicate the amount of copies owned or wanted of a card.

## Contribution

All contribution to add missing sets is highly appreciated. If you are interested in collaboration, please create a new issue for the project so I can be add you as an collaborator.

## Format

The cards are represented as a list of JSON objects which include all the information for each card. Each object should have a distinct set-id pair. The cards are sorted by set, then by id. The promotional cards are listed at the end. The common format is as follows:

    {
		"name": "Laser Wing",
		"set": "DM-01 Base Set",
		"id": "11",
		"civilization": "Light",
		"rarity": "Rare",
		"type": "Spell",
		"cost": 5,
		"text": "Choose up to 2 of your creatures in the battle zone. They can't be blocked this turn.",
		"flavor": "This is light speed.",
		"illustrator": "Gyokan"
	}

- name: The name of the card.
- set: The set the card belongs to. As a card with the same name may have multiple printings, there should be a distinct object for each of them. (eg. Faerie Life is included in sets DM-06 and DM-10, there are two distinct objects for Faerie Life)
- id: The collector's number of the card.
- civilization: One of these strings: Light, Water, Darkness, Fire or Nature. Refers to the color of the card (yellow, blue, black, red and green, respectively).
    - civilizations: If the card is multicolored, this property is used instead of the civilization property. It represents a list of the civilizations of the card in a following format (the civilizations must be in the same order as listed in the options):
		
    	    "civilizations": [
    		    "Civilization1",
    		    "Civilization2"
    	    ],
		
- rarity: One of these strings: Common, Uncommon, Rare, Very Rare, Super Rare or None. Refers to the rarity symbol found on the card (dot, diamond, star, star inside a sphere, four squares or no symbol at all, respectively).
- type: One of these strings: Creature, Spell, Evolution Creature or Cross Gear. Refers to the type of the card.
- cost: The mana cost of the card, found the top-left corner of the card.
- text: The rules text of the card which defines its abilities. Multiple clauses are to be separated by \n between them.
- flavor: The flavor text of the card. This property is included only if the card contains a flavor text.
- illustrator: The illustrator of the card.
	
If the type of the card is Creature (includes the subtybes of Creature eg. Evolution Creature) the following properties are included after the illustrator property:
	
    "race": "Light Bringer",
    "power": 2500

- race: The race of the creature. There are a finite amount of different races, the best way of finding them is to refer to existing creature objects.
    - races: If the creature is from multiple races, this property is used instead of the race property. The format is as follows:
		
			"races": [
				"Race1",
				"Race2"
			],
			
	- power: The power of the creature. In the original cards, some creatures have plus-signs on the left side of the power values but here the signs are ignored in order to represent the powers as integers.