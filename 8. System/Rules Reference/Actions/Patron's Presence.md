---
type: action
source-type: "Remaster"
traits: ["[[Aura]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** A palpable weight extends from your familiar in a @Template[emanation|distance:15]. Enemies who enter or start their turn within the aura must succeed at a Will save against your spell DC or become [[Stupefied 2]] as long as they remain within the aura, or [[Stupefied 3]] on a critical failure. The aura lasts until the end of your next turn, but the familiar can Sustain it up to 1 minute.

**Source:** `= this.source` (`= this.source-type`)
