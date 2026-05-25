---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've become a champion of the runelords of sloth. They spur you toward idleness, and their spirits are slow to come to your aid. Once they arrive, however, their combined might is undeniable. The first time each day you spend 10 minutes resting, you gain 1 Mythic Point. During this time, you don't need to sleep, but you can't perform activities like Refocus or [[Treat Wounds]]. You gain the [[Summon Sloth]] activity.

**Source:** `= this.source` (`= this.source-type`)
