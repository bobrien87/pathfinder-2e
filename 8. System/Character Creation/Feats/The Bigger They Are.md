---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Bravado]]", "[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With reckless speed, you dash, jump and swing around a creature to find a more vulnerable spot. Attempt to `act tumble-through` a creature at least one size category larger than you, using the following effects.
- **Critical Success** You move through the enemy's space, treating the squares in its space as difficult terrain (every 5 feet costs 10 feet of movement). If you don't have enough Speed to move all the way through its space, you get the same effect as a failure. If you successfully pass through the target's square, the target gains weakness to your precision damage equal to half your level, which lasts until the end of your turn.
- **Success** As success, but the weakness applies only against the next attack you make against the target.
- **Failure** Your movement ends, and you trigger reactions as if you had moved out of the square you started in.
- **Critical Failure** As failure, and you fall [[Prone]].

> [!danger] Effect: The Bigger They Are

**Source:** `= this.source` (`= this.source-type`)
