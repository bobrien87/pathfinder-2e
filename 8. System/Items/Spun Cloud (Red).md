---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

On the Elemental Plane of Air, small clouds of differing colors can sometimes float separately from other cloud formations. Clever people can spin these clouds into small handfuls, creating a magical bundle of elemental power. Unlike most bottled breath, *spun clouds* don't have any effect on you while you hold them in your lungs, but you can exhale the cloud as a single action. When exhaled, the cloud flows out and expands into a @Template[burst|distance:20] within 60 feet of you. The cloud dissipates after 1 minute.

A red cloud terrifies those it surrounds. Any creature in the cloud, or that later enters the cloud, must succeed at a DC 24 [[Will]] save or become [[Frightened]] 2 (or [[Frightened]] 3 on a critical failure). Regardless of the result of its save, the creature becomes temporarily immune for 24 hours. This is an emotion, fear, and mental effect.

**Source:** `= this.source` (`= this.source-type`)
