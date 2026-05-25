---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You were born with a layer of scales across your entire body that resemble those of your draconic progenitor. When you're unarmored, the scales give you a +1 item bonus to AC with a Dexterity cap of +3. The item bonus to AC increases to +2 at 5th level. The item bonus to AC from these scales is cumulative with armor potency runes on your explorer's clothing, the [[Mystic Armor]] spell, or [[Bands of Force]].

**Special** You can select this feat only at 1st level, and you can't retrain into or out of this feat.

**Source:** `= this.source` (`= this.source-type`)
