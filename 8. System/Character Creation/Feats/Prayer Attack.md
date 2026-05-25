---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Red Mantis Assassin|Red Mantis Assassin]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Red Mantis Assassin Dedication"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a sawtooth saber in each hand.

You've mastered the signature assassination style of the Red Mantis. Attempt to [[Feint]] an enemy within 30 feet. If your Feint is successful, when you use Prayer Attack on subsequent turns you automatically make the target [[Off Guard]] against your melee attacks for that turn without rolling a check to Feint, so long as you remain visible to the target and the target remains within 30 feet of you. If you use your Prayer Attack against a different target, you must attempt to Feint the target normally.

When you use Prayer Attack, your next successful Strike with a sawtooth saber that turn deals 2d6 persistent bleed damage to the target.

**Source:** `= this.source` (`= this.source-type`)
