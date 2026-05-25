---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Aldori Duelist|Aldori Duelist]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Aldori Duelist Dedication, you have broken or forsaken the Aldori swordpact"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are a swordlord exile. You have abandoned or been abandoned by the Aldori Academy. Aldori swordlords are honor-bound to challenge you on sight. Additionally, your unbridled skill strikes terror in those around you. You can use Dueling Lore instead of Intimidation to Coerce and Demoralize while your [[Aldori Dueling Sword]] is visible to the target of your attempt.

With broken pride, your blade is now a disgraced tool used to remove obstacles between you and your goals, whatever they may be. The first time you hit a creature with an Aldori dueling sword each round, you deal 5 additional precision damage.

**Special** You can't take both this feat and [[Aldori Swordlord]].

**Source:** `= this.source` (`= this.source-type`)
