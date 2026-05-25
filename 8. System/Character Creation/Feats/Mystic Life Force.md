---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Magic energy sustains you, supporting your form far beyond the capabilities of mere flesh. You can't die except due to old age as long as you're under the effects of an ongoing spell or within your [[Spellsurge]] aura; if your [[Dying]] or [[Doomed]] condition would increase to a high enough value to kill you, it doesn't increase, and any effect that would instantly kill you instead just reduces you to 0 Hit Points.

If you die for any reason, you transform into a magical font attached to an allied creature of your choice within 1 mile. This creature gains knowledge of the [[Embodied Font]] ritual to return you to your corporeal state. Until you're restored, once per hour, you can cast *spellsurge*, centered on the chosen creature. You still make all choices for the *spellsurge* and can take actions allowed by the spell, though you can take no other actions.

**Source:** `= this.source` (`= this.source-type`)
