---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 625}"
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

The spores of a certain mushrooms, if carefully collected and suspended in a properly mixed alchemical fluid, can kill those near death. If a creature is reduced to 0 Hit Points while under the effect of execution powder, it must succeed at a DC 34 [[Will]] save or die (this is a death effect). If a creature dies from execution powder, the spores from their last breath alight on a random creature adjacent to the victim, granting that creature 20 temporary Hit Points and a +1 status bonus to attack and damage rolls for 10 minutes.

**Saving Throw** DC 34 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 7d6 poison damage (1 round)

**Stage 2** 9d6 poison damage (1 round)

**Stage 3** 12d6 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
