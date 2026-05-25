---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[General]]", "[[Linguistic]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "trained in Diplomacy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You launch an insightful quip at a foe, distracting them. Choose a foe within 30 feet and roll a [[Diplomacy]] check against the target's Will DC.
- **Critical Success** The target is distracted and takes a –3 status penalty to Perception and Will saves for 1 minute.

The target can end the effect early with a retort to your Bon Mot. This can either be a single action that has the concentrate trait or an appropriate skill action to frame their retort. The GM determines which skill actions qualify, though they must take at least 1 action. Typically, the retort needs to use a linguistic Charisma-based skill action.
- **Success** As critical success, but the penalty is –2.
- **Critical Failure** Your quip is atrocious. You take the same penalty an enemy would take had you succeeded. This ends after 1 minute or if you issue another Bon Mot and succeed.

> [!danger] Effect: Bon Mot

**Source:** `= this.source` (`= this.source-type`)
