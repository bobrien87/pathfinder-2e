---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Invoker|Rivethun Invoker]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Rivethun Invoker Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Requirements** You're under the effects of Enter Spirit Trance.

The spirits you've invoked throughout your life have left behind echoes and spiritual fragments, which you can manifest across your own flesh, temporarily transforming you into something more akin to spirit than mortal. For 1 minute, you gain fast healing 5 and you become [[Concealed]]. You can't use this concealment to Hide. Your Strikes gain the benefits of a ghost touch property rune. Whenever you deal damage with a Strike, you can choose to have that Strike deal spirit damage, rather than its usual damage type.

If you would be knocked [[Unconscious]] or your dying value would increase while One with the Spirits is active, the spirits revive you at the beginning of your next turn, restoring you to 30 Hit Points. One with the Spirits then immediately ends.

**Source:** `= this.source` (`= this.source-type`)
