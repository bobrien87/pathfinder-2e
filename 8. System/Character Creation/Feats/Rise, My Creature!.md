---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lepidstadt Surgeon|Lepidstadt Surgeon]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Lepidstadt Surgeon Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have created life! You have usurped the power of the gods themselves! You gain a prototype construct companion pieced together from corpses and animated by chemicals or Stasian technology. You use Medicine in place of Crafting to Repair your construct or rebuild it if it's been destroyed.

Your creation has an affinity for the lightning that brought it to life. When your construct companion takes electricity damage, it gains a +1 circumstance bonus to its Athletics skill checks until the end of its next turn.

Although the coils or alchemical residue make it obvious to you and those with similar training that your creation is not undead, others must generally succeed at a DC 15 [[Crafting]] check, DC 15 [[Medicine]] check, or DC 15 [[Religion]] check to verify those claims with [[Recall Knowledge]].

**Source:** `= this.source` (`= this.source-type`)
