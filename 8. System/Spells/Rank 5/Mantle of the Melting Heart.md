---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]", "[[Morph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You bathe yourself in a mantle of liquid metal, gilding your skin and armor with an oily sheen. Upon Casting this Spell, pick two of the options below. As a single action, which has the concentrate trait, you can change one of your chosen abilities to a different option from the list.

- **Copper Core** You draw electricity toward you, then disperse it. You gain resistance 10 to electricity. All electricity effects within 30 feet of you must succeed at a counteract check against your spell DC or target you and only you.
- **Golden Flesh** Your body gains the chemical inertness of gold, barely reacting to substances that would otherwise greatly disturb your physiology. You become immune to poison and disease and gain a +2 circumstance bonus to your checks against any poison and disease effects currently affecting you.
- **Reactive Touch** Your touch reacts easily with other metals. Any metal that touches you or that you touch takes 2d6 acid damage that bypasses Hardness.
- **Weighted Grasp** Your arms become long cables, your fists heavy as anchors. You gain a cabled fist unarmed attack with the disarm, finesse, reach, and trip traits and that's in the flail group. Your cabled fist deals 1d4 bludgeoning damage plus an additional 1d6 poison damage and Grab.

> [!danger] Effect: Spell Effect: Mantle of the Melting Heart

**Source:** `= this.source` (`= this.source-type`)
