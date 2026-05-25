---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:2`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your careful shot against an unsuspecting opponent pierces a vital artery or organ. Make a ranged Strike. If the target is [[Off Guard]], the Strike deals an extra die of weapon damage, and the foe takes persistent bleed damage equal to the amount of precision damage from your [[One Shot, One Kill]].

**Source:** `= this.source` (`= this.source-type`)
