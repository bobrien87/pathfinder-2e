---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You pluck a single thread from your ikon, which ties itself in three loops about your wrist, where it remains for the next minute. If you fail an attack roll or skill check, and a +1 status bonus would change your failure into a success or your success into a critical success, you gain a +1 status bonus to this check retroactively, changing the outcome appropriately as the thread pulls you to the future you desire. The thread then falls from your wrist. You can have only one thread in existence at a time.

**Source:** `= this.source` (`= this.source-type`)
