---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 150}"
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

**Trigger** You make an attack with the affixed weapon, but you haven't rolled yet

This fluorite crystal glows with a strange phosphorescence. When you activate the crystal, the weapon becomes a *+2 greater striking weapon* on the Strike and until the end of this turn, gaining a +2 item bonus to the attack roll and increasing the damage to three weapon damage dice.

> [!danger] Effect: Potency Crystal

**Source:** `= this.source` (`= this.source-type`)
