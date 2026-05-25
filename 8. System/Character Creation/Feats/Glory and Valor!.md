---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Divine]]", "[[Healing]]", "[[Nephilim]]"]
prerequisites: "Battleblooded"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You call upon your ascendant blood with a mighty cry that fills you with a revitalizing energy for 1 minute or until you critically fail a Strike, whichever comes first. For the duration, the first time each round you successfully Strike a creature of your level or higher, you regain @Damage[(floor(@actor.level/2))[healing]]{Hit Points equal to half your level}.

**Source:** `= this.source` (`= this.source-type`)
