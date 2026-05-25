---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Mortal Herald Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are granted access to your deity's realm and can travel there quickly. You can cast [[Interplanar Teleport]] once per day as an innate divine spell with a casting time of only 1 minute. You act as the planar key for the destination, and you can only travel to your deity's realm. You and the other targets of the spell always appear in the center of your deity's realm, and you (but not necessarily your allies) are immune to all the realm's harmful conditions (such as toxic air or extreme temperatures) while there. You can return to your previous location by spending 1 minute picturing your destination; you can bring up to 8 willing creatures back with you in this way, and they need not be the same targets of the previous casting of interplanar teleport.

**Source:** `= this.source` (`= this.source-type`)
