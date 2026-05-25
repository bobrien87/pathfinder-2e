---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Animist]]", "[[Apparition]]", "[[Concentrate]]", "[[Spellshape]]"]
frequency: "once per round"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Requirements** You are attuned to at least 2 apparitions.

If your next action is to cast a cantrip or a spell that is at least 2 ranks lower than the highest-rank spell slot you have, you can draw power from one of your attuned apparitions to reduce the number of actions to cast it by 1 (minimum 1 action). The chosen apparition is dispersed until you can re-attune to it at your next daily preparations, but you can't disperse an apparition in this way if you would no longer be attuned to any apparitions afterward.

**Special** This can only be used on a cantrip or spell from the class matching the one you gained this feat from.

**Source:** `= this.source` (`= this.source-type`)
