---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Yaoguai]]"]
prerequisites: "Unleash Yaoguai Might"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your yaoguai form has reached its pinnacle, allowing you to assume (or perhaps, return to) the form of a monster of legend. You can [[Unleash Yaoguai Might]] any number of times per day.

Once per day when you Unleash Yaoguai Might, you can gain one of the following additional benefits, which persists for 1 minute or until you Change Shape again.

- Your body grows to impossible heights. Your [[Enlarge]] effect is heightened to 4th rank.
- Your spiritual power erupts to punish your enemies. You deal an additional 1d4 spirit damage with all Strikes and attack spells, and your Strikes and attack spells gain the spirit trait.
- You can leap off the air itself. You gain the effects of the [[Fly]] spell.

> [!danger] Effect: Legendary Monster

**Source:** `= this.source` (`= this.source-type`)
