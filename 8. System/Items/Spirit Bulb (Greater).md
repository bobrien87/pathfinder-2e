---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]", "[[Plant]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

This magical bulb is harvested from an ancient grove rich in primal plant magic. When you activate the bulb, you either eat it to have it cast a 6th-rank [[Plant Form]] spell affecting you, or plant it in the ground next to you to have it cast a 6th-rank [[Summon Plant or Fungus]] spell. If you choose the summoning option, the plant or fungus appears where you planted the bulb, and you can Sustain the activation to keep control of the creature.

**Source:** `= this.source` (`= this.source-type`)
