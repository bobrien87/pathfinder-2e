---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Inhaled]]", "[[Poison]]"]
price: "{'gp': 1000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Mindfog mist can be used to undermine spellcasters, as its effect on a victim's mental faculties are swift and powerful.

**Activate** A (manipulate)

**Saving Throw** DC 35 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** [[Stupefied 2]] (1 round)

**Stage 2** [[Confused]] and [[Stupefied 3]] (1 round)

**Stage 3** [[Confused]] and [[Stupefied 4]] (1 round)

**Source:** `= this.source` (`= this.source-type`)
