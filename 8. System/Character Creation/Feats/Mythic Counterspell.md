---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Mythic]]"]
prerequisites: "Quick Recognition, ability to cast spells from spell slots, Sage's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature Casts a Spell, you've successfully Recognized the Spell, and you have either a prepared spell or an unexpended spell slot of equal or greater rank.

You quench and counter your enemy's magic with potent spellcraft amplified and enhanced by carefully deployed mythic power. Spend a Mythic Point, and expend a prepared spell or unexpended spell slot of the same rank as the triggering spell or higher. You lose your spell slot as if you'd cast the triggering spell. You then attempt to counteract the triggering spell using mythic proficiency to determine your spellcasting proficiency bonus for the counteract check.

**Source:** `= this.source` (`= this.source-type`)
