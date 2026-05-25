---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Manipulate]]", "[[Poison]]"]
prerequisites: "Living Vessel Dedication, your entity is a demon"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Most of the changes from the demon within you have harmed you so far, but you've found a way to expel some of the corruption within you to poison others. Until the beginning of your next turn, you and your weapons are covered in toxic sludge or another similar manifestation of the demonic corruption; your melee Strikes deal an additional 1d6 poison damage, and each time a creature hits you with a melee unarmed attack or otherwise touches you, it takes 1d6 poison damage.

At 14th level, the poison damage increases to 2d6, and at 20th level, the poison damage increases to 3d6.

**Source:** `= this.source` (`= this.source-type`)
