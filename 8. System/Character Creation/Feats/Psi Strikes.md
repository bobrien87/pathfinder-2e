---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Mindshift]]", "[[Psychic]]"]
frequency: "once per turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per turn

**Requirements** Your most recent action was to Cast a Spell or to [[Unleash your Psyche]].

You siphon residual psychic energies from your spell into one weapon you're wielding or one of your unarmed attacks and when you unleash your mind, the energies flare to match. The attack deals an extra 1d6 force damage until the end of the current turn. If your Psyche is Unleashed, this benefit instead lasts until your psyche subsides.

**Source:** `= this.source` (`= this.source-type`)
