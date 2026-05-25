---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

The echo of kirin's song can be captured within this small glass chime, which shatters and calls up a meandering breeze of its own when rung. Adding this catalyst to a [[Gust of Wind]] spell causes any flying creatures that would be pushed by the spell's effects to be pushed 30 feet in a direction of your choice, rather than 30 feet in the direction of the spell.

**Source:** `= this.source` (`= this.source-type`)
