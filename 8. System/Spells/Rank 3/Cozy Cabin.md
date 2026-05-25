---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Wood]]"]
cast: "1 minute"
range: "30 feet"
duration: "12 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shape a cabin 20 feet on each side and 10 feet high. This cabin has the structure trait and the same restrictions as magic items that create structures. The walls of the hut are simple and wooden, with small, square glass windows, and it has one wooden door. It doesn't include its own lock, but it has a fastener to which a lock can be applied.

The interior contains three cots, one chamber pot, and a small fireplace holding a magical fire. The interior is lit with a small magical light that you can light or extinguish at will using a Sustain action. The climate inside the hut is comfortable and allows creatures inside it to withstand most hostile weather conditions, but incredible heat or cold, powerful storms, and winds of hurricane force or greater destroy the hut. Other creatures can freely enter and exit the hut without damaging it, but if you exit the hut, the spell ends. You can Dismiss the spell.

**Source:** `= this.source` (`= this.source-type`)
