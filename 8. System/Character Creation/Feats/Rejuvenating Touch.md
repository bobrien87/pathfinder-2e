---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Champion]]"]
prerequisites: "lay on hands"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your healing energies linger after you cast, providing continual benefits. An ally that recovers Hit Points from your [[Lay on Hands]] gains 10 temporary Hit Points immediately and at the start of their turn during each of the next 10 rounds. These temporary HP last until the start of the creature's next turn. This effect ends if the ally is knocked [[Unconscious]].

> [!danger] Effect: Rejuvenating Touch

**Source:** `= this.source` (`= this.source-type`)
