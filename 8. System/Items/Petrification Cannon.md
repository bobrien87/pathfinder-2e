---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Concussive]]", "[[Double barrel]]", "[[Fatal d10]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Built from the taxidermic body of a basilisk, a *petrification cannon* functions as a *+2 greater striking double-barreled musket*. A *petrification cannon* can be activated to fire a beam of energy that transforms flesh into stone.

**Activate—Basilisk Beam** `pf2:2` (manipulate, visual)

**Frequency** once per hour

**Effect** A beam of coiling energy leaps from the petrification cannon at a target within 60 feet. The target must attempt a Fortitude save against DC 34 [[Fortitude]] save{DC 34} with the effects of [[Petrify]].

**Craft Requirements** The initial raw materials must include the body of a basilisk.

**Source:** `= this.source` (`= this.source-type`)
