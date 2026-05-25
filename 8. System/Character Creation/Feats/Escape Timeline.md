---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Chronoskimmer|Chronoskimmer]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Chronoskimmer Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** Your turn begins.

You step outside of the flow of time momentarily, allowing you to avoid dangers. Your physical form stops existing momentarily, and you can't be targeted or affected until the start of your next turn—you simply don't exist at that moment in time. Your turn ends immediately, advancing 1 round for all timed durations and effects, such as conditions and afflictions. You still attempt saving throws, flat checks, or any other checks at the end of your turn as normal, but you don't take any damage due to these checks (though you take any non-damaging effects as normal). At the start of your next turn, you reenter the flow of time and reappear in the same space where you left time last round. If the space isn't clear, you arrive in the nearest open space.

**Source:** `= this.source` (`= this.source-type`)
