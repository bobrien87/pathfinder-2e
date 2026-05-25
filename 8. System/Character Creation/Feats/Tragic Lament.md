---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Shared Archetype Feats|Shared Archetype Feats]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Celebrity or Dandy, legendary in Performance"
frequency: "once per PT10M"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature you're aware of critically succeeds on a Strike against you and would deal damage to you.

**Frequency** once per 10 minutes

You dramatically cry out in poetic verse about the tragedies that led to your doom at this very moment, instilling guilt in your attacker. The Strike deals normal damage rather than critical damage as your foe relents on their attack at the last moment as they're moved by your words, though other effects that happen on a critical hit still occur. The creature that made the triggering Strike must then succeed on a [[Will]] save against your Class DC or be [[Slowed]] 1 for 1 round by guilt at its actions against you.

**Source:** `= this.source` (`= this.source-type`)
