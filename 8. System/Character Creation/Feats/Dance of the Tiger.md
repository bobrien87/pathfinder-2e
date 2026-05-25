---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Occult]]", "[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Tales tell of the Tiger stalking the Mousedeer for days, hidden and instilling dread upon its prey. Your dance embodies the character role so well you can trail an opponent from its own shadow. Attempt a Performance check against the Will DC of a single adjacent enemy.
- **Critical Success** You step on the foe's shadow, bringing a cold dread. The opponent is [[Frightened]] 2; its shadow remains pinned underfoot, stretching and deforming to remain connected to your square, and indicates where it has gone even if you lose sight of the foe. The creature can't reduce its frightened condition below 1 as long as you remain on its shadow. Your connection to its shadow breaks if the distance between you and the target exceeds 120 feet or if you don't end your turn adjacent to the target. Once your connection to its shadow breaks, the enemy is immune to Dance of the Tiger for 1 hour.
- **Success** As critical success, except the creature is only [[Frightened]] 1 and your connection to its shadow breaks at 60 feet instead of 120.

**Source:** `= this.source` (`= this.source-type`)
