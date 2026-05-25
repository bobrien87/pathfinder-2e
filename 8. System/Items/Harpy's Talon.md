---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 3}"
usage: "affixed-to-a-slashing-weapon"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You successfully Strike a creature with the affixed weapon.

This sharp metal claw is used to inflict additional pain upon your enemies. When you activate the harpy's talon, the weapon deals persistent bleed damage equal to the number of weapon damage dice. If the Strike was a critical success, the persistent bleed damage increases to twice the number of weapon damage dice.

> [!danger] Effect: Harpy's Talon

**Source:** `= this.source` (`= this.source-type`)
