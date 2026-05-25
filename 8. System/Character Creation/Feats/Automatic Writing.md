---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[General]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "expert in Occultism"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day When confronted with the unknown, you can receive knowledge beyond your own experience via written messages delivered by your hand. You spend 10 minutes seated while holding a writing utensil, using it to make small circular motions as you open your mind to the forces around you. You receive information as your hand writes on its own, guided by spirits. At the end of these 10 minutes, [[Recall Knowledge]] with any Lore skill in which you are not trained, using your Occultism modifier instead of your modifier with that skill. The strain of this spirit channeling leaves you [[Stupefied 1]] for the next 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
