---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Revelation]]"]
cast: "`pf2:2`"
duration: "10 minutes"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The elements grant you sensory enhancements. Choose one of the options below. The spell gains the listed trait or traits.

- **Aquatic Echolocation** (water) You use your hearing as a precise sense when underwater.

- **Heatsense** (fire) You can sense creatures with a temperature of 90º Fahrenheit or higher within 30 feet as an imprecise sense.

- **Magnetoreception** (metal) You can sense creatures carrying metal items with a total of 1 Bulk or greater; this is an imprecise sense with a range of 30 feet. If a creature is made of metal or has the metal trait, you can detect it as though magnetoreception were a precise sense. In addition, you continuously know which direction is north.

- **Mechanoreception** (air) You can see [[Invisible]] creatures and objects. They appear to you as translucent shapes, and they are [[Concealed]] to you.

- **Tremorsense**(earth) You gain tremorsense (imprecise) with a range of 30 feet.

- **Woodsense**(plant, wood) You can sense creatures carrying wood items with a total of 1 Bulk or greater; this is an imprecise sense with a range of 30 feet. If a creature is made of wood or has the plant or wood trait, you can detect it as though woodsense were a precise sense.

**Heightened (6th)** The duration increases to 8 hours, and you can take 1 minute to recalibrate the sense, switching from your current elemental sense to a different one.

**Source:** `= this.source` (`= this.source-type`)
