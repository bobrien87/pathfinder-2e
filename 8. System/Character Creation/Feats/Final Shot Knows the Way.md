---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]", "[[Press]]"]
prerequisites: "Warshard Warrior Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a ranged warshard weapon and used it to make a ranged Strike against a foe this round.

You judge a foe's defenses after attacking them and channel that knowledge into your warshard weapon and its ammunition. Spend a Mythic Point, then Stride twice. At any point during this movement, attempt a ranged Strike at mythic proficiency with your warshard weapon against the same foe you already attacked this round. This Strike ignores any modifiers from cover or concealment the target may have, as the ammunition weaves and twists through the air in an impossible flight. All penalties from range increments are negated during this Strike. If this shot hits its target, the target is so astounded by the shot that they become [[Off Guard]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
