---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Animist]]", "[[Druid]]", "[[Magus]]", "[[Sorcerer]]", "[[Thaumaturge]]", "[[Witch]]", "[[Wizard]]"]
prerequisites: "a familiar"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Animist** You are able to materialize more of your attuned apparition's essence, creating a more powerful vessel for it to inhabit and aid you with.

**Druid** You infuse your familiar with additional primal energy, increasing its abilities.

**Magus** You infuse your familiar with more magical energy.

**Sorcerer, Wizard, Witch** You infuse your familiar with additional magical energy.

**Thaumaturge** By applying the best of multiple traditions of magic, you've found a more efficient way for your familiar to store its energy.

You can select four familiar or master abilities each day, instead of two.

**Special** Add the bonus familiar abilities you gain for being a witch to this amount. If your arcane thesis is [[Improved Familiar Attunement]], your familiar's base number of familiar abilities, before adding any extra abilities from the arcane thesis, is four.

**Source:** `= this.source` (`= this.source-type`)
