---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Changeling]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through your heritage, you can replicate a hag's magic. Choose one common spell of 4th rank or lower from those available to a coven, including the spells contributed to a coven by a hag of your mother's type. You can cast this spell once per day as a 4th-rank occult innate spell.

Spells available to all covens are [[Augury]], [[Charm]], [[Clairaudience]], [[Clairvoyance]], [[Dream Message]], and [[Illusory Disguise]]. The eligible spells granted by the most prominent types of hag are:

**Cuckoo Hag** [[Nightmare]], [[Spellwrack]]

**Iron Hag** [[Earthbind]], [[Spellwrack]]

**Sea Hag** [[Humanoid Form]], [[Mariner's Curse]], [[Water Walk]]

**Sweet Hag** [[Charm]], [[Honeyed Words]], [[Outcast's Curse]]

**Source:** `= this.source` (`= this.source-type`)
