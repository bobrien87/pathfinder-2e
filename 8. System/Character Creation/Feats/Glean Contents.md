---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Society"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are adept at quickly scanning loose papers and carefully discerning the contents of sealed letters without damaging the seal. You can attempt Society checks to Decipher Writing on a message that is only partially glimpsed, upside down or reversed from your perspective, and gain a +1 circumstance bonus to the check when doing so. You can also use this feat to decipher sealed letters, adding the manipulate trait to your attempt to Decipher Writing. This doesn't prevent witnesses from noticing your efforts; you might need to attempt Deception or Stealth checks to avoid being noticed. In either use of this feat, the recipient is made aware of your efforts on a critical failure (for instance, you might be caught rubbernecking or you might disturb the papers in a way their owner notices).

**Source:** `= this.source` (`= this.source-type`)
