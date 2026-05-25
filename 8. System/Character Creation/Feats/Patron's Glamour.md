---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Seneschal|Seneschal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Illusion]]"]
prerequisites: "Seneschal Witch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Gathering up threads of your old connection, you can temporarily disguise yourself as your missing patron. You gain [[Illusory Disguise]] as an innate spell of your patron's tradition, automatically heightened to the rank of your witch cantrips, but you can use it only to disguise yourself as the humanoid representation of your patron. Detection spells of lower rank than this *illusory disguise* give your patron's information rather than your own.

**Source:** `= this.source` (`= this.source-type`)
