---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Animist]]", "[[Apparition]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would die.

Your attuned apparition gathers all of the energy it can through your shared bond and uses that power to disperse itself while channeling the energy back into you, saving your life. You can use Spirit's Sacrifice even while [[Unconscious]] or otherwise unable to act. Choose one apparition you have attuned; you do not die, your [[Wounded]] condition is reduced to 1 if it would be higher, and you regain a number of Hit Points equal to @Damage[(2*@actor.level)[healing]]{twice your level}. The chosen apparition is dispersed until you can re-attune to it at your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
