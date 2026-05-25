---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Olfactory]]", "[[Visual]]"]
cast: "10 minutes"
range: "500 feet"
area: "30-foot burst"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You craft an imaginary scene that includes up to 10 discrete creatures or objects of various sizes, all of which must be within the spell's area. These elements generate appropriate sounds and smells, and they feel right to the touch. Elements of an illusory scene are incapable of speech. Unlike with the [[Illusory Creature]] spell, creatures in your scene lack combat abilities and statistics. Your scene doesn't include changes to the environment around it, though you can place your scene within the illusory environment of a [[Mirage]] spell.

When you create the scene, you can choose to have it be static or follow a program. Though a static scene is stationary, it includes basic natural movement. For example, wind blowing on an illusory piece of paper would rustle it. A program can be up to 1 minute long and repeats when finished. For instance, you could create a scene of two orcs fighting each other, and the fight would go the same way for each repetition. If you create a loop, the two fighters end up in the same place at the start of the scene and at the end of it, but you can smooth the program so it's hard to tell when the loop ends and begins. Anyone observing the scene for more than a few minutes almost always notices it looping. You're unable to alter the program after you create the illusion.

Any creature that touches any part of the image or uses the [[Seek]] action to examine it can attempt to disbelieve your illusion. If they interact with a portion of the illusion, they disbelieve only that portion. They disbelieve the entire scene only on a critical success.

**Heightened (6th)** Creatures or objects in your scene can speak. You must speak the specific lines for each actor when creating your program. The spell disguises your voice for each actor.

**Heightened (8th)** As the 6th-rank version, and the duration is unlimited.

**Source:** `= this.source` (`= this.source-type`)
