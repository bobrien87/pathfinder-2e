---
type: action
source-type: "Remaster"
traits: ["[[Illusion]]", "[[Psyche]]", "[[Psychic]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your flights of imagination spill into the real world, causing you to become indistinct, hazy, or cloaked in figments. You become [[Concealed]] until the start of your next turn. This concealment can't be used to [[Hide]], as normal for concealing effects that leave your location obvious.

**Source:** `= this.source` (`= this.source-type`)
