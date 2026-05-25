---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Oatia Skysage|Oatia Skysage]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Occult]]"]
prerequisites: "Oatia Skysage Dedication, Night's Glow"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your power from the moon and stars becomes strong enough to illuminate the night sky. You gain your choice of the [[Asterism]] or [[Touch of the Moon]] domain spell.

**Special** You can take this feat a second time, gaining the focus spell that you didn't gain the first time.

**Source:** `= this.source` (`= this.source-type`)
