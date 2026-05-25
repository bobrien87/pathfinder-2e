---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lion Blade|Lion Blade]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Lion Blade Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You quietly speak or recall coded phrases and metaphors whose meanings inspire you to complete your mission. You gain a +1 status bonus to one skill of your choice until the beginning of your next turn. You can Sustain this effect for up to 1 minute. If you're an expert in Performance, the bonus increases to +2. If you're a master in Performance, the bonus is +3, and if you're legendary, the bonus is +4.

**Source:** `= this.source` (`= this.source-type`)
