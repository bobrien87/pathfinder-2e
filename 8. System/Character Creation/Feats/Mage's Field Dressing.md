---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "War Mage Dedication, Battle Medicine"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your previous action was to Cast a Spell from a wizard spell slot, and the spell affected an ally within 60 feet.

As your spell takes hold on your ally, you use some of its magic to quickly dress their wounds. You use [[Battle Medicine]] on one ally affected by the required spell. You do not need to be holding or wearing a [[Healer's Toolkit]], as you conjure glowing threads, bandages, or similar supplies out of pure magic, which adds the arcane trait to Battle Medicine.

**Source:** `= this.source` (`= this.source-type`)
