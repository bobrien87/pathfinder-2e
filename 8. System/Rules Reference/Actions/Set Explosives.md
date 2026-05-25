---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You have 1 or 2 bombs in hand

**Effect** You attach the bombs to an inanimate object within your reach, such as a door, wall, or column, and rig them to detonate at a set time. The bombs explode at a specific time you determine (such as after your next action or at the start of your next turn, to a maximum of 1 minute), dealing their damage and splash damage to the inanimate object. Combine this damage for the purpose of resistances and weaknesses, and this damage ignores an amount of the object's Hardness equal to your level. Any creatures adjacent to the hazard take the bombs' splash damage, also combined for the purpose of resistances and weaknesses. As a reminder, since you didn't throw the bombs, the Bomber's Field Discovery and similar effects don't apply. Making sure your timing is correct requires concentration, so you can't Set Explosives again while you're waiting for a previously set bomb to detonate.

**Source:** `= this.source` (`= this.source-type`)
