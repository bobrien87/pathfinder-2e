---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Divine]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn a pact with devils, granting you success in life in exchange for your soul in the afterlife. Once per hour, when you critically fail a check, you can reroll the check as a free action; this is a fortune effect. Additionally, you can choose to automatically succeed at checks to [[Earn Income]] for tasks below your level, without rolling.

However, when you die, your soul is consigned to Hell. You can't be returned to life except by powerful magic such as the [[Wish]] ritual, and even then, the devils responsible for the contract can track your every move for 1 year. The devils gain the effects of a [[Pinpoint]] spell. They can also use 10th-rank [[Scrying]] on you at will, and you automatically critically fail your saving throw.

**Special** You can't retrain out of a Pact of Infernal Prowess without journeying to Hell and destroying the devil's written contract spelling out the terms of your pact.

**Source:** `= this.source` (`= this.source-type`)
