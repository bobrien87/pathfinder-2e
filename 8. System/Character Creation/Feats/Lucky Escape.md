---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Unexpected Sharpshooter|Unexpected Sharpshooter]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Misfortune]]"]
prerequisites: "Unexpected Sharpshooter Dedication"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A creature targets you with an attack, even if you aren't aware of it.

Your enemy lies in wait, lines up the perfect shot, and pulls the trigger... then at just the right moment you duck down to notice something scrawled on the cobblestone in chalk, a shiny coin, or some other coincidental distraction, creating an opportunity for the attack to miss. The attacker must roll the attack twice and use the worse result.

**Source:** `= this.source` (`= this.source-type`)
