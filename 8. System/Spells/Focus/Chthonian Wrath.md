---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:2`"
area: "60-foot cone"
defense: "basic Reflex"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You evoke the energy of a part of the Outer Rifts. The damage types of the spell (one energy and one physical) are based on the result of rolling on the table below. You deal 4d6 damage of each of the corresponding damage types to each creature in the cone (8d6 total damage).

**Heightened (+1)** The damage for each type increases by 1d6

Chthonian Wrath`r 1D4`RealmManifestationDamage and type1SkiesBolts and lightning and flying debrisBludgeoning and electricity2DepthsAcid and demonic shellsAcid and slashing3FrozenFrigid air and iceBludgeoning and cold4VolcanicJagged volcanic rocks and magmaFire and piercing

**Source:** `= this.source` (`= this.source-type`)
