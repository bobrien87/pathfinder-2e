---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 45}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` Interact

**Saving Throw** DC 22 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** 2d6 poison damage and [[Stunned]] 1 (2 rounds)

**Stage 2** 2d6 poison damage and [[Confused]] (1 round)

**Stage 3** 2d6 poison damage and controlled (2 days)

**Stage 4** dead. A creature that dies while infected with creeping death immediately releases a burst of spores in a @Template[emanation|distance:15], exposing creatures in the area to creeping death. If the corpse of a creature killed by creeping death isn't burned, it rises as the host of a cythnophorian 12 hours later.

**Source:** `= this.source` (`= this.source-type`)
