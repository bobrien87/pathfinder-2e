---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing creature"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

An elemental force fills your target, granting the target the swiftness of air, the ruggedness of earth, the sting of fire, or the flexibility of water, depending on which element you choose. Choose an element when you Cast the Spell. The target gains the benefit of that element as described below, and this spell gains that trait's element.

- **Air** The target gains a +30-foot status bonus to its land Speed and gains a fly Speed equal to its land Speed without the status bonus.

- **Earth** While on the ground, the target gets a +2 status bonus to Fortitude and Reflex saves against effects that would [[Shove]] or [[Trip]] it, and to saves against effects that would attempt to knock it [[Prone]]. In addition, the ground adjacent to the target is difficult terrain, and the difficult terrain moves with the target, though the target ignores this difficult terrain with its own movement.

- **Fire** The target's melee unarmed Strikes and melee weapon Strikes deal 1d6 persistent fire damage on a hit.

- **Metal** The target's Strikes using a metal weapon or an unarmed attack deal an additional 1d4 electricity damage on a hit and get a +1 status bonus to the attack roll if the target is made of metal or wearing metal armor.

- **Water** The target takes on a watery sheen, gaining resistance 5 to fire and a swim Speed equal to its land Speed.

- **Wood** The target gains a number of temporary Hit Points equal to the spell's rank, then gains half that number of temporary HP at the start of each of its turns.

> [!danger] Effect: Spell Effect: Elemental Gift

**Heightened (8th)** You can target up to 5 willing creatures.

**Source:** `= this.source` (`= this.source-type`)
