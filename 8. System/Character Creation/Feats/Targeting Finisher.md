---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Finisher]]", "[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attack harms and hinders your foe. Choose a particular part of your foe from the list below and Strike.

If you hit and damage the target, apply the effect corresponding to the chosen part. This hindrance lasts until the end of your next turn. On a critical hit, you also apply a lesser effect lasting for 1 minute.

- **Arm (or another limb used for attacks, such as a tentacle)** The target is [[Enfeebled]] 2. On a critical hit, it is also [[Enfeebled]] 1 for 1 minute.
- **Head** The target is [[Stupefied 2]]. On a critical hit, it is also [[Stupefied 1]] for 1 minute.
- **Legs** The target takes a –10-foot status penalty to its Speeds. On a critical hit, it also takes a –5-foot status penalty to its Speeds for 1 minute.

> [!danger] Effect: Targeting Finisher

**Source:** `= this.source` (`= this.source-type`)
