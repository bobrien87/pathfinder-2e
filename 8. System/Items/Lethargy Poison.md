---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Incapacitation]]", "[[Injury]]", "[[Poison]]", "[[Sleep]]"]
price: "{'gp': 7}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Lethargy poison is commonly used in hit-and-run tactics by attackers who want their victims alive; the ambusher retreats until the poison sets in and the victim falls unconscious. Further exposure to lethargy poison does not require the target to attempt additional saving throws; only failing an saving throw against an ongoing exposure can progress its stage.

**Activate** `pf2:2` (manipulate)

**Saving Throw** DC 18 [[Fortitude]] save

**Maximum Duration** 4 hours

**Stage 1** [[Slowed]] 1 (1 round)

**Stage 2** [[Slowed]] 1 (1 minute)

**Stage 3** [[Unconscious]] with no Perception check to wake up (1 round)

**Stage 4** [[Unconscious]] with no Perception check to wake up (1d4 hours).

**Source:** `= this.source` (`= this.source-type`)
