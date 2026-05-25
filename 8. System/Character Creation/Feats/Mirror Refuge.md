---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Extradimensional]]", "[[Occult]]", "[[Reflection]]"]
prerequisites: "Mirror-Risen"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You're within 5 feet of a mirrored surface.

Your origin in the space behind mirrors enables you to use a mirror as a hideaway, like the spell [[One with Stone]]. You meld into an adjacent mirror. You can hear but not see outside this space, and creatures outside can't see or hear you. You can cast spells while within the mirror, but no effects can cross the mirror. Your Mirror Refuge lasts for 10 minutes unless the mirror is broken, which expels you and deals 10d6 damage to you. You can Dismiss the effect. You appear in a space adjacent to the mirror when the effect ends.

**Source:** `= this.source` (`= this.source-type`)
