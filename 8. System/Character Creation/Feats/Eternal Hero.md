---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Heroic Scion Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You might be protected by divine intervention or the necessity of cosmic balance. You might be watched over by agents of destiny or fate. You could even be simply someone whose luck and skill have always worked together to ensure your triumph, no matter the odds you might face. Whatever the explanation, you're almost impossible to kill. You reduce the DC of recovery checks by 1 (this is cumulative with the reduction from the Heroic Scion Dedication feat). Whenever your doomed condition would increase to 4 or more, it doesn't increase. The first time each day you would be reduced to 0 Hit Points or outright killed by magical means, you instead remain at 1 Hit Point and become immune to all damage until the end of your next turn.

If you finally do die, you can spend a Mythic Point as a free action to immediately reincarnate—manifesting in a new body with the same statistics (save for potential changes to your ancestry and ancestry feats) within 15 feet of where your death occurred. Each time you repeat this reincarnation, the cost to do so increases by 1, so that after your third reincarnation, you can no longer swiftly return (as no mythic character can ever have more than 3 Mythic Points at one time).

**Source:** `= this.source` (`= this.source-type`)
