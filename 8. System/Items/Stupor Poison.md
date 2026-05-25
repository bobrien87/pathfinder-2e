---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Incapacitation]]", "[[Injury]]", "[[Poison]]", "[[Sleep]]"]
price: "{'gp': 16}"
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

Stupor poison is a more potent distillation of lethargy poison. Further exposure to stupor poison doesn't require the target to attempt additional saving throws; only failing a saving throw against an ongoing exposure can progress its stage.

**Saving Throw** DC 20 [[Fortitude]] save

**Maximum Duration** 6 hours

**Stage 1** [[Slowed]] 1 and [[Off Guard]] (1 round)

**Stage 2** [[Slowed]] 2 and off-guard (1 round)

**Stage 3** [[Unconscious]] with no Perception check to wake up (1 round)

**Stage 4** unconscious with no Perception check to wake up (1d6 hours)

**Source:** `= this.source` (`= this.source-type`)
