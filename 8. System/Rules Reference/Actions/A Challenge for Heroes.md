---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Mental]]", "[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You declare an enemy within 60 feet to be a heroic test. For 1 minute, that enemy deals an additional 10 spirit damage to you with each successful Strike or spell it targets you with.

> [!danger] Effect: A Challenge for Heroes (Enemy)

Whenever that enemy deals spirit damage to you, each ally who has the enemy in melee reach can attempt a [[Reactive Strike]] against it, even if the ally doesn't normally have that reaction. If an ally successfully slays the enemy with a Reactive Strike due to this effect, that ally immediately gains temporary Hit Points equal to your level, which persist for 1 minute.

> [!danger] Effect: A Challenge for Heroes (Ally)

**Source:** `= this.source` (`= this.source-type`)
