---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
frequency: "once per round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Requirements** Your previous action was to Cast a non-cantrip Spell that dealt damage.

Your magic echoes ominously as you glimpse injury in the target's future. At the beginning of your target's next turn, it takes damage equal to twice the triggering spell's rank as a seemingly random and minor misfortune finds it. The damage and type of misfortune is of a type matching the spell; for instance, if you dealt fire damage, a flame might spontaneous ignite on them or they might burn a hand on their torch. The target is then temporarily immune to Foretell Harm for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
