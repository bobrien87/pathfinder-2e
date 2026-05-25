---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
traits: ["[[Consecration]]"]
cast: "8 hours"
range: "1-mile-radius circle centered on you"
duration: "see text"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the primal presence of the Fierani Forest and the elven legacy of Kyonin in an attempt to purify a portion of the blighted realm of Tanglebriar. Initially created by the elven wizard Aelthian in hopes of banishing Treerazer himself, this revision to that faulty ritual focuses instead upon the region he blighted rather than the nascent demon lord himself. Thus avoiding the catastrophic repercussions Aelthian experienced when he attempted to direct this magic against a foe too powerful to directly harm.

This version draws upon the ancient legacy of the forest itself by calling upon the remnants of primal spirits that remain locked away in Tanglebriar, bolstering them with elven magic. Successfully performing the ritual in an area in which Treerazer is currently located is more difficult, but the ritual's effects can weaken and distract him. If Treerazer is slain or banished, the effects of this ritual are longer lasting and less expensive—see "Cleansing Tanglebriar" on page 67 of this volume for more details.

*Purify Tanglebriar's* primary caster must succeed at a DC 41 check, while the secondary casters must succeed at a DC 36 check. If Treerazer is present in the ritual's targeted area, these checks increase to DC 43 for the primary caster and DC 38 for the secondary casters, but if the primary caster wears the Viridian Crown, all checks for the primary and secondary casters are reduced by 5.
- **Critical Success** The region within the area grows less blighted for 1 month (during which time additional purify Tanglebriar attempts in this area have no additional effect). Greater difficult terrain becomes difficult terrain; difficult terrain becomes regular terrain, and hazardous terrain becomes non-hazardous. All DCs to [[Sense Direction]], [[Subsist]], and to resist environmental afflictions in the area are reduced by 4. Creatures allied with Treerazer take a –2 status penalty to Initiative checks within this region. If Treerazer is in the area when the ritual is performed, the party gains 2 Torment points toward weakening the demon lord and 2 Triumph Points.

> [!danger] Effect: Spell Effect: Purify Tanglebriar
- **Success** As critical success, but for 1 week (during which time additional purify Tanglebriar attempts in this area have no additional effect). Creatures allied with Treerazer take no penalty to Initiative checks. If Treerazer is in the area when the ritual is performed, the party gains 1 Torment Point and 1 Triumph Point.
- **Failure** The region is unaffected.
- **Critical Failure** The region is unaffected, and the magic itself becomes corrupted and backfires on the casters. Each caster takes 20d6 void damage (DC 38 [[Fortitude]] save) as the purification energies sap away life itself. For 1 month, any attempt by that same primary caster to perform purify Tanglebriar increases its DCs by 5.

**Source:** `= this.source` (`= this.source-type`)
