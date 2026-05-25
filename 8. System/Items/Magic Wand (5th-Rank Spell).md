---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This baton is about a foot long and contains a single spell. The appearance typically relates to the spell within.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell at the indicated rank.

**Craft Requirements** Supply a casting of the spell at the listed rank.

*Note: To create a scroll or wand of a specific spell, drag the spell from the compendium or compendium browser into the inventory of a PC, NPC, or loot actor.*

**Source:** `= this.source` (`= this.source-type`)
