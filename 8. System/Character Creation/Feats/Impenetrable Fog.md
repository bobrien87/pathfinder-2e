---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Fog condenses in a chaotic, swirling pattern, thick enough that it seems to push back against you. You call forth a fog bank in a @Template[burst|distance:10] within 120 feet. All creatures in the fog are [[Concealed]], and all creatures outside the fog become concealed to creatures within it. The fog is so magically dense it impedes movement, making the area difficult terrain. The fog lasts until the end of your next turn, and you can Sustain the impulse up to 1 minute.

**Level (+3)** You can make the radius of the burst larger. Increase its maximum size by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
