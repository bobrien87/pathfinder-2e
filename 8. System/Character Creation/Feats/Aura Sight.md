---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[General]]", "[[Secret]]", "[[Skill]]"]
prerequisites: "expert in Occultism"
frequency: "once per PT1H"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You've learned how to read the natural auras of other living creatures. To do this, you must focus on a single living target without blinking for 1 minute. You can do this while performing some other minor task—such as making conversation to distract from your intentions—but you can't blink or otherwise lose your concentration. You can then perceive any or all of the following information.

- The target's current apparent attitude toward you (friendly, indifferent, and so on).
- The target's current apparent emotional state.
- A general assessment of the target's physical health, such as what conditions or afflictions it has. You might need to succeed at an Occultism check against the affliction or condition's DC to detect the presence of a specifically hidden or subtle condition or affliction.

In addition, the GM rolls a secret [[Occultism]] check for you against the target's Deception DC. If your result exceeds your target's, you can identify if they're being deceptive in some way (such as expressing a false attitude toward you or faking an emotional state). This doesn't allow you to automatically identify the exact nature of that deception, only to tell the outward appearance is false.

**Source:** `= this.source` (`= this.source-type`)
