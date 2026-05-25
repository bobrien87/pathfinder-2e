---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fighter]]", "[[Press]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a single one-handed melee weapon and hold nothing else in your hands.

After your initial attack redirects your foe's defenses, your follow-up wrests their weapon from their grasp. Make a melee Strike with a one-handed melee weapon. In addition to its other effects, this Strike gains the success and critical success effects of the [[Disarm]] action. The Strike also has the following failure effect.
- **Failure** The target is [[Off Guard]] until the end of your current turn.

**Special** If you're in [[Disarming Stance]], you gain a +1 circumstance bonus to the attack roll.

**Source:** `= this.source` (`= this.source-type`)
