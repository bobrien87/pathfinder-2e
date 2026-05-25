---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "14"
traits: ["[[Exploration]]", "[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

For many, the Calling of an ascended celestial is a wondrous but challenging path, which they must walk alone. This isn't the case for you. A single celestial is responsible for shepherding you into the celestial ranks and has offered to serve as a mentor to you throughout the time of your transformation. You can call upon this mentor for advice, guidance, and support. Once per day, you can spend 30 minutes in deep meditation. During this time, you spiritually converse with your celestial advisor. You gain three benefits during this conversation, which can occur in any order of your choosing.

You discuss a topic of interest with your celestial advisor. This allows you to Recall Knowledge on any topic once, with mythic proficiency. You can spend 1 Mythic Point to instead Recall Knowledge on any three topics with mythic proficiency.

You discuss a goal, activity, or event with your celestial advisor. This must be a goal you plan to achieve or an event you expect to happen within 1 week. Your celestial advisor gives you a piece of advice to help you achieve your goal or to see your way through the expected event. This has the effect of [[Read Omens]].

You discuss an immediate action that you intend to take with your celestial advisor. This must be an action you plan to take within the next 8 hours. Your celestial advisor gives you their opinion on the outcome. This has the effect of [[Augury]], except that the augury can see 8 hours into the future, and the GM doesn't roll a flat check for a failure.

**Source:** `= this.source` (`= this.source-type`)
