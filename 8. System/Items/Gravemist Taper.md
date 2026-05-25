---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

A *gravemist taper* is a conical candle with symbols of terror and death carved into the wax. The taper can be used as a catalyst when casting a [[Mist]] spell, burning the taper away, coloring the mist gray, and filling the mist with ghastly, shadowy shapes. The flat check to overcome the [[Concealed]] state from the mist rises to 7, and a creature who fails such a check becomes [[Frightened]] 1. This aspect of the spell has the emotion, fear, and mental traits.

**Source:** `= this.source` (`= this.source-type`)
