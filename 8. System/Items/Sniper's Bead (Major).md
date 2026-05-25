---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 1600}"
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

You take no range increment penalty on your attack, even if the target is all the way out to the weapon's sixth range increment. As normal, you still can't hit a target more than six range increments away.

**Source:** `= this.source` (`= this.source-type`)
