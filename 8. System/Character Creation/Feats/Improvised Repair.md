---
type: feat
source-type: "Remaster"
level: "3"
traits: ["[[General]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can hastily patch damaged equipment together, but the temporary fix lacks the full care required for lasting repairs. You patch together a broken item possessed by you or an adjacent willing creature. Until the item takes damage again, it still functions as a shoddy item of its type. If it's a magic item or another item with activations, it can't be activated while patched together, but can be used for normal functions (such as Striking with a weapon or using Shield Block with a shield). This activity restores no Hit Points, so the item is easy to destroy. Once the item is Repaired normally such that it is no longer broken, it is also no longer shoddy.

**Source:** `= this.source` (`= this.source-type`)
