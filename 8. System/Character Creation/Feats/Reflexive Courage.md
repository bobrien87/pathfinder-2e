---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Bard]]", "[[Concentrate]]"]
prerequisites: "warrior muse"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature within your reach uses an auditory effect, manipulate action, or move action; makes a ranged attack; or leaves a square during its move action.

**Requirements** You are affected by [[Courageous Anthem]].

You bellow a ferocious call to arms, inspiring yourself to lash out at a foe. Make a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the action is disrupted.

**Source:** `= this.source` (`= this.source-type`)
