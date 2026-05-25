---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Healing]]", "[[Vitality]]"]
prerequisites: "Living Vessel Dedication"
frequency: "once per PT1H"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You tap into the entity's life force to heal your wounds, though at the cost of the entity's personality bleeding into your own. You recover a number of @Damage[(4*@actor.level)[healing]]{Hit Points equal to four times your level}. Each time you use Tap Vitality, you begin to bleed more and more of the entity's personality and instincts into your own until the next time you spend an hour or more assuaging the entity, bringing your mind back under your own control.

**Special** This action has the tradition trait appropriate to your entity, typically divine for a demon, occult for an aberration or outer entity, or primal for a fey.

**Source:** `= this.source` (`= this.source-type`)
