---
type: feat
source-type: "Remaster"
level: "1"
prerequisites: "trained in Hero-God Lore or Legendary Beast Lore"
frequency: "once per PT10M"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You successfully [[Recall Knowledge]] to identify a creature that has the mythic trait.

**Frequency** once per 10 minutes

Your ancestors confronted and bested mythic beasts of Iblydan antiquity. Through a combination of hearing these tales and channeling a hint of those warriors' mythic power, you've developed a knack for bypassing a mythic creature's fabled defenses. The next time you successfully Strike the triggering creature, your Strike treats its mythic resistance as 2 lower. You treat its resistance as 4 lower if your Hero-God Lore or Legendary Beast Lore proficiency rank is expert, 6 lower if your rank is master, and 8 lower if your rank is legendary.

If your Strike would already ignore mythic resistance (because you are a mythic character or wield a mythic weapon), your next successful Strike against the creature instead deals an additional 1d6 precision damage. This additional damage increases to 1d8 if your Hero-God Lore or Legendary Beast Lore proficiency rank is expert, 1d10 if your rank is master, or 1d12 if your rank is legendary.

**Source:** `= this.source` (`= this.source-type`)
