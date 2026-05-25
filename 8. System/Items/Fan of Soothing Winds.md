---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Air]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This fan of *soothing winds* has six cloud-shaped glass beads on the bottom of the fan, one on each of the exposed ribs. One side of the beads is white, and the other is a dark, stormy gray. Once flipped, a bead stays on its newly exposed side for an entire day before resetting overnight.

**Activate—Healing Wind** `pf2:2` (concentrate)

**Frequency** once per day per bead

**Effect** You open your fan and turn a bead of your choice. The fan casts a 3-action [[Heal]] spell with an area of a @Template[cone|distance:30] instead of a @Template[emanation|distance:30]; the save DC for an undead creature is 28. This spell gains the air trait. The rank of the spell depends on which bead you're turning: the first two beads cast 4th-rank *heal*, the center two cast 3rd-rank *heal*, and the last two cast 2nd-rank *heal*.

**Source:** `= this.source` (`= this.source-type`)
