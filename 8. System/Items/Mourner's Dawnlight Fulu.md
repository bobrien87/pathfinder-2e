---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 120}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (concentrate, manipulate)

A *mourner's dawnlight fulu* is a stack of pages that resembles joss paper, used to locate the remains of the lost. When you Activate the fulu, you envision a specific object or deceased creature you're familiar with and want to find. You then rip the fulu into pieces and let them drift in the wind. If the item or creature you seek is within 500 feet, the pieces flutter through the air and land on the target, or on the surface closest to a buried or otherwise obscured target. If the torn fulu lands or fails to locate the desired target, its magic ends.

**Source:** `= this.source` (`= this.source-type`)
