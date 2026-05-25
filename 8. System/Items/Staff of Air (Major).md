---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved from white ash wood, a *staff of air* crackles with electrical sparks, and a breeze always follows the wielder. While wielding a *staff of air*, you feel lighter on your feet, and you can Step into difficult terrain once per round.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Gale Blast]]
- **1st** [[Air Bubble]], [[Gust of Wind]]
- **2nd** [[Ash Cloud]], [[Mist]]
- **3rd** [[Blazing Dive]], [[Lightning Bolt]], [[Wall of Wind]]
- **4th** [[Ash Cloud]], [[Air Walk]]
- **5th** [[Blazing Dive]], [[Lightning Storm]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
