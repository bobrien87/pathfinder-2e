---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Magaambyan Attendant|Magaambyan Attendant]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Skill]]"]
prerequisites: "Mask Familiar, expert in Stealth"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wearing your [[Mask Familiar]] in its mask form, and it has the [[Skilled]] (Religion) familiar ability.

Your mask can hide you from the undead. You become [[Concealed]] to undead using vision or lifesense, allowing you to [[Hide]] and [[Sneak]] without other sources of cover or concealment. This effect lasts only as long as you continue to take no actions other than to Hide, Sneak, [[Recall Knowledge]], [[Command an Animal]] to direct your mask familiar, or other surreptitious actions. The GM determines which actions end the effect, but attacking, casting spells, activating items, and the like always do.

**Source:** `= this.source` (`= this.source-type`)
