---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Prophesied Monarch|Prophesied Monarch]]"
source-type: "Remaster"
level: "18"
traits: ["[[Auditory]]", "[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You declare your current foes as irredeemable enemies, calling your allies down upon them. Speak your decree; all your knights who hear your decree can use their reaction to Stride up to twice directly toward an enemy and then Strike that enemy if it's within their reach or range.

When you speak a Decree of War, you can spend a Mythic Point as part of the action to let every individual within a 10-mile radius around you at that moment know that war has come to your kingdom. You and your knights are able to gain access to free food, lodging, and repairs of common items while within the affected area for the next month, as allied citizens and creatures come to your aid. During this time, you also receive at least 10-minutes' warning whenever an enemy group of more than 10 creatures travels in your direction, as allied scouts report to you.

**Source:** `= this.source` (`= this.source-type`)
