---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Gatewalkers Player's Guide (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shift your body into a higher gear, your speed compounding further and further. You gain a +10-foot status bonus to all your Speeds, which lasts until the end of your next turn. At any time during your next turn, you can use Unstable Gearshift again, increasing the status bonus by another 5 feet and prolonging the effect for another round. You can keep using Unstable Gearshift in this way until you can no longer use your deviant abilities.

**Awakening** When moving at high speed, your form blurs. You have concealment for the duration of any move action you take while you are affected by Unstable Gearshift.

**Awakening** Your high-speed form has become partially out of phase with reality. While you are affected by Unstable Gearshift, you are not affected by physical difficult terrain (such as rubble), you do not trigger traps that use weight or pressure plates as a trigger, and you can move through enemy spaces without making checks to [[Tumble Through]], as you simply phase through them.

**Source:** `= this.source` (`= this.source-type`)
