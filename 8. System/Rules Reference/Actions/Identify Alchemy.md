---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're holding or wearing an [[Alchemist's Toolkit]].

You can identify the nature of an alchemical item with 10 minutes of testing using alchemist's toolkit. If your attempt is interrupted in any way, you must start over.
- **Success** You identify the item and the means of activating it.
- **Failure** You fail to identify the item but can try again.
- **Critical Failure** You misidentify the item as another item of the GM's choice.

**Source:** `= this.source` (`= this.source-type`)
