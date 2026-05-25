---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Captain|Captain]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Captain Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You accept anyone who would follow you on your adventures. You can take followers from any common ancestry, and from uncommon or rare ancestries at the GM's discretion. Your follower gains the traits, size, Speeds, languages, and other special abilities listed in their ancestry. For example, elf followers have the elf and humanoid traits, a 30-foot speed, low-light vision, and the typical languages for elves. Followers don't use their ancestry's Hit Points or attribute boosts and flaws. They also don't gain abilities that would allow them to use actions beyond the standard ones available to a follower, such as Activating an Item or Casting a Spell.

**Source:** `= this.source` (`= this.source-type`)
