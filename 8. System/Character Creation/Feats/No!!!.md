---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A non-minion ally within 60 feet is reduced to 0 Hit Points.

The shock of seeing your ally near death breaks whatever limits exist in your mind, sending your power spilling forth. If your psyche is currently unleashed, you can immediately use a psyche action that takes 1 action or less to use. If your psyche is not currently unleashed, you Unleash your Psyche, which remains unleashed until the end of your next turn. You can ignore Unleash Psyche's requirement of needing to have [[Cast a Spell]] on your previous turn, but you still can't Unleash your Psyche if you're stupefied or for 2 rounds after your psyche subsides.

**Source:** `= this.source` (`= this.source-type`)
