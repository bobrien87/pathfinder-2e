---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Basic mutagens that affect your physical form can bring out the beast within you, turn you nigh invincible, or make your body more elastic. While you're affected by one of the listed mutagens, you get an additional benefit.

- **Bestial Mutagen** You gain the mutagen's item bonus to your Intimidation checks. In addition, you increase the damage die size of your claws and jaws by one step, and they gain the deadly d10 trait.
- **Juggernaut Mutagen** You gain resistance to all physical damage equal to half your level.
- **Quicksilver Mutagen** You can stretch your legs and Step up to 10 feet, and you can squish and compress your body, allowing you to make it through tight spaces as if you were one size smaller, in addition to any effect from Squeezing.

**Special** If you can be under the effects of multiple mutagens (with the mutagenist greater field discovery, for example), you get all relevant benefits.

**Source:** `= this.source` (`= this.source-type`)
