---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You draw your foe into a fated conflict—one you know you'll win. Choose an enemy within your reach. Until the end of your next turn, that enemy gains a +2 circumstance bonus to attack rolls it makes against you, but it must attempt a [[Will]] save against your class DC whenever it tries to move away from you, Strike a target other than you, or Cast a Spell that doesn't include you as a target. On a failure, the action or actions related to the failed attempt is disrupted. Whenever the enemy misses you with a Strike while this effect is active, you heal @Damage[(1d8+5)[healing]] Hit Points.

> [!danger] Effect: Only You and I

**Source:** `= this.source` (`= this.source-type`)
