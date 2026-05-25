---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Demolitionist|Demolitionist]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]"]
prerequisites: "Demolitionist Dedication, master in Engineering Lore"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know exactly how to make a memorable entrance... by detonating a bomb to produce a devastating explosion, of course! You Set Explosives on a door, window, container, or heavy gate. When the explosives detonate, you can attempt an Engineering Lore check to [[Force Open]] the target. If a bomb would add an item bonus to attack rolls, add that item bonus to your Engineering Lore check. Since you're blasting your way in, you can't avoid breaking the object or structure. If you roll a critical success, you get a success instead.

**Source:** `= this.source` (`= this.source-type`)
