---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 3}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You critically succeed at an attack roll with the affixed weapon

This claw set in an iron clasp and chain is usually that of a large predator. When you activate the claw, the triggering attack gains the weapon's critical specialization effect.

> [!danger] Effect: Predator's Claw

**Source:** `= this.source` (`= this.source-type`)
