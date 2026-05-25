---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You breathe life into a mass of fiery critters. They swarm the target and create an aura around it in a @Template[emanation|distance:5]. The target and enemies in the aura are subject to an effect depending on the insects you choose. On subsequent rounds, the first time you Sustain this spell each round, you repeat the effect on the target and all your enemies in the insect aura. Pick a type of insect to determine the effects.

- **Fire Ants** You create fiery flying ants that deal 3d6 piercing damage plus 2d6 persistent fire damage with a basic Reflex save. A creature that fails its save must move 5 feet in a direction of your choice as it tries to escape the biting ants; this happens after all the creatures attempt their saves and can't add new creatures to the aura if the main target moves.

- **Fireflies** (incapacitation) You create a flurry of fireflies that deal 3d6 fire damage and can dazzle or blind, depending on the target's Fortitude save.
- **Critical Success** The creature takes no damage.
- **Success** The creature takes half damage and is [[Dazzled]] for 1 round.
- **Failure** The creature takes full damage and is [[Blinded]] for 1 round. It's then temporarily immune to being blinded by cinder swarm for 24 hours.
- **Critical Failure** As failure, but double damage and blinded for 1 minute.

**Heightened (+1)** Increase the ants' piercing damage and fireflies' fire damage by 2d6.

**Source:** `= this.source` (`= this.source-type`)
