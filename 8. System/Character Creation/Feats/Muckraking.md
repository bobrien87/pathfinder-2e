---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Venture Gossip|Venture Gossip]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Venture-Gossip Dedication"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It seems like your knowledge has come in handy after all and you have your enemy at your feet. Pulling out your fan mail, you read your fans' scathing remarks about your enemy to their face, letting them feel just how much everyone hates them and everything that they've done. They hate the way that they walk, they hate the way that they talk.

Your enemy takes 10d10 mental damage, with a [[Will]] save. On a critical failure, they're [[Off Guard]] until the beginning of your next turn and lose all reactions, except to cry, loudly.

**Source:** `= this.source` (`= this.source-type`)
