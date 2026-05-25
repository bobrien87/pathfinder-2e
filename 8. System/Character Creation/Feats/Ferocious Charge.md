---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Beastmaster Dedication, animal companion with antlers, head, or horn unarmed attack"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've taught your companions to charge directly at an enemy. Your companions with a qualifying unarmed Strike learn the Ferocious Charge activity.

**Ferocious Charge** `pf2:2` The companion Strides up to twice its Speed in a straight line and makes an antlers, head, or horn Strike. If it moved at least 20 feet, it deals an additional 1d8 untyped damage. This damage increases to 2d8 if your companion is specialized. The companion can use Ferocious Charge while Burrowing, Climbing, Flying, or Swimming instead of Striding if it has the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
