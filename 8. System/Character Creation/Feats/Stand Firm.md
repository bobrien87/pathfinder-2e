---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Linguistic]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your words help your ally shake off unease and terror. You shout a bolstering comment at an ally within 30 feet of you who has the [[Fleeing]] or [[Frightened]] condition and can hear you. That ally reduces the value of their frightened condition by 2 (to a minimum of 0). If they are fleeing, they can immediately attempt a new saving throw against the effect that caused the condition. If that save is a failure, but not a critical failure, the ally needs to spend one fewer action on their turn to escape the source of the fleeing condition. This allows that ally to Strike or Cast a one-action Spell that doesn't necessarily get them further away from the source, but the ally still has the fleeing condition and can't Delay or Ready as usual. If the ally is under an effect that reduces the number of actions they have on their turn, they don't gain this benefit on a failed saving throw. Once you use Stand Firm on an ally, that ally is immune to it until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
