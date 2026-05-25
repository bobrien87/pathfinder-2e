---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Curse]]", "[[Druid]]", "[[Linguistic]]", "[[Manipulate]]", "[[Primal]]", "[[Ranger]]"]
prerequisites: "expert in Occultism, expert in Survival"
frequency: "once per PT1H"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Requirements** You must be in either natural terrain or in abandoned or relatively unused artificial terrain (such as a darkened alley or haunted house).

You know there are places in the world that are just wrong—places where the birds don't sing and where you always feel like you're being watched. You can spot these places, and you can awaken them. To do so, you must gesture toward a 10-foot by 10-foot square you can see and make an ominous proclamation of some manner (i.e. "This is cursed ground," "That is an ill-omened place."). The next creature that enters the marked territory must attempt a Will save against your spell DC (if you're a druid) or class DC (if you're a ranger).
- **Success** The target is unaffected.
- **Failure** Something goes horribly awry for the victim in the cursed ground. The details are up to the GM—it can be a purely "natural" accident (they step into an old bear trap, perhaps) or something stranger and more spectral. The target gains a condition for 2 rounds. Roll 1d4 on the table and use the failure column to determine which condition.
- **Critical Failure** As failure, but the effect is astonishingly gruesome. Use the critical failure column, and the condition lasts for 1 minute.

d4FailureCritical Failure1[[Clumsy]] 2[[Clumsy]] 32[[Enfeebled]] 2[[Enfeebled]] 33[[Stupefied 2]][[Stupefied 3]]4[[Dazzled]][[Blinded]] for 1 round, then [[Dazzled]]

**Source:** `= this.source` (`= this.source-type`)
