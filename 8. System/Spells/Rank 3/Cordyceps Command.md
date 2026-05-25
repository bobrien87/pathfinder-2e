---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Fungus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "30"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder #203: Shepherd of Decay"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a mote of cordyceps spores uniquely tailored to the target before whisking it at them. When you Cast this Spell, choose one of the following behaviors that the fungus compels: ascend, consume, descend, or lure. While the target is controlled by the cordyceps toxin's stage 3 effects, it performs that behavior. This control might include risky behavior (such as climbing down a precarious cliff or weaving between armed foes), but it doesn't compel outright lethal actions (such as leaping off the top of that same cliff). If the behavior directly leads to harm (such as falling off the cliff) or hostile actions (such as being attacked by creatures that can now reach the descending creature), the target gains a +4 bonus to their next saving throw against the poison.

**Ascend**: The creature tries to reach higher altitudes by any reasonable means, such as Climbing, seeking stairs, or even stacking debris to jump atop of in an attempt to be as high up as possible.

**Consume**: The creature greedily eats or drinks whatever is nearby, using actions to draw and consume elixirs, food, or other consumable items. If the creature has a jaws Strike, fangs Strike, or similar unarmed Strike, the creature can instead chase after and use that Strike against edible targets. If no other food or drink is accessible, the creature attempts to steal or seek nearby nutrition.

**Descend**: The creature tries to reach lower altitudes by any reasonable means, such as Climbing, descending while flying, or even falling [[Prone]] and attempting to burrow into the ground.

**Lure**: The creature moves toward an exposed location and attempts to get bystanders' attention, such as by gesticulating, Performing, or igniting light sources. The target is [[Off Guard]] while controlled in this way.
- **Success** The target is unaffected.
- **Failure** The target is afflicted with cordyceps toxin at stage 1.
- **Critical Failure** The target is afflicted with cordyceps toxin at stage 2.

**Cordyceps Toxin** (poison)

**Saving Throw** DC 28 [[Fortitude]] save;

**Maximum Duration** 6 rounds

**Stage 1** [[Stupefied 1]] (1 round)

**Stage 2** [[Confused]] (1 round)

**Stage 3** [[Controlled]] (1 round)

**Source:** `= this.source` (`= this.source-type`)
