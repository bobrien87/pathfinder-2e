---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[Auditory]]", "[[General]]", "[[Linguistic]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "master in Diplomacy, follower of a specific religion or philosophy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You point out a detail that incontrovertibly supports your faith, causing a listener's mind to whirl. Attempt a [[Diplomacy]] check and compare the result to the Will DC of a single target that can hear you and understands your language; that target is then temporarily immune to Evangelize with respect to your deity or philosophy for 1 day. A creature that already agrees with you is unaffected, and at the GM's discretion, a target that genuinely changes its perspective to support your faith as a result of the argument is also otherwise unaffected.
- **Critical Success** The target is [[Stupefied 2]] for 1 round.
- **Success** The target is [[Stupefied 1]] for 1 round.
- **Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
