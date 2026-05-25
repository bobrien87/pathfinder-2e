---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Morph]]", "[[Primal]]", "[[Yaksha]]"]
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

Pulling your hair loose into flames and gnashing your teeth into ragged fangs, you howl a vow of ire, and your form surges to meet the demands of your deadly promise. For the next minute, you gain two unarmed attacks. You gain a tusks melee unarmed attack that deals 1d6 piercing damage, is in the brawling group, and has the finesse and unarmed traits. You also gain a flame-hair melee unarmed attack that deals 1d4 fire damage, is in the brawling group, and has the agile, finesse, and unarmed traits.

**Source:** `= this.source` (`= this.source-type`)
