---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]"]
price: "{'gp': 12}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

The delicate process of extracting violet venom from a violet fungus leaves it diluted at the best of times. Alchemists are still on the hunt for a truly pure, unadulterated version of this highly toxic poison.

**Saving Throw** DC 17 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 rounds

**Stage 1** 1d6 poison plus [[Enfeebled]] 1 (1 round)

**Stage 2** 1d6 poison plus [[Drained]] 1 (1 round)

**Stage 3** 2d6 poison plus enfeebled 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
