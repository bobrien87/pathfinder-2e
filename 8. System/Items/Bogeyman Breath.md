---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Fear]]", "[[Inhaled]]", "[[Mental]]", "[[Poison]]"]
price: "{'gp': 360}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This dust is created from the powdered bones of ensnared rabbits and other woodland creatures that died from fright. When inhaled, it pollutes the victim's mind with fear, awakening an unshakable prey response that sees danger lurking in every shadow.

**Saving Throw** DC 28 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** 4d6 mental damage, [[Frightened]] 1, and can't reduce frightened value for 1 round (1 round)

**Stage 2** 4d6 mental damage, [[Frightened]] 2, and can't reduce frightened value for 1 round (1 round)

**Stage 3** 4d6 mental damage, frightened 2, [[Fleeing]] the poison cloud for 1 round, and can't reduce frightened value for 1 round (1 round)

**Source:** `= this.source` (`= this.source-type`)
