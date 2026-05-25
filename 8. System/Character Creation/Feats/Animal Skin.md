---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Barbarian]]", "[[Morph]]", "[[Primal]]"]
prerequisites: "Animal Instinct"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your proficiency in unarmored defense increases to expert. When you are raging and unarmored, your skin transforms into a thick hide. You gain a +2 item bonus to AC (+3 if you have the [[Greater Juggernaut]] class feature). The thickness of your hide gives you a Dexterity modifier cap to your AC of +3. This item bonus to AC is cumulative with Armor Potency runes on your explorer's clothing, [[Mystic Armor]], and [[Bands of Force]].

**Source:** `= this.source` (`= this.source-type`)
