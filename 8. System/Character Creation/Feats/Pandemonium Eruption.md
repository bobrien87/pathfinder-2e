---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Nephilim]]"]
prerequisites: "Proteankin"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You unleash the pent-up chaos within you, becoming a nexus of unbridled destruction that wreaks unfettered havoc on everyone in your vicinity. Each creature within @Template[emanation|distance:15]{15 feet} of you takes 14d6 @Damage[14d6[acid]|options:area-damage]{acid}, @Damage[14d6[electricity]|options:area-damage]{electricity}, or @Damage[14d6[sonic]|options:area-damage]{sonic} damage, chosen randomly for each target. Each target receives a [[Reflex]] save against the higher of your class DC or spell DC, but any creature that is subjected to the type of damage for which you currently have resistance through your Proteankin lineage takes a –2 penalty to the save. Any target that critically fails the save is also [[Confused]] until the end of their next turn.

**Source:** `= this.source` (`= this.source-type`)
