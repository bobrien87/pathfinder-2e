---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Kitharodian Actor Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are unarmored.

You clear your mind, regulate your breathing, and prepare your muscles in a stance inspired by Kemen Kayton, a graduate of Zimar's Monastery of the Seven Forms. Kemen controversially shunned monastic life and instead used his martial skills as a death-defying stunt performer, winning acclaim for exhibitions that saw him survive great falls and escape deadly traps. While in this stance, you gain a +2 circumstance bonus to Reflex saving throws and skill checks to [[Escape]], as well as resistance 2 to all physical damage.

**Source:** `= this.source` (`= this.source-type`)
