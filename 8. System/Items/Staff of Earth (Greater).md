---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 450}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Geometric patterns are etched into the smooth brown-and-gray surface of a *staff of earth*, which makes a solid, resonant thud whenever tapped against the ground. While wielding a *staff of earth*, you gain a +1 circumstance bonus to your Fortitude saves and DC against effects that [[Shove]] you or knock you [[Prone]].

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Scatter Scree]]
- **1st** [[Pummeling Rubble]]
- **2nd** [[Expeditious Excavation]], [[Pummeling Rubble]]
- **3rd** [[Earthbind]], [[Shifting Sand]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
