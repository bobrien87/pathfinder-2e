---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Red Mantis Assassin|Red Mantis Assassin]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Healing]]", "[[Magical]]"]
prerequisites: "Red Mantis Assassin Dedication"
frequency: "once per day"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You swathe yourself in a veil of red mist for 1 minute. While the shroud is active, you gain fast healing equal to half your level. You can Interact with your shroud, swirling it around you, to gain a +1 circumstance bonus to AC until the beginning of your next turn. Finally, if you die while the shroud is active, you can choose to have your entire body vanish into red mist, leaving behind only your gear; you make this choice when you activate Crimson Shroud.

At 10th level, you can use this ability once per hour instead of once per day.

**Source:** `= this.source` (`= this.source-type`)
