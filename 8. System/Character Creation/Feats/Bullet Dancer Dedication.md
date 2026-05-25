---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bullet Dancer|Bullet Dancer]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "expert in unarmored defense"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You mix guns and melee into a deadly art. You gain the Bullet Dancer Stance action. You are also granted familiarity with bayonets, reinforced stocks, martial firearms, and martial combination weapons; for the purposes of proficiency and abilities from this archetype, you treat bayonets, reinforced stocks, martial firearms, and martial combination weapons as simple weapons. You gain access to uncommon combination weapons that have a firearm ranged form.

**[[Bullet Dancer Stance]]** `pf2:1` (stance)

@Embed[Compendium.pf2e.actionspf2e.Item.SMF1hTWPHtmlS8Cd inline]

Bullet Dancer

**Source:** `= this.source` (`= this.source-type`)
