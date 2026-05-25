---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 striking frost staff* is an heirloom that was gifted to Alzarius by his mother when he made his choice to remain in Xer. It is a gift he claims has been handed down through generations of spellcasters in his family.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Frostbite]]
- **2nd** [[Environmental Endurance]], [[Resist Energy]]
- **3rd** [[Environmental Endurance]], [[Slow]], [[Wall of Wind]]
- **4th** [[Ice Storm]], [[Resist Energy]], [[Vapor Form]]
- **5th** [[Environmental Endurance]], [[Howling Blizzard]], [[Wall of Ice]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
