---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Bravado]]", "[[Move]]", "[[Swashbuckler]]"]
prerequisites: "trained in Performance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are adjacent to an enemy.

You sweep your foe into your dance. Attempt a Performance check against an adjacent enemy's Will DC.
- **Critical Success** Your foe is swept up in your dance. You both move up to 10 feet in the same direction, remaining adjacent to one another. Your movement doesn't trigger reactions from the target (and the target's movement doesn't trigger reactions because it's forced movement).
- **Success** As critical success, but you both move only 5 feet.
- **Failure** The foe doesn't follow your steps. You can move 5 feet if you choose, but this movement triggers reactions normally.
- **Critical Failure** You stumble, falling [[Prone]] in your space.

**Source:** `= this.source` (`= this.source-type`)
