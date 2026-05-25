---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Scrying]]"]
cast: "`pf2:2`"
range: "100 feet"
area: "20-foot burst"
targets: "1 creature or object tracked and up to 5 other willing creatures"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This spell grants perfect sight based on scrying, allowing several willing targets to track the exact movements or position of one creature or object. Choose one target creature or object in the area to be tracked. It becomes the sensor for the spell. Up to five willing creatures of your choice in the area can see a ghostly image of this creature or object when it's out of their sight. They can perceive the creature or object perfectly, allowing them to ignore the [[Concealed]] or [[Invisible]] condition, though physical barriers still provide cover.

The tracking creatures can see the tracked creature or object through all barriers other than lead or running water, which block their vision. Distance doesn't matter, though the creature or object might move so far away it becomes too small to perceive. The tracking creatures don't see any of the environment around the target, though they do see any gear a creature is wearing or holding, and they can tell if it removes objects from its person.

If the target to be tracked is willing, the duration is 1 hour. If you try to track an unwilling creature, the target must attempt a Will save.
- **Critical Success** The creature or object is unaffected.
- **Success** As described, and the duration is 1 minute.
- **Failure** As described, and the duration is 1 hour.

**Source:** `= this.source` (`= this.source-type`)
