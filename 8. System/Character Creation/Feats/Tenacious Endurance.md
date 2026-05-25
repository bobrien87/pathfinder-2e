---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Beastmaster Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You encourage your companion to refuse to yield, against even the mightiest of foes. When one of your animal companions is reduced to 0 Hit Points, if it isn't wounded, it can remain standing with 1 Hit Point and become [[Wounded]] 1.

**Source:** `= this.source` (`= this.source-type`)
