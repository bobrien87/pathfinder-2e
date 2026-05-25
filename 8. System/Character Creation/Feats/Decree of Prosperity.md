---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You speak with a gentle encouragement that inspires confidence and competence in your followers. Speak your decree; all your knights who hear your decree treat failures (but not critical failures) on non-attack skill checks as successes for 1 minute.

When you speak a Decree of Prosperity, you can spend a Mythic Point as part of the action to have the inspiration spread to every individual within a 10-mile radius around you at that moment. Each individual receives a +2 status bonus to all checks to [[Earn Income]], and they're all able to find jobs of their level in the region for the next month. The people who benefit from this effect quickly learn that it happened because of your decree; for the next month, you can obtain food and lodging for free anywhere within the affected area, and you can obtain up to 10 common items of 3rd-level or lower at half price.

**Source:** `= this.source` (`= this.source-type`)
