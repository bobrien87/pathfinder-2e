---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Alter Ego Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Knowing how someone thinks makes it much easier to know where they'll be, or even replace them altogether. You can cast [[Mind Probe]] as an innate occult spell once per day, using your class DC or spell DC, whichever is higher.

If you cast *mind probe* on a target you're studying for the purpose of Assuming their Role, and the target fails their save, you can delay the spell from coming into effect until you Assume their Role. When you use the spell this way, you can Sustain it up to 10 times during its duration, asking a question each time. The spell lasts until you ask all 10 questions or are no longer Assuming the Role, whichever comes first. You don't need to Sustain the Spell to extend its duration-only when asking a question-nor do you need to be in range or have line of effect to Sustain it.

**Source:** `= this.source` (`= this.source-type`)
