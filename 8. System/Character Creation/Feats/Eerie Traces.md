---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Exploration]]", "[[Move]]", "[[Ranger]]"]
prerequisites: "trained in Intimidation, trained in Survival"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The tracks you leave behind are strange, somehow disconcerting and unnerving—they might travel backward, or through places no one would think to pass through. You change your tracks into eerie traces, moving up to half your travel speed as you do so. You don't need to attempt a Survival check to change your tracks, but anyone tracking you must attempt a Will save against the higher of your class DC or spell DC.
- **Success** The tracker is unaffected.
- **Failure** The tracker becomes [[Frightened]] 1 for as long as it follows your tracks. This condition doesn't decrease until the tracker stops following you, and it comes back if the tracker resumes following your tracks. If the tracker enters into an encounter with you after following your tracks, it begins the encounter frightened 1.
- **Critical Failure** As failure, but your disturbing traces cause the tracker to be [[Frightened]] 2 instead.

**Source:** `= this.source` (`= this.source-type`)
