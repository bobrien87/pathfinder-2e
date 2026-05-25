---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Fungus]]", "[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "one creature or object"
defense: "basic Fortitude"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You unleash a sickly gray beam of toxic spores at your target. Make a spell attack against the target. If you hit a non-magical object that's made of organic material (such as a tree, wooden house, or massive skull), it melts away into a foul-smelling sludge. A single casting can destroy no more than a 10-foot cube of matter.

If you hit a creature, it takes 6d12 poison damage and 6d12 spirit damage with a basic Fortitude save. If you critically hit, the target gets a result one degree of success worse than the outcome of its Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage. Fungal tendrils swiftly digest the body and reduce it to sludge—the target takes 2d12 persistent,acid damage.
- **Critical Failure** As failure, but the target takes double damage, plus 4d12 persistent,acid damage.

**Heightened (+1)** The poison damage and spirit damage each increase by 1d12.

**Source:** `= this.source` (`= this.source-type`)
