---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
defense: "Will"
duration: "1 hour"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You implant a mental mine within your psyche that detonates against anyone attempting to magically manipulate your thoughts. You can Sustain the spell to suppress the effects of the mine for 1 round to allow someone to safely use a mental effect on you. You can Dismiss the spell. The first creature that uses a magical mental effect against you triggers the animus mine, causing the spell to end. The animus mine deals 4d8 mental damage to the triggering creature, which must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Stunned]] 1.
- **Critical Failure** The creature takes double damage and is stunned 1. You're unaffected by the triggering mental effect.

**Heightened (+1)** The damage increases by 2d8.

**Source:** `= this.source` (`= this.source-type`)
