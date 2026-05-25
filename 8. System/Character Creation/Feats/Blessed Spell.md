---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Blessed One|Blessed One]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Blessed One Dedication, ability to cast spells from spell slots, Mercy"
frequency: "once per PT10M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

When you focus your magic on an ally, you can remove harmful conditions.

If your next action is to [[Cast a Spell]] from a spell slot, and that spell targets only a single ally, you can also attempt to remove a harmful condition from that ally. The condition must be one that could be removed by your Mercy feat, including those granted by later feats such as [[Greater Mercy]].

Attempt a counteract check based on the spell's DC and level. This effect is in addition to the normal effects of your spell.

**Source:** `= this.source` (`= this.source-type`)
