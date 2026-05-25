---
type: action
source-type: "Remaster"
traits: ["[[Leshy]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're on a solid surface

**Effect** You send your roots into or across the ground, making it harder for you to stumble. Until you move, you gain a +2 circumstance bonus to your Fortitude or Reflex DC against attempts to [[Reposition]], [[Shove]], or [[Trip]] you (or a +4 circumstance bonus if you're a root leshy). This bonus also applies to saving throws against spells or effects that attempt to move you or knock you [[Prone]]. If an effect forces you to move, you move only half the normal distance, as some of the effort goes to tearing loose the roots.

**Source:** `= this.source` (`= this.source-type`)
