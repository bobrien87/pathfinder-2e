---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Kobold]]"]
prerequisites: "Benefactor's Strike, Dracomancer, or Kobold Breath"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your connection to your draconic benefactor becomes especially pronounced. You gain additional effects for the prerequisite kobold feat. If you have more than one of the prerequisite feats, you gain the appropriate additional effects.

- **Benefactor's Strike** Your unarmed strikes made with your jaws, claws, or tail gain the deadly d6 trait.
- **Dracomancer** Increase the number of times per day you can cast each of the granted 1st- and 2nd-rank innate spells by 1.
- **Kobold Breath** Creatures that critically fail their save against your Kobold Breath take 3d4 persistent damage of the type dealt by your draconic benefactor.

**Source:** `= this.source` (`= this.source-type`)
