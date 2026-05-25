---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Shared Archetype Feats|Shared Archetype Feats]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Celebrity or Gladiator Dedication"
frequency: "once per day"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're reduced to 0 Hit Points

**Frequency** once per day

In the world of drama, the finale of any performance doesn't have to be the end, and for you, this now extends to life itself. When damage reduces you to 0 Hit Points, you can use this reaction to suddenly spring back into action. Instead of gaining the dying condition and falling [[Unconscious]], you regain a number of Hit Points equal to @Damage[(10+@actor.level+@actor.system.abilities.con.mod)[healing]]{10 + your level + your Constitution modifier}.

**Source:** `= this.source` (`= this.source-type`)
