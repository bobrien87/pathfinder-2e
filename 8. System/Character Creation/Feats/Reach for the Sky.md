---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pistol Phenom|Pistol Phenom]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Pistol Phenom Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a loaded firearm.

You command the room, firing a gun into the air and ordering everyone to surrender and put their hands in the air. You fire your firearm and then attempt a single Intimidation check to [[Demoralize]] each enemy within 30 feet. Creatures who become frightened instinctively put their hands in the air. If they had Raised a Shield, they lose the benefits, as they raise the shield above their head where it's of little use to block attacks. With their hands in the air, each of these frightened creatures can't use reactions or free actions that require their hands, or items held in their hands, until the beginning of their next turn. Regardless of the result, each creature is then temporarily immune to Reach for the Sky for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
