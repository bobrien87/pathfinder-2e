---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This colorless mist has a mild, waxy scent that precedes acute shortness of breath. Creatures that don't need to breathe can still take the poison's damage but are immune to its other effects.

**Saving Throw** DC 38 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** 6d6 poison damage, [[Drained]] 1, and can't breathe

**Stage 2** 8d6 poison damage, [[Drained]] 2, and reduce remaining air by 1 additional round

**Stage 3** 10d6 poison damage, [[Drained]] 3, and reduce remaining air by 2 additional rounds

**Source:** `= this.source` (`= this.source-type`)
