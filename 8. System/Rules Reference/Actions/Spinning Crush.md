---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:3`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wielding a loaded firearm or loaded crossbow.

You go into a vicious spin, smashing your weapon into those nearby and increasing your momentum by firing. All creatures adjacent to you take @Damage[(4d6+@actor.abilities.str.mod)[bludgeoning]|options:area-damage]{4d6 bludgeoning damage plus your Strength modifier}; this increases to @Damage[(6d6+@actor.abilities.str.mod)[bludgeoning]|options:area-damage]{6d6} if your firearm has a striking rune, @Damage[(8d6+@actor.abilities.str.mod)[bludgeoning]|options:area-damage]{8d6} if it has a greater striking rune, and @Damage[(10d6+@actor.abilities.str.mod)[bludgeoning]|options:area-damage]{10d6} if it has a major striking rune. This ability does not apply other effects that increase damage with your firearm Strikes such as weapon specialization. Creatures affected by this attack must attempt a [[Reflex]] save. A creature that fails its save is also pushed 10 feet directly away from you.

**Source:** `= this.source` (`= this.source-type`)
