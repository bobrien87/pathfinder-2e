---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 4500}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rugged suit of *+2 resilient fortification full plate* has a large red gemstone inset into the overlapping plates of the chest piece. While wearing the armor, you might be given the role of protecting the flank of an army in battle, or perhaps standing your ground as the last line of defense in a castle keep.

**Activate—Phalanx** `pf2:3` (concentrate, manipulate, metal)

**Frequency** once per day

**Effect** You raise walls of rapidly shifting metal plates in two @Template[type:line|distance:60]{60-foot lines} going in opposite directions. Each wall is 60 feet high and is greater difficult terrain. Whenever a creature enters or starts their turn in the wall's space, they take @Damage[6d10[slashing]|options:area-damage|traits:concentrate,manipulate,mental] damage (DC 32 [[Fortitude]] save). The shifting walls also provide greater cover from any attack originating from the opposite side.

**Source:** `= this.source` (`= this.source-type`)
