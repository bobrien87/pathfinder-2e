---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Warshard Warrior Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a melee warshard weapon.

You hurl your warshard weapon at an opponent, even though the weapon isn't designed to be thrown. Spend a Mythic Point. Your weapon gains the thrown trait with a range increment of 40 feet; if your weapon already has the thrown trait, increase its range increment by 40 feet. Make a ranged Strike at mythic proficiency at an opponent within range. For this ranged Strike, apply your full Strength modifier to the damage, as if it were a melee Strike. After the Strike resolves, the weapon flies back to your hand, and you can then attempt a melee Strike (at your normal proficiency, not mythic proficiency) against a target in reach of your weapon. Both attacks count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both attacks.

**Source:** `= this.source` (`= this.source-type`)
