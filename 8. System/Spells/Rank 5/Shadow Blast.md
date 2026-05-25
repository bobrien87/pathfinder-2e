---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Shadow]]"]
cast: "`pf2:2`"
range: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** varies

**Defense** [[Reflex]] save or [[Will]] save (target's choice)

You shape the shadow substance of the Netherworld into a blast. Choose @Damage[(@item.rank+1)d8[acid]|options:area-damage], @Damage[(@item.rank+1)d8[bludgeoning]|options:area-damage], @Damage[(@item.rank+1)d8[cold]|options:area-damage], @Damage[(@item.rank+1)d8[electricity]|options:area-damage], @Damage[(@item.rank+1)d8[fire]|options:area-damage], @Damage[(@item.rank+1)d8[force]|options:area-damage], @Damage[(@item.rank+1)d8[piercing]|options:area-damage], @Damage[(@item.rank+1)d8[slashing]|options:area-damage], @Damage[(@item.rank+1)d8[sonic]|options:area-damage], or @Damage[(@item.rank+1)d8[spirit]|options:area-damage] damage, and choose a @Template[cone|distance:30], a @Template[burst|distance:15] within 120 feet, or a @Template[line|distance:50]. The blast deals 6d8 damage of the type you chose to each creature in the area.

**Heightened (+1)** The damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
