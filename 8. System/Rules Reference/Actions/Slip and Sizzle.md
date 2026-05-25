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

Your team executes a brutal technique designed to knock down an opponent and blast them with magical devastation. Signal up to two squadmates within the aura of your commander's banner; one of these squadmates must be adjacent to an opponent and the other must be capable of casting a spell that deals damage. The first squadmate can attempt to [[Trip]] the adjacent opponent as a reaction. If this Trip is successful, the second squadmate can cast a ranged spell that deals damage and takes 2 or fewer actions to cast. This spell is cast as a reaction and must either target the tripped opponent or include the tripped opponent in the spell's area.

If the second squadmate cast a spell using slots or Focus Points as part of this tactic, they are [[Slowed]] 1 until the end of their next turn and do not gain a reaction when they regain actions at the start of their next turn.

**Source:** `= this.source` (`= this.source-type`)
