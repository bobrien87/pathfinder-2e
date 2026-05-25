---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sister Of The Golden Erinys|Sister Of The Golden Erinys]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Aura]]", "[[Divine]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "Sister of the Golden Erinys Dedication"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You channel the unending wrath of the erinyes all around you. You have a 30-foot aura for 1 minute or until you Dismiss it. You and your allies in the aura gain a +3 status bonus to damage with Strikes. Your enemies who end their turn within the aura can't reduce their frightened value below 1.

**Source:** `= this.source` (`= this.source-type`)
