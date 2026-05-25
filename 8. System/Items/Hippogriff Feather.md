---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

Tawny-colored hippogriff feathers can be up to 2 feet long. Used as a catalyst with a [[Ghostly Carrier]] spell, a single *hippogriff feather* grants the hand semicorporeal wings that increase the hand's maneuverability. The hand has a range of only 60 feet, but its increased agility grants it a +1 status bonus to its AC and Reflex saves.

**Source:** `= this.source` (`= this.source-type`)
