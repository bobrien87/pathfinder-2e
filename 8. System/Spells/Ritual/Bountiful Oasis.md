---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Water]]"]
cast: "1 day"
area: "10-foot burst"
duration: "1 year"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You redirect the flow of underground lakes and other nearby sources of water to cause a lush natural spring to emerge from the ground. The water of the spring is a clean source of fresh water, perfect for drinking, farming, and supporting all forms of life. The spring purifies itself every morning at dawn, removing toxins and contaminants unless they're more than double the spring's rank.

The ritual creates a spring that's geographically appropriate to the terrain where the ritual is performed; for example, it creates a desert oasis in sandy, arid regions and a natural hot spring in a mountain range.
- **Critical Success** A small pond or oasis appears, fed by a natural spring that discharges enough pure drinking water to sustain a small settlement. The ground in a @Template[burst|distance:20] surrounding the spring bursts with life, invigorated by the spring's irrigation. A variety of regionally appropriate, fruit-bearing plants and other crops immediately take root and prosper.
- **Success** As critical success, but the oasis is a small pool that discharges enough pure drinking water to sustain roughly a dozen people, without any plants growing around the perimeter.
- **Failure** You're unable to redirect the flow of the water.
- **Critical Failure** You create a small pond of fetid and stagnant water that never dries, attracting disease-carrying insects and sickening creatures who partake of its waters.

**Source:** `= this.source` (`= this.source-type`)
