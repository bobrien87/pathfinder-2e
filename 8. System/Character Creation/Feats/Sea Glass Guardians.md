---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Eerily beautiful elemental water beings race around you, eager to protect and heal you and your allies. Their forms vary and might include eels formed of undulating water or ice crystals whirling in the shape of a jellyfish. The guardians flow around combatants and don't occupy a space. They attempt to intercept all dangers, granting you and your allies within your kinetic aura a +1 status bonus to AC and saving throws.

If any creature affected is critically hit or critically fails at a saving throw against an attack, effect from an enemy, or hazard and remains above 0 HP, the guardians reach out to heal that creature. The creature regains @Damage[((floor((max(12,@actor.level)-12)/3)+4)d8+(floor((max(12,@actor.level)-12)/3)*4+8))[healing]] HP, and the impulse ends. If the creature is in water, the healing dice are d10s instead of d8s.

> [!danger] Effect: Stance: Sea Glass Guardians

**Level (+3)** The healing increases by 1d8+4.

**Source:** `= this.source` (`= this.source-type`)
