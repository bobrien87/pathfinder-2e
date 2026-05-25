---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]", "[[Sanctified]]"]
prerequisites: "Godling Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** Your hierophant invoked your judgment on their previous turn

To prevent yourself from frivolously calling down the terrible power of divine wrath, you have vowed to do so only with the assent of your mortal hierophant. If your hierophant successfully Strikes a target, they can spend a single action to invoke your wrath. On your turn, you can then Pass Vengeful Judgment on the target, calling down a scouring pillar of divine energy that deals 20d10 spirit damage with a [[Fortitude]] save. You do not need to have line of effect to the target and it functions at any range. If one of your current domain spells can deal a type of damage other than spirit, you can choose to match this damage type (for instance, calling down a flaming pillar that deals fire damage if you have the fire domain).

If you spend a Mythic Point as part of Passing your Vengeful Judgment, the blast extends into the heavens, scattering the clouds in a detonation visible to all creatures within a 10-mile radius as a show of wrath and a warning to those who would dare harm your followers or question your commandments. For the next month, you and your hierophant gain a +2 status bonus to Intimidation checks against creatures in the area.

> [!danger] Effect: Pass Vengeful Judgment

**Special** If you have Font of Life or Death, you can choose for the damage type to be vitality (if you chose heal) or void (if you chose harm) when you use this ability.

*Note: A DC was not provided for this ability by Paizo. The button above uses the better of your class or spell DC.*

**Source:** `= this.source` (`= this.source-type`)
