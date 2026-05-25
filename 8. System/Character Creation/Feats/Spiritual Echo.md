---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Occult]]", "[[Sarangay]]"]
prerequisites: "Awakened Jewel"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You possess the head gem of a deceased ancestor or loved one, which has begun to resonate with your own. While you possess this gem, you gain the ability to Cast a Spell as a 4th-rank occult innate spell once per day. The type of spell is determined by the clan of the sarangay to whom the head gem belonged, which you choose when you take this feat. In addition, choose a Lore skill to represent knowledge the deceased had. You become trained in that Lore skill. If the gem is lost or destroyed, it can be regrown as if it were your own head gem.

- **Full Moon** [[Spirit Sense]]
- **Half Moon** [[Status]]
- **New Moon** [[Darkness]]
- **Waning Moon** [[Creation]]
- **Waxing Moon** [[Blood Vendetta]]

**Source:** `= this.source` (`= this.source-type`)
