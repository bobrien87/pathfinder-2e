---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lepidstadt Surgeon|Lepidstadt Surgeon]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Electricity]]", "[[Healing]]", "[[Manipulate]]"]
prerequisites: "Lepidstadt Surgeon Dedication"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** You're wearing or holding a [[Healer's Toolkit]].

"In lightning, there is life." This lesson is whispered throughout Lepidstadt, and you can put it to practical use. You have integrated a miniature Stasian coil into your healer's toolkit. You use the coil to gently shock a willing or [[Unconscious]] ally within your reach, who gains 2d4 temporary Hit Points from the jolt. These temporary Hit Points last for 1 minute. These temporary Hit Points increase by 1d4 at 8th level and every 4 levels thereafter.

> [!danger] Effect: In Lightning, Life

A creature that has resistance or immunity to electricity is immune to this ability, and a creature that received temporary Hit Points from In Lightning, Life is temporarily immune to it for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
