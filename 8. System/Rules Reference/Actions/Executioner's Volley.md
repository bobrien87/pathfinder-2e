---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

You command your squadmates to act as a lethal firing squad. You and each squadmate within the aura of your commander's banner can attempt a ranged Strike as a reaction against a single target you choose; combine the damage from all attacks for the purpose of resistances and weaknesses. If the designated target is a living creature, these attacks gain the death trait. If the designated target dies as a result of this tactic, all other enemies within the affected area of your commander's banner must succeed at a [[Will]] save against your class DC or be [[Frightened]] 2; this is an emotion, fear, and mental effect.

**Special** If one of your squadmates knows or has prepared a cantrip with a range of 30 feet or more that deals damage and requires 2 or fewer actions to cast, they can cast it targeting the designated enemy instead of taking the other actions normally granted by this tactic, gaining all other listed benefits.

**Source:** `= this.source` (`= this.source-type`)
