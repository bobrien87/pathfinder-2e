---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Consumable]]", "[[Magical]]", "[[Scroll]]"]
price: "{'gp': 8000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Casting a Spell from a scroll requires holding the scroll in one hand and activating it with a Cast a Spell activity using the normal number of actions for that spell.

The spell must appear on your spell list. Because you're the one Casting the Spell, use your spell attack modifier and spell DC. The spell also gains the appropriate trait for your tradition (arcane, divine, occult, or primal).

Any physical costs are provided when a scroll is created, so you don't need to provide them when casting from a scroll. If the spell requires a locus, you must have that locus to Cast the Spell from a scroll.

*Note: To create a scroll or wand of a specific spell, drag the spell from the compendium or compendium browser into the inventory of a PC, NPC, or loot actor.*

**Source:** `= this.source` (`= this.source-type`)
