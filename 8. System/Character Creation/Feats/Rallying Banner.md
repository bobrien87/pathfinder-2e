---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Brandish]]", "[[Commander]]", "[[Emotion]]", "[[Healing]]", "[[Mental]]", "[[Visual]]"]
frequency: "once per PT10M"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

Your banner waves high, reminding your allies that the fight can still be won. You restore @Damage[(max(4,(4 + floor((@actor.level - 8)/2))))d6[healing]] Hit Points to each ally within the aura of your commander's banner. This healing increases by an additional 1d6 at 10th level and every 2 levels thereafter.

Since this healing relies on drawing from your allies' morale and adrenaline, the healing it grants is halved when used outside of combat.

**Source:** `= this.source` (`= this.source-type`)
