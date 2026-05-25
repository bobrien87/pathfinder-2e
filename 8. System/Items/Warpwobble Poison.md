---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Mental]]", "[[Poison]]"]
price: "{'gp': 90}"
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

Warpwobble poison causes hallucinations of space bending and stretching, leading to vertigo and an inability to discern a stable place to move.

**Saving Throw** DC 26 [[Will]] save

**Maximum Duration** 6 rounds

**Stage 1** treat all squares as difficult terrain (1 round)

**Stage 2** treat all squares as greater difficult terrain (1 round)

**Stage 3** treat all squares as uneven ground (DC 26), treating a critical success to [[Balance]] as a success, and a success as a success but moving on greater difficult terrain (1 round)

**Source:** `= this.source` (`= this.source-type`)
