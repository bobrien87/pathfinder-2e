---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "500 feet"
area: "10-foot cylinder"
defense: "basic Reflex"
duration: "10 minutes (sustained)"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) an empty 10-foot radius, 50-foot-tall cylinder

You conjure forth a massive tower with a large dragon that's bound to crawl its length. The dragon and the tower share the same space, and the dragon intercepts any attack targeting the tower. When the dragon dies, the tower crumbles. The dragon is immune to all conditions, has an AC of 40, a +30 modifier for all saving throws, and 250 Hit Points. When you Cast the Spell, and once per round when you Sustain it, the dragon unleashes its breath in a @Template[type:cone|distance:60], dealing 13d8 damage (basic Reflex save). The damage type depends on the tradition used to cast this spell: **arcane** force, **divine** spirit, **occult** mental, **primal** fire.

**Source:** `= this.source` (`= this.source-type`)
