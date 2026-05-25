---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Splinter Of Finality|Splinter Of Finality]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Manipulate]]", "[[Occult]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your brush your fingers across your splinter of finality, momentarily creating a metaphysical vortex from which mortal spirits struggle to escape. For the next minute, incorporeal undead treat all squares within 30 feet of you as difficult terrain and living creatures within the same area die from the dying condition at dying 5 rather than dying 4.

As it comes close to tasting a living soul, the splinter of finality is empowered. If a living creature's dying value increases while within your Soul Well, your spectral dagger deals one additional weapon die of damage until the end of your next turn.

> [!danger] Effect: Soul Well (Additional Damage)

**Source:** `= this.source` (`= this.source-type`)
