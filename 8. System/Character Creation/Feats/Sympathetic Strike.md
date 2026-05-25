---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Witch]]"]
prerequisites: "Witch's Armaments"
frequency: "once per round"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

You collect your patron's magic into one of your witch armaments, causing them to shine with runes, light, or another signifier of your patron.

Make an unarmed Strike with one with your witch's armaments. If you hit, you establish a sympathetic link with the target, making it easier for your patron to affect them. Until the beginning of your next turn, the target takes a –1 circumstance penalty to its saves against your hexes, or a –2 penalty if the triggering Strike was a critical hit.

> [!danger] Effect: Sympathetic Strike

**Source:** `= this.source` (`= this.source-type`)
