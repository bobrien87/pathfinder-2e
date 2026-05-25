---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Animist]]", "[[Apparition]]", "[[Spellshape]]"]
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Your apparition infuses your body with additional power. You regain one expended apparition spell slot that is at least 2 ranks lower than your highest-rank spell slot and takes 1, 2, or 3 actions to Cast. You then immediately cast an apparition spell that can be cast using that slot. The number of actions required for Apparition's Reflection is equal to the action cost of the spell cast. Maintaining control after such a surge is difficult, however; after casting the spell, you're [[Confused]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
