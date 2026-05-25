---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fire]]", "[[Healing]]", "[[Mythic]]"]
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You regain Hit Points while you are [[Unconscious]].

When you escape death, you return to life with retributive fire that burns those who harmed you. You expend 1 Mythic Point, return to consciousness, Stand, and regain additional Hit Points equal to your level. You then erupt in flames, dealing fire damage equal to twice your level (@Damage[(2*@actor.level)[fire]]) to adjacent foes, with a [[Reflex]] save against your class DC. Foes that critically fail the save are also pushed 5 feet away from you.

**Source:** `= this.source` (`= this.source-type`)
