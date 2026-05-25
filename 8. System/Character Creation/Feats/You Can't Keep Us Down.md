---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Healing]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Seeing your allies falter, you fill their hearts with your unbreakable hope, rousing them to stay in the fight. All allies within 60 feet that are [[Dying]], or [[Unconscious]] and [[Wounded]], are healed a number of Hit Points equal to @Damage[(3*@actor.level)[healing]]{three times your level}. Then, all allies within 60 feet that are [[Prone]] may stand up as a free action that does not provoke reactions.

**Source:** `= this.source` (`= this.source-type`)
