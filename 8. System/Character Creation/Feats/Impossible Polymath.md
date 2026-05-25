---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Bard]]"]
prerequisites: "trained in Arcana, Nature, or Religion, Esoteric Polymath"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your esoteric formulas are so unusual that they allow you to dabble in magic from diverse traditions that other bards don't understand. As long as you're trained in Arcana, you can add arcane spells to your book from [[Esoteric Polymath]]; as long as you're trained in Nature, you can add primal spells to your book; and as long as you are trained in Religion, you can add divine spells to your book.

Like your other spells in your book, you can add one of these spells from another tradition to your repertoire as an occult spell each day using Esoteric Polymath, but you can't retain any spells from another tradition when you prepare again, even if you have [[Eclectic Polymath]].

**Source:** `= this.source` (`= this.source-type`)
