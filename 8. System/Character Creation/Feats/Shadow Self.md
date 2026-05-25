---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Halfling]]"]
prerequisites: "legendary Stealth"
frequency: "once per PT1H"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You successfully use Stealth to [[Hide]] and become [[Hidden]] from all your current foes, or use Stealth to [[Sneak]] and become undetected to all your current foes.

You slip from your adversaries' notice and appear to be somewhere else. You become [[Invisible]] for 1 minute or until you take a hostile action, whichever comes first. Choose a location within 10 feet of you. Until your invisibility ends, you appear to be hidden in that location to anyone trying to find you. If the searcher gets clear evidence that you're not there, they no longer think you're hidden there, but they don't discover your actual location.

**Source:** `= this.source` (`= this.source-type`)
