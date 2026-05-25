---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Archetype]]", "[[Aura]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a fan.

As you spin and glide your fans alongside your allies, you kick up a mild wind that gently carries you all forward. So long as you're holding a fan, you and allies who start their turn in a 30- foot aura emanating around you gain a +5-foot circumstance bonus to land Speed for 1 round; you also gain this bonus to your fly Speed if you possess one, but it can't grant you the ability to fly if you wouldn't otherwise be able to.

> [!danger] Effect: Pushing Wind

Additionally, the air impedes the movements of your foes. While holding a fan, the area in a 10-foot aura emanating around you is difficult terrain for all enemies.

**Source:** `= this.source` (`= this.source-type`)
