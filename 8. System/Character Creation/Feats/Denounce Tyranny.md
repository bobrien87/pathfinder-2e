---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Steel Falcon|Steel Falcon]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Steel Falcon Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You witnessed a creature harm an ally, harm a noncombatant, or commit a wantonly evil act in the last round.

You call out a creature's despicable or cowardly actions, disrupting its alliances or even making its allies ashamed to be seen with it. Attempt a [[Diplomacy]] check and compare the result to the Will DCs of up to three of the triggering creature's allies within 30 feet of you. If you succeed on the check, the target refuses to treat the triggering creature as an ally for 1 round (2 rounds on a critical success). It's possible to get a different degree of success for each target. If you're a master in Diplomacy, you can instead target up to five creatures, and if you're legendary in Diplomacy, you can target up to 10 creatures.

**Source:** `= this.source` (`= this.source-type`)
