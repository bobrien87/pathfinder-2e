---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mind Smith|Mind Smith]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Magical]]", "[[Mental]]"]
prerequisites: "Mind Smith Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a swing and a thought, you detonate your mind weapon into a burst of psychic shards that shred the mind. You concentrate and unleash a @Template[cone|distance:15] that deals @Damage[(ceil(@actor.level/2)d6)[mental]|options:area-damage] damage to all creatures in the area, with a [[Will]] save against the higher of your class DC or spell DC. After the attack, your mind weapon automatically re-forms, and you can't use this ability again for 1 minute. Mind Shards' damage increases by 1d6 at level 7 and every two levels thereafter.

**Source:** `= this.source` (`= this.source-type`)
