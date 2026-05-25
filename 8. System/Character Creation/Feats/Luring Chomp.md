---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Dragonet]]", "[[Mental]]", "[[Visual]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through your wiles, charm, or a little bit of magic, you lure in a foe for a closer look—and a quick bite! Choose a creature within 30 feet. It must attempt a [[Will]] save against your class DC or spell DC, whichever is higher.

If the target fails its save, you pull it up to 30 feet. If the target ends this movement in reach of your jaws, you can attempt a jaws Strike against it. Regardless of the result of its save, the target is temporarily immune for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
