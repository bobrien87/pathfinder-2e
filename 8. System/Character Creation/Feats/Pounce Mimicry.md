---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Wild Mimic Dedication, you have seen a creature use an ability that lets them Stride and Strike as a single action (such as Pounce) or have identified a creature with such an ability in combat"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're unarmored or wearing light armor.

You have mastered the art of stalking your prey and striking when they are most vulnerable. You Stride and then Strike. If you began this action [[Hidden]], you remain hidden until after the Strike. You can use Pounce Mimicry while Burrowing, Climbing, Flying, or Swimming instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
