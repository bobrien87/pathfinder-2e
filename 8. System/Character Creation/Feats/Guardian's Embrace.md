---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scions Of Domora|Scions Of Domora]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Scion of Domora Dedication"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are adjacent to your spirit guide or it is sharing your space.

Your spirit guide discorporates to surround you in an invisible protective shroud. You gain a +2 status bonus to AC against physical attacks until the beginning of your next turn. If you are hit by a physical attack during this time, you can use a reaction to gain resistance 10 to physical damage dealt by that attack; doing so ends the AC bonus, and you can't use Guardian's Embrace again for 10 minutes. Your spirit guide cannot be targeted by effects, cannot be affected by area effects, and cannot take any actions while this ability is active. Your spirit guide appears in a space adjacent to you when the effect ends.

**Source:** `= this.source` (`= this.source-type`)
