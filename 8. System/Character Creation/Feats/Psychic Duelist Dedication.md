---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Psychic Duelist|Psychic Duelist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Occultism, you have been in a psychic duel"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through experience and in-depth visualizations of mental battles, you've grown adept at psychic duels. You gain a +2 circumstance bonus to your initiative rolls for psychic duels. Each time you enter a psychic duel, choose one of the following benefits for the duration of that duel.

- **Mind Mace** You gain a status bonus to mental damage with spells you cast equal to the spell's rank.
- **Psychic Fist** You can use your standard attribute modifier for Strike damage instead of your highest mental modifier, and you can use your full AC instead of using your Will DC in place of your AC.

Psychic Duelist

**Source:** `= this.source` (`= this.source-type`)
