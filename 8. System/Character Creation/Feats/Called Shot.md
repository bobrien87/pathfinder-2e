---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Flourish]]", "[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You target a specific area of your foe's anatomy to debilitating effect. Declare a part of your foe's anatomy to target and make a ranged weapon Strike. If you hit and deal damage, the target takes one of the following effects, based on the body part you targeted. The GM should use the stated effects as a guideline when attacking creatures with stranger anatomy-for instance, applying the "arms" effect to a creature's tentacles if those are what the creature uses to attack.

- **Arms** The target is [[Enfeebled]] 2 until the end of your next turn. On a critical hit, it's also [[Enfeebled]] 1 for 1 minute.
- **Head** The target is [[Stupefied 2]] until the end of your next turn. On a critical hit, it's also [[Stupefied 1]] for 1 minute.
- **Legs** The target takes a –10-foot status penalty to its Speeds until the end of your next turn. On a critical hit, it also takes a –5-foot penalty to its Speeds for 1 minute.
- **Wings** If the target is flying using its wings, it immediately falls 20 feet, or 40 feet on a critical hit. The fall is gradual enough that if the target hits the ground, it takes no damage from the fall.

> [!danger] Effect: Called Shot

**Source:** `= this.source` (`= this.source-type`)
