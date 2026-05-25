---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 240}"
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

This toxin erratically stimulates the limbs, forcing unexpected shifts in momentum. The result resembles a gangly, lurching dance. At the start of each turn, the victim takes one or more Steps in a random direction if able. This movement is forced and doesn't count against the victim's actions for the round.

**Saving Throw** DC 30 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 4d6 poison and 1 Step of forced movement (1 round)

**Stage 2** 6d6 poison, [[Clumsy]] 1, and 1 Step of forced movement (1 round)

**Stage 3** 8d6 poison, [[Clumsy]] 2, 2 Steps of forced movement (1 round)

**Source:** `= this.source` (`= this.source-type`)
