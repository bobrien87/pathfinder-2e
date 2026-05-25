---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Yaoguai]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

As you enter your yaoguai form, you draw upon your internal magic to assume an even greater form. When you Change Shape to enter your yaoguai form, you can spend an additional action to gain the effects of [[Enlarge]] and an additional effect based on your heritage. This effect persists for 1 minute or until you Change Shape again.

- **Animal** Your hide thickens, granting a +1 circumstance bonus to AC.
- **Celestial** You recover some of your celestial perfection, granting you and all allies within 15 feet a +1 status bonus to attack rolls.
- **Elements** You're surrounded in wind and dust, granting concealment each round that you spend at least 1 action that has the move trait. You can't use this concealment to Hide or [[Sneak]], as normal for sources of obvious concealment.
- **Object** Your skin transmutes partially into an inorganic substance, granting resistance 5 to your choice of bludgeoning, piercing, or slashing.
- **Vegetation** You trigger an accelerated growth, gaining fast healing 5.

> [!danger] Effect: Unleash Yaoguai Might

**Source:** `= this.source` (`= this.source-type`)
