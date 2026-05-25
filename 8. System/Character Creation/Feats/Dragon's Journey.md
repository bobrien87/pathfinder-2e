---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "14"
traits: ["[[Air]]", "[[Archetype]]", "[[Flourish]]", "[[Move]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding two fans, one in each hand.

Your movements are like that of a dragon weaving a serpentine path between your enemies and allies. Using your fans, you slice the air and create a path of least resistance, allowing you to move across the battlefield with an ethereal grace. You Stride, your movement doesn't trigger enemy reactions, and any allies you pass within 5 feet of can immediately use their reaction to Stride, moving in the same direction. Allies must end their movement as close as possible to you or another ally who benefited from this ability. During Dragon's Journey, ally movement doesn't trigger reactions.

**Source:** `= this.source` (`= this.source-type`)
