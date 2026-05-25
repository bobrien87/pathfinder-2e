---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Kitharodian Actor Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You were once cast in the role of Daronlyr XII, one of Taldor's most ambitious rulers who slew his cousin to seize the crown, yet somehow still managed to convince the entire Ulfen Guard to swear loyalty to him simply through his powers of oration. You attempt a Performance check to launch into a powerful monologue, pulling lines from Daronlyr's playbook to win respect from everyone around you, even your enemies. The DC of this check is a hard difficulty DC of your level. On a success, any hostile creatures within 20 feet take a –2 circumstance penalty to attack rolls and spell attack rolls that target you until the beginning of your next turn, and any allies within 20 feet are [[Quickened]] until the beginning of your next turn. The additional action can be only used to Strike or Stride.

**Source:** `= this.source` (`= this.source-type`)
