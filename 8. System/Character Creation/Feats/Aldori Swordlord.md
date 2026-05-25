---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Aldori Duelist|Aldori Duelist]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Aldori Duelist Dedication, you have taken the last name of Aldori, sworn to the Aldori swordpact, and demonstrated skill at swordplay by winning a duel using only a sword in the presence of an Aldori swordlord."
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are an Aldori swordlord. You can always obtain free room and board at the Aldori Academy for yourself and your allies.

You can use Dueling Lore instead of Diplomacy to Make an Impression or Request provided that the target you are Making an Impression on would be aware of the Aldori swordlords or your Request is related to your standing as a swordlord.

Whenever you successfully Strike a creature with an [[Aldori Dueling Sword]], you gain 5 temporary Hit Points (or 10 temporary Hit Point on a critical success) that last for 1 round.

> [!danger] Effect: Aldori Swordlord (Temporary Hit Points)

**Special** You can't take both this feat and [[Swordlord Exile]].

**Source:** `= this.source` (`= this.source-type`)
