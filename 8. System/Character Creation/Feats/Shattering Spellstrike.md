---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Force]]", "[[Magus]]"]
prerequisites: "resurgent maelstrom hybrid study, Spellstrike"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in Arcane Cascade stance and wielding an improvised weapon.

You intentionally channel a rampaging cascade of magic through your weapon, breaking it to deal more damage. Make a Spellstrike against a target with your improvised weapon. If the attack hits, it deals an additional 2d6 force damage as your improvised weapon breaks. If the spell used with the Spellstrike wasn't a cantrip or focus spell, increase this additional damage by the spell's rank.

If the item has a Hardness greater than your level, or if it's an artifact, cursed item, or other item that's difficult to break or destroy, it doesn't break and you don't deal additional damage.

**Source:** `= this.source` (`= this.source-type`)
