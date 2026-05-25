---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Mythic]]"]
cast: "`pf2:1`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Spend a Mythic Point. You regain Hit Points equal to your Constitution modifier (minimum 1) × your level and remove the [[Fatigued]] condition. If you're suffering from any recurring affliction such as poison or disease, attempt a saving throw against the affliction at mythic proficiency to see if you reduce the affliction's stage. This saving throw cannot increase your affliction's stage, nor does it change the affliction's maximum duration.

**Source:** `= this.source` (`= this.source-type`)
