---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 45}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Prepared from brown mold, this liquid oscillates between rapidly absorbing and releasing heat from its victim. Each round the type of damage dealt by this poison changes, starting with cold, then fire, then cold, and so on. If the victim of this poison takes cold damage from a source other than the oil, reduce the save DC to 22 for 1 round. If the victim takes fire damage from a source other than the oil, increase the save DC to 25 for 1 round.

**Saving Throw** DC 24 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 2d6 cold or fire damage (1 round)

**Stage 2** 3d6 cold or fire damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
