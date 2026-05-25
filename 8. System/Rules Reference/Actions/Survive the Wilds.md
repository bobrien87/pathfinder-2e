---
type: action
source-type: "Remaster"
traits: ["[[Aura]]", "[[Manipulate]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You wrap the pelt around yourself. You can choose to change the damage type the pelt is attuned to. The pelt shines gold, drawing the offending energies into itself.

Until the start of your next turn, this shine creates an aura in a @Template[type:emanation|distance:15]. You and all allies in the emanation gain a +2 circumstance bonus to AC and saving throws against effects with that trait.

**Source:** `= this.source` (`= this.source-type`)
