---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 340}"
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

This poison is named for the strain of fungi from which it's distilled. Hallucinations assail the victim's mind, causing them to see imaginary foes.

**Saving Throw** DC 32 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 3d8 poison damage, [[Off Guard]], and can't take reactions (1 round)

**Stage 2** 4d8 poison damage, off-guard, can't take reactions, [[Stunned]] 1 (1 round)

**Stage 3** 5d8 poison damage, off-guard, can't take reactions, and stunned 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
