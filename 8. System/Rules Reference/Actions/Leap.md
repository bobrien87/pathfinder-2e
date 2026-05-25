---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You take a short horizontal or vertical jump. Jumping a greater distance requires using the Athletics skill for a [[High Jump]] or [[Long Jump]].

- **Horizontal** Jump up to 10 feet horizontally if your Speed is at least 15 feet, or up to 15 feet horizontally if your speed is at least 30 feet. You land in the space where your Leap ends (meaning you can typically clear a 5-foot gap, or a 10-foot gap if your Speed is 30 feet or more). You can't make a horizontal Leap if your Speed is less than 15 feet.
- **Vertical** Jump up to 3 feet vertically and 5 feet horizontally onto an elevated surface.

**Source:** `= this.source` (`= this.source-type`)
