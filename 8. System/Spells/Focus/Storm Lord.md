---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Air]]", "[[Concentrate]]", "[[Druid]]", "[[Electricity]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "100-foot emanation"
defense: "basic Reflex"
duration: "1 minute (sustained)"
requirements: "You are outdoors and aboveground."
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The sky above you darkens in a matter of moments, swirling with ominous clouds punctuated by flashes of lighting. When you Cast the Spell and the first time you Sustain it each turn on subsequent rounds, select one of the following effects to occur in the area.

- **Calm** No additional effect.

- **Fog** Heavy fog rolls in, concealing the area with the effects of [[Mist]].

- **Rain** Torrential rain falls from the sky, dousing ordinary flames. Creatures in the area take a -2 circumstance penalty to Acrobatics and Perception checks.

- **Wind** Powerful winds buffet the area in all directions. Ranged attacks take a -4 circumstance penalty, and the area is difficult terrain for flying creatures.

In addition, once per round you can use a single action, which has the concentrate and manipulate traits, to call down a bolt of lightning, striking any target in range that you can see. You deal 10d6 electricity damage to the target; it must attempt a basic Reflex save. On a failure, it is also [[Deafened]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
