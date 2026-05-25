---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 6250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The bladed inner curve of this *+2 greater striking keen wounding dagger* has a jagged, saw-like edge, while its handle is wrapped in red leather. Carved from the mandible of a giant praying mantis, this magical weapon's blade is as sharp and serviceable as steel.

**Activate—Sweeping Slash** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You swing the dagger in a wide arc, causing a horizontal swipe of blood-red energy to sweep out in a @Template[cone|distance:30]. All living creatures in the area take @Damage[15d6[slashing]|options:area-damage] damage (DC 34 [[Reflex]] save), plus 1d6 bleed damage on a failed save.

**Source:** `= this.source` (`= this.source-type`)
