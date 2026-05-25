---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "10-foot burst"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

All things age, all things die, and at the end of days, even the universe will grow quiet and still. You awaken the cosmic principle of entropy, accelerating time in an area—flesh falters, plants shrivel, and even stone begins to crumble. Any creature that enters or begins its turn in the area takes 8d6 void damage with a basic Fortitude save, or 8d6 force damage if the creature normally doesn't take void damage, such as if the creature is a construct or undead. Even beings such as fiends with unlimited lifespans can be worn away by entropy.

The first time you Sustain the Spell on each subsequent turn, the entropic zone grows stronger in addition to having its duration increased. The radius of the burst increases by 10 feet (to a maximum of 40 feet), and the size of the damage dice increases by one step (from d6 to @Damage[(2+@item.rank)d8[void]|shortLabel], then to @Damage[(2+@item.rank)d10[void]|shortLabel], and finally to @Damage[(2+@item.rank)d12[void]|shortLabel]).

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
