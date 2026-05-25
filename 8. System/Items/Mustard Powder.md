---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 25}"
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

Concocted from the formulas provided by otherworldly refugees to Irrisen, mustard powder is rumored to be devastating to entire armies with proper dispersal. Recipes have quickly spread across Golarion. Mustard powder's sickened condition ends when the poison's other effects do.

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d6 poison and [[Dazzled]] (1 round)

**Stage 2** 2d4 poison, dazzled, [[Sickened]] 1, and unable to smell (1 round)

**Stage 3** 2d6 poison, dazzled, [[Sickened]] 2, and unable to smell (1 round)

**Source:** `= this.source` (`= this.source-type`)
