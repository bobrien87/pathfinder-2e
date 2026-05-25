---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Flourish]]", "[[Gunslinger]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Way of the Pistolero"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a stern call, carefully chosen barb, or some other challenging declaration, you demand your foe's attention in a duel. Choose an opponent within 30 feet who you can perceive and can hear you, and make your choice of a [[Deception]] check or [[Intimidation]] check against the target's Will DC. No matter the result of the check, the foe is temporarily immune to your Pistolero's Challenge until noon the next day.
- **Success** Both you and the opponent gain a +2 status bonus to damage rolls with Strikes made against each other. If you're a master in the skill you used for the check, the status bonus to damage rolls increases to +3, and if you're legendary, it increases to +4.

> [!danger] Effect: Pistolero's Challenge

You can have only one challenge in effect at a time; challenging a new opponent ends this effect on any current target. Otherwise, the effect lasts until one of you is defeated, flees, or the encounter ends.
- **Critical Failure** You become [[Frightened]] 1 and can't use this ability again for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
