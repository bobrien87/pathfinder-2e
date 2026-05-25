---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 16}"
usage: "affixed-to-a-two-handed-firearm-or-crossbow"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a ranged Strike with the affixed weapon before rolling;

**Requirements** You're a master with the affixed weapon.

This plain wooden bead dangles from a string attached to the stock of the affixed weapon. When you activate the bead, its magic greatly lessens the effect of distance on your triggering attack.

You take no range increment penalty on your attack, as long as the attack is against a target within the affixed weapon's first two range increments.

**Source:** `= this.source` (`= this.source-type`)
