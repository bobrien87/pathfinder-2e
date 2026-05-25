---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]"]
cast: "Passive"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You [[Craft]] a temporary item out of anything, anywhere, with whatever materials happen to be on hand, spending only 10 minutes to perform the initial Crafting check.

The temporary item must be one you've memorized or have the formula for, and must be common, non-magical, half your level or lower, and must be a weapon, armor, or a non-consumable piece of adventuring gear (non-consumable adventuring gear appears on page 291 of Player Core). Instead of a single item, you can create 10 pieces of a single type of ammunition. You can create only the physical item, not any information or magic, so for example, while you could create a blank journal or one with random pages, you couldn't use it as a scholarly journal or a religious text

**Source:** `= this.source` (`= this.source-type`)
