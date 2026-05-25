---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Rogue]]"]
prerequisites: "legendary in Deception, Perfect Distraction"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would be hit by an attack or targeted by an effect, or you are within an effect's area.

**Requirements** You have [[Perfect Distraction]] ready to use.

You reactively switch with your decoy to foil your foe. You use Perfect Distraction, even if you were observed, as long as you end the movement of your [[Sneak]] while [[Concealed]] or in a location with cover or greater cover. Your decoy is targeted by the attack or effect instead of you. In the case of an area effect, if your Sneak doesn't move you out of the area, both you and the decoy are targeted by the effect.

**Source:** `= this.source` (`= this.source-type`)
