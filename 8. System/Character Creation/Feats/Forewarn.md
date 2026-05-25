---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Overwatch|Overwatch]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Overwatch Dedication, master in Perception"
frequency: "once per PT1M"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

**Trigger** An enemy within your overwatch field attempts an attack against an ally who is also within your overwatch field.

Your foresight and planning are more valuable than armor as you direct your ally away from danger, but there's a limit to how often you can guide your allies away from a foe's relentless assaults. The triggering attack roll targets your Perception DC instead of your ally's AC. Though this allows your ally to avoid taking penalties to their AC, it doesn't remove any conditions or other effects causing such penalties. For example, an enemy with sneak attack would still deal extra damage to your ally if they are [[Off Guard]], even though they wouldn't take the –2 circumstance penalty when defending against the attack.

**Source:** `= this.source` (`= this.source-type`)
