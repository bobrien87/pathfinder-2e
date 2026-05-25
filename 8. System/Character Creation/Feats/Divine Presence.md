---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Divine]]", "[[Stance]]"]
prerequisites: "Mortal Herald Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spirit becomes one with your deity, granting you the bearing of a god. As long as you are in this stance, you have a 5-foot emanation that has the aura trait. Whenever you take an action, you can take it from your space or any space within the emanation as if it were the space you occupy. An enemy that ends its turn completely within the emanation is [[Off Guard]] to your Strikes. You can Sustain the emanation to increase its radius by 5 feet, up to a maximum of 15 feet.

**Source:** `= this.source` (`= this.source-type`)
