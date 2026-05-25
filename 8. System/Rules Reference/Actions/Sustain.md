---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Choose one of your effects that has a sustained duration or lists a special benefit when you Sustain it. Most such effects come from spells or magic item activations. If the effect has a sustained duration, its duration extends until the end of your next turn. (Sustaining more than once in the same turn doesn't extend the duration to subsequent turns.) If an ability can be sustained but doesn't list how long, it can be sustained up to 10 minutes.

An effect might list an additional benefit that occurs if you Sustain it, and this can even appear on effects that don't have a sustained duration. If the effect has both a special benefit and a sustained duration, your Sustain action extends the duration as well as having the special benefit.

If your Sustain action is disrupted, the ability ends.

**Source:** `= this.source` (`= this.source-type`)
