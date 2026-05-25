---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Concussive]]", "[[Fatal d10]]", "[[Magical]]", "[[Staff]]", "[[Void]]"]
price: "{'gp': 100}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A stock carved of enchanted wood forms the base for a *musket staff*, a magic weapon used by a gunwitch as both a powerful firearm and magical staff. Many other variants exist with different spells. This *+1 flintlock musket* has a [[Reinforced Stock]] permanently attached to it, and the musket's *weapon potency* rune (and any other runes) applies to Strikes with the stock as well. The *musket staff* also contains spells and can be prepared following the same rules as a staff.

- **Cantrip** [[Void Warp]]

- **1st** [[Grim Tendrils]]

**Source:** `= this.source` (`= this.source-type`)
