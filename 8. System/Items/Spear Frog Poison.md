---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 3}"
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

Carefully harvested from the skin of the poisonous spear frog, this toxin causes a burning rash and weakness in the limbs. Each frog yields enough toxin to Craft one dose of spear frog poison.

**Saving Throw** DC 15 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d4 poison damage (1 round)

**Stage 2** 1d6 poison damage and [[Enfeebled]] 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
