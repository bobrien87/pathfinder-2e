---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Werecreature|Werecreature]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You were born into a lineage of true werecreatures or were afflicted with the curse of the werecreature.

You're a werecreature, able to shift between your humanoid shape, an animal shape, and a monstrous hybrid of the two. You gain the beast and werecreature traits. Choose your werecreature type.

Once chosen, this can't be changed. You gain the [[Toughness]] feat but also a weakness to silver equal to half your level. You gain the [[Change Shape]] action. On the night of the full moon, you automatically use Change Shape to assume your hybrid shape, and you can't voluntarily activate or dismiss Change Shape until sunrise.

Werecreature

**Special** If you're a beastkin, you can use unarmed attacks from your hybrid shape while you're in your werecreature hybrid shape. These forms are otherwise separate.

**Source:** `= this.source` (`= this.source-type`)
