---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warrior Of Legend|Warrior Of Legend]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Hero-God's Bond"
frequency: "once per day"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** Your bonded partner gains the dying condition or their dying value would increase.

A lost love. A broken spear. Rage burning through a hero-god. When a myth speaks of a wounded partner, the hero-god often rejects the future. Too many find themselves on a battlefield, clutching a body that they swore to protect. In that moment, the wellspring of power ignites.

Increase the value of your [[Doomed]] condition by 1, to a maximum of [[Doomed]] 3. You gain a +2 status bonus to attack rolls against any creature that attacked or dealt damage to your partner in the last minute. If you reduce a creature to 0 HP that attacked or damaged your partner, you gain temporary Hit Points equal to twice their level. These benefits last until your bonded partner is no longer [[Unconscious]] or for 1 minute, whichever duration is shorter.

**Source:** `= this.source` (`= this.source-type`)
