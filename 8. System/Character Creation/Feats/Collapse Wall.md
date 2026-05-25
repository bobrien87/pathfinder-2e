---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Demolitionist|Demolitionist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Demolitionist Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature moves into the bombs' splash area.

**Requirements** You're within 30 feet of an area where you rigged bombs on a wall, cliff face, or similar vertical surface with [[Set Explosives]] or [[Demolition Charge]].

You detonate the required bombs in order to bring a wall down on a creature. If your bombs deal enough damage to reduce the wall's Hit Points below its Broken Threshold, the wall partially collapses on the creature. The creature takes bludgeoning damage equal to the damage dealt to the wall (basic Reflex save; the DC for this save is equal to your class DC or spell DC, whichever is higher). On a failure, they must spend an Interact action to dig themselves out of the collapse, and on a critical failure, they must spend 2 Interact actions to do so.

**Source:** `= this.source` (`= this.source-type`)
