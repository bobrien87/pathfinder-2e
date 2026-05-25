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

Your squad is rejuvenated by the arterial spray of your enemies. Choose a creature within the aura of your commander's banner and signal all squadmates within the aura who are wielding a piercing or slashing melee weapon, or who have a piercing or slashing melee unarmed attack. Those allies can Stride up to half their Speed as a free action. If they end this movement within reach of the designated target, they can Strike the target with the required weapon or unarmed attack as a reaction.

Once all Strikes are completed, if the target took damage and is not immune to bleed damage, it must succeed at a [[Fortitude]] save saving throw against your class DC or take 10 points of persistent bleed damage. The target takes a circumstance penalty on their save equal to the number of successful Strikes made as part of this tactic (up to a maximum –4 circumstance penalty).

> [!danger] Effect: Sanguine Revitalization

Your squadmates are energized by the display of your enemy's imminent defeat; each squadmate in a @Template[type:emanation|distance:20] is healed for 10d6 healing Hit Points.

**Source:** `= this.source` (`= this.source-type`)
