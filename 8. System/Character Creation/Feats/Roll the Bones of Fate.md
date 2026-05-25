---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]", "[[Prediction]]"]
prerequisites: "bones or lore mystery"
frequency: "once per PT10M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You roll a handful of bones to learn (or perhaps influence) the future course of events. Roll 1d4 and use the corresponding result below. Whenever you Roll the Bones of Fate, any effects from a previous usage immediately end.

**1 Good** You or an ally within 30 feet can roll twice on your next attack roll or skill check, taking the higher result. This is a fortune effect. 

> [!danger] Effect: Roll the Bones of Fate (Good)

**2 Bad** One creature you are observing within 30 feet must succeed at a Will save against your spell DC; on a failure, the target must roll twice on their next attack roll or skill check that takes at least one action to perform, taking the lower result. This is a misfortune effect.

**3 Mixed** You gain the benefits of rolling both a 1 and a 2.

**4 Cursed Possibilities** Your attempts to meddle in the forces of prophecy bring dire consequences for all. Every creature within 30 feet of you when you perform the augury rolls twice on their next attack roll or skill check that takes at least one action to perform; if the highest number rolled is odd, they take the lower result, and if the highest number rolled is even, they take the higher result. If they took the lower result, this effect has the misfortune trait for them, and if they took the higher result, it has the fortune trait.

**Source:** `= this.source` (`= this.source-type`)
