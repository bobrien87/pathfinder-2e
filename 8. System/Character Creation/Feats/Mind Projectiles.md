---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mind Smith|Mind Smith]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Mind Smith Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned to stretch your mind's influence further, releasing projectiles with a swing of your mind weapon. You can make ranged mind weapon Strikes; these are ranged Strikes with a maximum range of 30 feet that 1d6 damage of the same type as your mind weapon. Your ranged mind weapon Strike gains all the benefits of your mind weapon's runes as long as they still apply to a ranged weapon. For example, if your weapon had *+1*, *striking*, and [[Spell Reservoir]] runes, you would get a +1 item bonus to hit with your ranged mind weapon Strike, and it would deal the additional damage from the striking rune, but it wouldn't be able to unleash a spell from the *spell reservoir* rune, as that rune can be etched onto only melee weapons.

**Source:** `= this.source` (`= this.source-type`)
