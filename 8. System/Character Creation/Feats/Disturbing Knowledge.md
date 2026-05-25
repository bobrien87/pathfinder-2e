---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Emotion]]", "[[Fear]]", "[[General]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "master in Occultism"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You utter a litany of dreadful names, prophecies, and descriptions of realms beyond mortal comprehension, drawn from your study of forbidden tomes and scrolls. Even those who don't understand your language are unsettled by these dire secrets.

Attempt an [[Occultism]] check and compare the result to the Will DC of an enemy within 30 feet, or to the Will DCs of any number of enemies within 30 feet if you are legendary in Occultism. Those creatures are temporarily immune for 24 hours.
- **Critical Success** The target becomes [[Confused]] for 1 round and [[Frightened]] 1.
- **Success** The target becomes frightened 1.
- **Failure** The target is unaffected.
- **Critical Failure** You get overly caught up in your own words and become frightened 1.

**Source:** `= this.source` (`= this.source-type`)
