---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonet]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your scales are hard as armor, ensuring you always have some protection in the dangerous world. When you're unarmored, your scales give you a +1 item bonus to AC with a Dexterity cap of +3. The item bonus increases to +2 at 5th level. The item bonus to AC from these scales is cumulative with armor potency runes on your [[Explorer's Clothing]], the [[Mystic Armor]] spell, or [[Bands of Force]].

**Source:** `= this.source` (`= this.source-type`)
