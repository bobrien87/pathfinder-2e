---
type: feat
source-type: "Remaster"
level: "5"
prerequisites: "ardande trait, plant trait, or wood trait"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature successfully Shoves or Trips you, or you fail a saving throw against an effect that would move you or knock you [[Prone]].

You react instinctively, sprouting roots from your legs and plunging them deep into the ground to keep your footing. If a force would move you, you move half that distance, to a minimum of 5 feet. If you would be knocked prone, resolve the effect, then you Stand.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
