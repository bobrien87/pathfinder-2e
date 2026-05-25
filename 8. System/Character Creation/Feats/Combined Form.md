---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Polymorph]]", "[[Tanuki]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet uses a polymorph effect.

Cooperation and coordination are the secrets to getting by in tanuki society. When the triggering ally transforms, you Stride to their square and join shape with them, melding into their transformation. While you're melded in this way, you grant them the effects of either a 2nd- or 4th-rank enlarge spell as well as temporary Hit Points equal to your level; if their polymorph effect would normally grant them temporary Hit Points, you increase the amount by your level instead. While you're melded, you can't be separately targeted and you can't act except to speak or to use Change Shape to exit the Combined Form, which ends the effects of enlarge on your ally and removes any remaining temporary Hit Points they received from this ability at the time. If the triggering ally becomes [[Unconscious]] or the triggering polymorph effect ends, you automatically exit the Combined Form.

**Source:** `= this.source` (`= this.source-type`)
