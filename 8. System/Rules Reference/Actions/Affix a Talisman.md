---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Manipulate]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You must use a [[Repair Toolkit]]

You spend 10 minutes affixing a talisman to an item, placing the item on a stable surface and using the repair toolkit with both hands. You can also use this activity to remove a talisman. Attaching more than one talisman to an item deactivates all the talismans. They must be removed and re-affixed before they can be used again.

**Source:** `= this.source` (`= this.source-type`)
