---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Magical]]"]
cast: "`pf2:2`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You circulate magic through your wings, causing them to vibrate at high speeds such that their scraping produces disruptive sounds. You focus the sound at one creature within 30 feet who must succeed at a [[Fortitude]] save against your class DC or spell DC (whichever is higher) or become [[Sickened]] 1, or [[Sickened]] 2 on a critical failure, as the vibrations disrupt its inner equilibrium. You can Sustain the effect for up to 1 minute; the creature can't recover from the sickened condition as long as you continue your song and it can hear you.

**Source:** `= this.source` (`= this.source-type`)
