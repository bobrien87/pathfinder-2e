---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:3`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

Your squad rallies with a resounding clangor that drowns out all other sounds of war. Choose an enemy you are observing and signal all squadmates within the aura of your commander's banner. All squadmates can Stride up to twice their Speed directly toward the target as a reaction, yelling and trampling. When any squadmate enters a square adjacent to any enemy, that enemy must attempt a [[Fortitude]] save against your class DC or take @Damage[2d6[bludgeoning],2d6[sonic]|options:inflicts:deafened]{2d6 bludgeoning damage and 2d6 sonic damage} damage, plus an additional 2d6 bludgeoning and 2d6 sonic damage for every squadmate participating in Cry Havoc! (enemies who critically fail are [[Deafened]] for 1 round). Regardless of the outcome, the enemy is then temporarily immune to any further damage from Cry Havoc! for 24 hours.

Squadmates can use Cry Havoc! while Burrowing, Climbing, Flying, or Swimming instead of Striding if they have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
