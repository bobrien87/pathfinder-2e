---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Splinter Of Finality|Splinter Of Finality]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Manipulate]]", "[[Occult]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You wreathe yourself in the tatters of all the souls claimed by your blade. Until the start of your next turn, you gain resistance 10 to all damage except force, ghost touch, spirit, and vitality, doubled if the source of the damage is non-magical. If you slay a significant foe not immune to spirit damage with your [[Spectral Dagger]] while under this effect, its duration increases until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
