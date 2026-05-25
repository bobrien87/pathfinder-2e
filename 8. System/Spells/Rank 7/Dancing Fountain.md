---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:3`"
area: "30-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 30-foot burst centered on you

Tapping the ground, you create a shallow pool of water that spreads over the affected area, and majestic sprays, jets, and mists of water erupt forth in a dazzling water show. When you Cast the Spell, and the first time each round you Sustain the spell, you can command the fountain to use one of the following displays, which is accompanied by a loud burst of music. The dancing fountain is somewhat fickle in its desire for novelty, meaning it can't be commanded to use the same display on two consecutive turns.

- **Chasing Jets** A series of vertical jets shoot up in a chase sequence, forcing one creature within the fountain to move 15 feet in a direction of your choice unless it succeeds at a Reflex save against your spell DC. The fountain can't make a creature move outside its area.

- **Flashing Spray** Diffuse fog fills the area of the emanation. All creatures within the fountain become [[Concealed]], and all creatures outside the fountain become concealed to creatures within it. The spray persists until the beginning of your next turn.

- **Power Rings** The fountain blasts a series of rings of water into the air that land with a crash in a @Template[burst|distance:10] centered on a location of your choice within the fountain. The falling torrent deals 10d6 bludgeoning damage to all creatures within the burst (basic Reflex).

**Source:** `= this.source` (`= this.source-type`)
