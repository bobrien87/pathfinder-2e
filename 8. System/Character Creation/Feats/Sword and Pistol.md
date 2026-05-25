---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're comfortable wielding a firearm or crossbow in one hand and a melee weapon in the other, combining melee attacks with shots from the firearm. When you make a successful ranged Strike against an enemy within your reach with your one-handed firearm or one-handed crossbow, that enemy is [[Off Guard]] against your next melee attack with a one-handed melee weapon.

When you make a successful melee Strike against an enemy with your one-handed melee weapon, the next ranged Strike you make against that enemy with a one-handed firearm or one-handed crossbow doesn't trigger reactions that would trigger on a ranged attack but not a melee attack, such as Reactive Strike. Either of these benefits is lost if not used by the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
