---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spellshot|Spellshot]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Spellshot Dedication"
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can aim your bullets not just in three normal dimensions, but in additional dimensions as well, removing all obstacles between you and your target. Attempt a crossbow or firearm Strike against a foe who's observed or [[Hidden]] to you (but not undetected). The ammunition travels to your target in a straight line, passing through any non-magical barriers or walls in its way, though magical barriers and force effects stop the bullet. The shot ignores all cover, the [[Concealed]] condition, the hidden condition, and circumstance bonuses to AC from shields. It has a +4 status bonus to hit creatures wearing any type of armor. The Strike's damage can't be reduced with a Shield Block reaction using a non-magical shield.

**Source:** `= this.source` (`= this.source-type`)
