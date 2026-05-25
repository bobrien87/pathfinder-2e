---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Mental]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You speak a bizarre koan that transcends language and is understood by only one creature within 30 feet. The target must attempt a [[Will]] save against your class DC. It's then immune to this ability for 1 hour.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stupefied 1]] for 1 round.
- **Failure** The target is stupefied 1 for 1d4 rounds.
- **Critical Failure** The target is stupefied 1 and [[Confused]] for 1d4 rounds.

**Source:** `= this.source` (`= this.source-type`)
