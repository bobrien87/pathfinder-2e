---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]", "[[Visual]]"]
price: "{'gp': 150}"
usage: "affixed-to-a-shield"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You [[Shield Block]] a melee attack with the affixed shield

This slimy green stone glows with a strong light whenever the shield it adorns blocks a melee attack. When the eye is activated, the attacker must succeed at a DC 25 [[Fortitude]] save or become [[Slowed]] 1 for 1 minute as its body slowly stiffens in partial petrification.

**Source:** `= this.source` (`= this.source-type`)
