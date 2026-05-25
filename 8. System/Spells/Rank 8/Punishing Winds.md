---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "100 feet"
area: "30-foot cylinder"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) 30-foot-radius, 100-foot-tall cylinder

Violent winds and a powerful downdraft fill the area, forming a cyclone. All flying creatures in the area descend 40 feet. The entire area is greater difficult terrain for Flying creatures, and difficult terrain for creatures on the ground or Climbing. Any creature that ends its turn Flying within the area descends 20 feet. Any creature pushed into a surface by this spell's winds takes bludgeoning damage as though it had fallen.

The squares at the outside vertical edges of the cylinder prevent creatures from leaving. These squares are greater difficult terrain, and a creature attempting to push through must succeed at an Athletics check or Acrobatics check to Maneuver in Flight against your spell DC to get through. A creature that fails ends its current action but can try again.

**Source:** `= this.source` (`= this.source-type`)
