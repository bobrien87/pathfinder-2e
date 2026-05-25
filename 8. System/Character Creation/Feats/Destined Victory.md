---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Exemplar]]", "[[Ikon]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Usage** imbued into a worn ikon

You demand a battle against your chosen enemy. The imbued ikon gains the following abilities.

**Immanence** Whenever an enemy successfully Strikes you with a melee weapon, you gain a +2 status bonus to your AC against the next attack from that enemy before the start of your next turn.

**Transcendence—[[Only You and I]]** `pf2:1` (concentrate, transcendence)

@Embed[Compendium.pf2e.actionspf2e.Item.8r9ePG6BnrnO6YE1 inline]

**Source:** `= this.source` (`= this.source-type`)
