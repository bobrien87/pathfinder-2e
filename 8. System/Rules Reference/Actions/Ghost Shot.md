---
type: action
source-type: "Remaster"
traits: ["[[Flourish]]", "[[Gunslinger]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Make a firearm or crossbow Strike. If you're [[Hidden]] from or [[Undetected]] by the target, the Strike adds the additional precision damage from [[One Shot, One Kill]]; if you would already receive that additional damage on the Strike, the effects aren't cumulative. If you were undetected or [[Unnoticed]] by any creatures, you're now hidden from them instead, or undetected if the shot was made with a silencer.

**Source:** `= this.source` (`= this.source-type`)
