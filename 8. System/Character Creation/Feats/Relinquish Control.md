---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Apparition]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your turn begins.

Your apparition takes over and shields you from outside influence. Until the start of your next turn, you gain a +4 status bonus on saves against spells and effects that give you the [[Controlled]] condition or attempt to influence your actions (such as [[Charm]], [[Command]], or a nosoi's haunting melody). However, the only actions you can take are to [[Recall Knowledge]], Step, Strike, Cast an apparition Spell, Cast a vessel Spell, Sustain a vessel spell, or use an action that has the apparition trait. You gain a +2 circumstance bonus on all Recall Knowledge checks made using Lore skills granted by your attuned apparitions.

**Special** This feat requires a particularly strong bond with a specific apparition to learn. Choose one apparition you have access to; once you learn this feat, you must always choose that apparition as one of the apparitions you attune to each day.

**Source:** `= this.source` (`= this.source-type`)
