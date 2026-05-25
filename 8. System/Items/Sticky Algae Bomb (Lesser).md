---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Splash]]", "[[Water]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

These bombs have been mixed with sticky algae that glow and emit poison. Attacks with this bomb don't take the normal penalties and restrictions for being used in water or underwater. The bomb deals 1d8 poison damage and 1 poison splash damage. In addition, the target is tagged by the bioluminescent substance and leaves a highly visible trail for the next hour. The DC to [[Track]] a creature using this trail is 19, but the trail appears only in water.

**Source:** `= this.source` (`= this.source-type`)
