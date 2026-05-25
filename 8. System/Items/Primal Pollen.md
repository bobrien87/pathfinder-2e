---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Inhaled]]", "[[Magical]]", "[[Poison]]", "[[Primal]]"]
price: "{'gp': 25}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This magical flower immediately grows and blooms when planted, showering the area with intoxicating pollen. Insects take a –4 penalty on Fortitude saves to resist this poison.

**Saving Throw** DC 20 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** [[Fascinated]] and [[Slowed]] 1 (1 round)

**Stage 2** [[Confused]] and slowed 1 (1 round)

**Stage 3** confused (1 round)

**Stage 4** [[Unconscious]]

**Source:** `= this.source` (`= this.source-type`)
