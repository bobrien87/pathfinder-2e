---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vigilante|Vigilante]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Vigilante Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You establish a safe house-a secure space in which to hide your secrets from the outside world.

This safe house is roughly the size of two 10-foot cubes. It's in a location you have access to, and it can be part of a larger building or structure, like a hidden room or an underground cave.

The safe house protects objects and people inside it from magical detection. This has the effects of [[Veil of Privacy]], using your Deception modifier for the counteract DC and half your level rounded up for the counteract rank.

Setting up or moving your safe house takes a week of downtime.

The size of the safe house expands to four 10-foot cubes if you're an expert in Deception, eight cubes if you're a master, and 16 cubes if you're legendary.

**Source:** `= this.source` (`= this.source-type`)
