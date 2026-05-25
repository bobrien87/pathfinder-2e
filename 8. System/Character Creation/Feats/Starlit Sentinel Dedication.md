---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starlit Sentinel|Starlit Sentinel]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've been chosen by one of the constellations of the Tian Xia zodiac. You gain a transformation seal: a mundane-seeming item of light Bulk, such as a ring, brooch, or key, that has the arcane trait. If your seal is ever lost or destroyed, you can gain a replacement by spending 1 week of downtime in introspection to reconnect with your constellation. You, and only you, can transform into your sentinel form by Activating the seal.

[[Starlit Transformation]]

Starlit Sentinel

**Source:** `= this.source` (`= this.source-type`)
