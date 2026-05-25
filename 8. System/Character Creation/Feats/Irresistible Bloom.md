---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Emotion]]", "[[Incapacitation]]", "[[Mental]]", "[[Olfactory]]", "[[Visual]]"]
prerequisites: "ardande trait, plant trait, or wood trait"
frequency: "once per day"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You bloom, sprouting flowers and releasing a pleasant smell, becoming irresistible. All creatures in a @Template[emanation|distance:30] must attempt a [[Will]] save with a DC equal to your Class DC or Spell DC, whichever is higher. On a failure, a creature becomes [[Fascinated]] with you, and must spend at least one of its actions on its next turn moving toward you. On a critical failure, you acting hostile to that creature allows them to attempt another save, rather than automatically ending the fascination.

These effects last until the beginning of your next turn. You can spend one action at the beginning of your turn to Sustain the effects for an additional round. You can Sustain it in this way for a maximum of 1 minute.

**Special** This feat gains the trait for your ancestry.

**Source:** `= this.source` (`= this.source-type`)
