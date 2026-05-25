---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mythic]]", "[[Void]]"]
prerequisites: "Apocalypse Rider Dedication"
frequency: "once per PT10M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You hasten the passage of time for a living creature, prematurely aging them into decrepitude. A living creature within 60 feet takes 14d6 void damage and a part of its body you chose withers, taking the following penalties depending on the result of their a [[Fortitude]] save saving throw against your class DC or spell DC, whichever is higher.

- **Arms** The target's arms grow weak. The target becomes [[Enfeebled]] 1.
- **Head** The target has trouble thinking straight. The target becomes [[Stupefied 1]].
- **Legs** The target's legs buckle with every movement. The target takes a –10-foot status penalty to its Speeds.
- **Torso** The target's skin becomes thin and papery. The target gains weakness 10 to slashing damage.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and the withering penalty lasts until the end of your next turn.
- **Failure** The creature takes full damage and the withering penalty lasts for 1 minute.
- **Critical Failure** The creature takes double damage, and you can choose a second part of the body to wither. Both penalties last for 1 minute.

> [!danger] Effect: Wither Away

**Source:** `= this.source` (`= this.source-type`)
