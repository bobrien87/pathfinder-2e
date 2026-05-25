---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Force]]", "[[Magical]]", "[[Poison]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 37500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This slender metal wand is tinted green and small images of bladed weapons are etched on its surface.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 8th-rank [[Blessed Boundary]]. Damage from the wall also exposes the damaged creature to [[Cerulean Scourge]]. The poison uses its normal DC. A creature can be exposed to the poison no more than once per turn.

**Craft Requirements** Supply a casting of [[Blessed Boundary]] of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
