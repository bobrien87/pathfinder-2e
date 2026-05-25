---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ostilli Host|Ostilli Host]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Arcana or Nature"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** surki ancestry

You've bonded with an attached symbiote known as an ostilli. You can bond with only one ostilli at a time since the symbiote emits low-frequency magical pulses that repel other ostillis. You become trained in Ostilli Lore; if you were already trained, you become an expert.

The ostilli is a Tiny creature grafted to your body. Like other grafts, it has no Hit Points or Speeds of its own and can't be targeted separately. It can't be removed and dies when you do; in the event of your demise and resurrection, you can bond to a new ostilli during a week of downtime, though you lose any abilities granted by your ostilli bond during that time. Your ostilli is obvious, unless you attempt to cover it with clothing or armor. In such a case, an onlooker can determine you're bonded to an ostilli with a successful Nature, Perception, or Surki Lore check against your Deception DC. Your ostilli must be visible for you to use any of the actions it grants.

Your ostilli is constantly siphoning ambient magic from the surroundings, granting you the [[Repel Ambient Magic]] and [[Spit Ambient Magic]] actions.

Ostilli Host

**Source:** `= this.source` (`= this.source-type`)
