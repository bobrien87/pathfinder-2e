---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "10-foot burst"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You orchestrate an invisible ensemble of lost sounds captured inside errant breezes across the Plane of Air, and you can direct this symphony to attack foes within range. The sounds materialize and manifest as directed, appearing as silhouetted instruments and musicians that dance and bob in the wind.

When you Cast the Spell, a captured breath of ephemeral music explodes in a great crescendo, appearing in a space you choose within range. On subsequent rounds, the first time you Sustain the Spell each round, you can move your conjured melody to a space within range (if needed) and create another explosion of music.

Each explosion of sound from the *phantom orchestra* deals 8d6 sonic damage to all creatures in a 10-foot burst (basic Fortitude save). The *phantom orchestra* doesn't take up space, grant flanking, or have any other attributes a creature would.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
