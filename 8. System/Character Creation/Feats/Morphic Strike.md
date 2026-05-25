---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Yaoguai]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can lash out with a portion of your previous self. You gain a melee unarmed Strike depending on your heritage, described below. You can use this unarmed Strike in either your humanoid form or your yaoguai form. These Strikes are in the brawling group. Like other unarmed attacks, you can improve this attack with handwraps of mighty blows.

- **Animal** `pf2:1` claw (agile, finesse), Damage 1d6 slashing
- **Celestial** `pf2:1` spirit touch (magical, sanctified, spirit), Damage 1d4 spirit
- **Elements** `pf2:1` elemental current (magical), Damage 1d4; this ability deals the same damage type and gains the same elemental traits of the cantrip you gained from your heritage
- **Object** `pf2:1` striking surface (sweep), Damage 1d8 bludgeoning or slashing (chosen when you gain this feat)
- **Vegetation** `pf2:1` root (reach), Damage 1d6 bludgeoning

**Source:** `= this.source` (`= this.source-type`)
