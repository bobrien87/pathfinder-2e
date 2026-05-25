---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Deadly d8]]", "[[Disarm]]", "[[Electricity]]", "[[Finesse]]", "[[Magical]]"]
price: "{'gp': 21000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+3 greater striking greater shock rapier* has a golden blade, and miniature electric arcs flash across its guard while it's wielded. When out of its sheath under an open sky, the blade causes storm clouds to gather slowly above.

**Activate—Lightning Stab** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast a 8th-rank [[Lightning Bolt]] (DC 38).

**Activate—Divert Lightning** R (concentrate)

**Frequency** once per 10 minutes

**Trigger** An electricity effect targets you or a creature within 10 feet of you, or has you or a creature within 10 feet of you in its area

**Effect** You try to divert the electricity off course, to be absorbed by *storm flash*. Choose one eligible creature to protect and roll a melee attack roll against the DC of the electricity effect. If you succeed, the chosen creature takes no electricity damage from the triggering effect.

**Source:** `= this.source` (`= this.source-type`)
