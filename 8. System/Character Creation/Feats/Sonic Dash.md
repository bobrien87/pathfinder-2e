---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You bounce up and down once, then sprint forward. You Stride twice in a straight line. You can use Sonic Dash while Burrowing, Climbing, Flying, or Swimming instead of Striding if you have the corresponding movement type.

**Awakening** Your Sonic Dash generates a sonic boom, dealing 1d4 sonic damage for every two levels you have (@Damage[floor(@actor.level/2)d4[sonic]|options:area-damage]) to all creatures other than you in a @Template[type:emanation|distance:5] at the point you end your Sonic Dash, with a [[Fortitude]] save. Creatures that fail are [[Deafened]] for 1 round, or 1 minute on a critical failure.

**Awakening** Your speed generates a slipstream that allows you to reposition your allies. You can dash through a willing ally's space during your Sonic Dash, causing them to be drawn by winds alongside you. You deposit them in any unoccupied space adjacent to you at the end of your Sonic Dash.

**Source:** `= this.source` (`= this.source-type`)
