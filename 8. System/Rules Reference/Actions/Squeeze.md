---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Move]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You contort yourself to squeeze through a space so small you can barely fit through. This action is for exceptionally small spaces; many tight spaces are difficult terrain that you can move through more quickly and without a check.
- **Critical Success** You squeeze through the tight space in 1 minute per 10 feet of squeezing.
- **Success** You squeeze through in 1 minute per 5 feet.
- **Critical Failure** You become stuck in the tight space. While you're stuck, you can spend 1 minute attempting another Acrobatics check at the same DC. Any result on that check other than a critical failure causes you to become unstuck.

Sample Squeeze Tasks- **Trained** space barely fitting your shoulders
- **Master** space barely fitting your head

**Source:** `= this.source` (`= this.source-type`)
