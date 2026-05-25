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

A *ghostcracker* pops and smokes when consumed. When you throw the *ghostcracker* down in your space as part of casting an [[Illusory Creature]] spell, the appearance of the creature twists nightmarishly. When an enemy's attack or spell ends the *illusory creature* spell, the creature "dies" in a disturbing fashion, rendering the enemy [[Frightened]] 1. From this effect, the ghostcracker adds the emotion, fear, and mental traits to the spell.

**Source:** `= this.source` (`= this.source-type`)
