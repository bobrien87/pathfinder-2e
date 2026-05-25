---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Plant]]", "[[Primal]]"]
prerequisites: "ardande trait, plant trait, or wood trait"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You grow a simple tool from your own body, coaxing flowers, vines, roots, and wood to grow and sprout from your flesh into the desired shape. You create a one level 0 common simple tool with no intricate parts or written text, such as a crowbar, rope, or shovel. You can't replicate a tool kit or weapon with this ability. This item lasts for 1 minute, or until you create another tool with this ability, whichever comes first. When duration runs out, the item crumbles to mulch.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
