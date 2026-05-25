---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 50}"
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

A blue cloud protects against lightning. Creatures gain resistance 5 to electricity while in the cloud.

> [!danger] Effect: Spun Cloud (Blue)

**Source:** `= this.source` (`= this.source-type`)
