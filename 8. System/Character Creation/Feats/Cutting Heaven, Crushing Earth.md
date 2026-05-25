---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Spirit Warrior|Spirit Warrior]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Spirit Warrior Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your skill in combining fist and blade has grown into a seamless art where each attack makes an opponent more vulnerable to the next. As long as you have invested and are wearing a set of handwraps of mighty blows, you also apply their runes to a single weapon you're wielding that can be used with your [[Overwhelming Combination]] ability. You gain the following benefits.

- When you successfully Strike an opponent with this weapon, it's [[Off Guard]] to the next Strike you make against it with a fist unarmed attack before the end of your next turn.
- When you successfully Strike an opponent with your fist unarmed attack, it's off-guard to the next Strike you make against it with a one-handed, agile, or finesse melee weapon before the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
