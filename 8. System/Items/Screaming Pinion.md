---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Concussive]]", "[[Fatal d10]]"]
price: "{'gp': 3000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking flintlock musket* is an innovation of the Platinum Wing, and possession of one by a civilian is a high crime in Andoran. The gun's secret is the chip of a warshard used as the hammer in the striking mechanism.

**Activate—Transcendent Shot** `pf2:1` (manipulate)

**Requirements** The screaming pinion is unloaded

**Effect** You call on the power of the warshard to load the screaming pinion with a bullet made of divine fury. The next attack from the gun deals spirit damage, rather than its typical type, and on a critical hit, the target is subject to the weapon's critical specialization effect. If the gun isn't fired before the end of your next turn, the bullet disappears, and the gun becomes unloaded.

**Activate—Eagle's Cry** `pf2:2` (concentrate, manipulate, sonic)

**Frequency** once per day

**Effect** The musket unleashes a piercing sound wave in a @Template[type:line|distance:70]. Each creature in the area takes @Damage[8d10[sonic]|options:area-damage] damage with a DC 30 [[Fortitude]] save. A creature that critically fails its save is also [[Deafened]]. If the screaming pinion has a +3 potency rune, the DC increases to 35 (DC 35 [[Fortitude]] save), and the damage increases to @Damage[10d10[sonic]|options:area-damage|shortLabel].

**Source:** `= this.source` (`= this.source-type`)
