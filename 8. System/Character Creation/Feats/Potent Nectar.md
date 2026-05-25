---
type: feat
source-type: "Remaster"
level: "17"
prerequisites: "Caustic Nectar"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your nectar becomes particularly dangerous. Select one of the following benefits when you gain this feat. This choice is permanent and can't be changed.

- Your nectar is sticky, and clings to your target. Your nectar unarmed attack deals an additional 1d4 persistent acid damage to the target. This persistent damage isn't multiplied on a critical hit.

- Your nectar is shot at a high velocity, and splashes upon contact. Your nectar unarmed attack additionally deals 1d4 acid splash damage. This splash damage isn't multiplied on a critical hit.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
