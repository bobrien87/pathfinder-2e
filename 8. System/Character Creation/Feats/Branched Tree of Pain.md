---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a weapon ikon that deals piercing or slashing damage

The blade of your ikon takes one or more notches, capable of dealing mortal pain to your foes.

**Immanence** When you Strike with the ikon, you critically succeed if you roll a 19 on the die as long as that result would be a success. This has no effect on a 19 if the result would be a failure.

**Transcendence—[[Plant Thirty Barbs]]** `pf2:1` (death, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.cfQb0mBbyrjhyGf5 inline]

**Source:** `= this.source` (`= this.source-type`)
