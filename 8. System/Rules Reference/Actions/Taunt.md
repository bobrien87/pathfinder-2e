---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Guardian]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

With an attention-grabbing gesture, noise, cutting remark, or threatening shout, you attempt to draw an enemy to you instead of your allies. Taunt gains the auditory trait, visual trait, or both, depending on how you draw the target's attention. Even mindless creatures are drawn to your taunts. Choose an enemy within 30 feet to be your taunted enemy. If your taunted enemy takes a hostile action that includes at least one of your allies but doesn't include you, they take a –1 circumstance penalty to their attack rolls and DCs for that action, and they also become [[Off Guard]] until the start of their next turn.

Your enemy remains taunted until the start of your next turn, and you can have only one Taunt in effect at a time. Taunting a new enemy ends this effect on any current target.

> [!danger] Effect: Taunt

**Source:** `= this.source` (`= this.source-type`)
