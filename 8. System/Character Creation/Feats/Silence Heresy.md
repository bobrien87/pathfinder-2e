---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "0"
prerequisites: "Order of the Rack"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You channel a power that stifles dangerous words. Make a melee Strike. If the attack hits, the target is unable to speak in a voice louder than a whisper for 1 round. This prevents the target from using most auditory effects involving its voice, and it must succeed at a DC 5 flat check to Cast a Spell with a verbal component or the spell is disrupted. If your Strike is a critical hit, the target is entirely unable to speak for 1 round and is limited to a whisper for 1 minute thereafter. Once a creature has been affected by this ability, it is temporarily immune for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
