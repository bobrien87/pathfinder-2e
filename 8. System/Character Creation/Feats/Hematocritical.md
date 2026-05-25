---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bloodrager|Bloodrager]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Fortune]]", "[[Rage]]"]
prerequisites: "Bloodrager Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a Strike that critically hit a creature that isn't immune to bleed damage.

You bathe in the arterial fluids of your enemy, drinking deep of their freed essence to empower your magic and increase your spellcasting efficacy. If your next action is to Cast a Spell that requires a spell attack roll, you roll the spell attack roll twice and use the better result; this is a fortune effect. Alternatively, if your next action is to cast a spell that requires the creature damaged by the triggering strike to attempt a save, they roll twice and take the lower result; this is a misfortune effect.

**Source:** `= this.source` (`= this.source-type`)
