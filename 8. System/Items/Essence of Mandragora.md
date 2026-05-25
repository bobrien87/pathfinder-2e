---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 20}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This poison is extracted carefully from a mandragora's thorny vines in a process that, due to the mandragora's humanoid form, eerily mirrors drawing blood.

**Saving Throw** DC 21 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 1d6 poison damage and [[Stupefied 1]] (1 round)

**Stage 2** 1d6 poison damage, [[Confused]], and stupefied 1 (1 round)

**Stage 3** 2d6 poison damage, confused, and stupefied 1 (1 round)

**Source:** `= this.source` (`= this.source-type`)
