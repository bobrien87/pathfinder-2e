---
type: action
source-type: "Remaster"
traits: ["[[Fire]]", "[[Healing]]", "[[Light]]", "[[Visual]]"]
cast: "`pf2:3`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're transformed into phoenix form by the monstrosity form spell granted by this feat

**Effect** You dismiss phoenix form while a fiery corona erupts from you as searing light. Each creature in a @Template[type:burst|distance:10] takes @Damage[max(16,(2*(floor(@actor.level/2))))d6[fire]|options:area-damage] damage with a [[Fortitude]] save against your spell DC; creatures that critically fail are [[Blinded]] for 1 round. You gain 8d6 temporary Hit Points. At 18th level and again at 20th level, the burst deals an additional 2d6 fire damage, and you gain an additional 1d6 temporary Hit Points.

**Source:** `= this.source` (`= this.source-type`)
