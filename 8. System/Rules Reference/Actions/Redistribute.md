---
type: action
source-type: "Remaster"
traits: ["[[Eidolon]]"]
cast: "`pf2:r`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Trigger** An enemy's Strike against your eidolon is a critical hit.

Your eidolon rearranges its component bodies in response to a powerful blow, mitigating the worst of the damage they would have taken. The triggering critical hit becomes a hit. Your eidolon immediately switches forms, from condensed to dispersed or from dispersed to condensed.

**Source:** `= this.source` (`= this.source-type`)
