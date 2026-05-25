---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Basic mutagens that affect your mind and thoughts can make you communicate telepathically, protect you from being detected, or let you communicate with anyone. While you're affected by one of the listed mutagens, you get an additional benefit.

- **Cognitive Mutagen** You also gain the mutagen's item bonus to Deception, Diplomacy, Intimidation, Medicine, Nature, Performance, Religion, and Survival checks. In addition, you can communicate telepathically with creatures within 60 feet with whom you share a language. The communication is two-way once you establish it, so a creature you contact can also communicate with you.
- **Serene Mutagen** Detection, revelation, and scrying effects of 9th rank (or 17th level) or lower detect nothing from you or your possessions and auras. For instance, detect magic would still detect other magic in the area, but not any magic on you.
- **Silvertongue Mutagen** Ignore circumstance penalties you would take to Deception, Diplomacy, Intimidation, and Performance checks. In addition, your words transcend linguistic barriers; everyone listening to you speak hears your words as if you were speaking in their own language (though you don't actually speak that language, nor does this ability allow you to understand any additional languages).

**Special** If you can be under the effects of multiple mutagens (with the mutagenist greater field discovery, for example), you get all relevant benefits.

**Source:** `= this.source` (`= this.source-type`)
