---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Artifact]]", "[[Cold]]", "[[Deadly d10]]", "[[Divine]]", "[[Propulsive]]"]
price: "{'value': {}}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The B*ow of Sun Slaying* is a *+3 major striking greater frost composite shortbow* constructed out of wood, horn, and sinew. It bears carvings of a long-forgotten demigod who legends say possessed the ability to destroy the sun with a single arrow.

**Activate—Darkness for My Foes** `pf2:1` (concentrate)

**Frequency** once per day

**Requirements** Your last action was a successful Strike against your foe with this weapon

**Effect** You whisper, "Darkness for my foes," and the target of your last attack takes @Damage[(10d6)[cold],(10d6)[spirit]] damage (DC 45 [[Will]] save).

**Source:** `= this.source` (`= this.source-type`)
