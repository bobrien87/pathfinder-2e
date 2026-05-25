---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Pistol Phenom Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're possessed with an incredibly vivacious spark that separates you not only from ordinary gun users and gunslingers, but even from other phenoms. Using that distinctive verve, when you perform impeccably and control the scene with your abilities, you also manage to set up your foes for disaster and ensure they remain in your sights for any follow-up attacks you want to make against them. If you critically succeed at a Performance check for [[Pistol Twirl]] or a pistol phenom archetype feat, you gain a +1 status bonus to your attack rolls with one-handed firearms and one-handed melee weapons until the end of your turn.

> [!danger] Effect: Phenom Verve

**Source:** `= this.source` (`= this.source-type`)
