---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lepidstadt Surgeon|Lepidstadt Surgeon]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Medicine, attended the University of Lepidstadt"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Before everything else, before the blood and the monsters and the Stasian technology and the horror, you are a doctor. You are, in fact, an exceptionally good doctor. You become an expert in Medicine.

When you successfully [[Administer First Aid]] to stabilize a dying creature that doesn't yet have the [[Wounded]] condition, it regains @Damage[(2d8 + 10*max(0,(@actor.system.skills.medicine.rank - 2)))[healing]] Hit Points; this healing increases by 10 when you are a master of Medicine and by another 10 when you are legendary in Medicine.

When you successfully Administer First Aid to stop bleeding, the target rolls the flat check (with lowered DC for an assisted recovery) twice and takes the better result; this is a fortune effect.

> [!danger] Effect: Lepidstadt Surgeon Dedication (Stop Bleeding)

Lepidstadt Surgeon

**Source:** `= this.source` (`= this.source-type`)
