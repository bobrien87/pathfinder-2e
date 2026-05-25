---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:3`"
range: "500 feet"
duration: "until the end of your next turn"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure the rotting corpse of Deskari, previously Lord of the Locust Hosts, to the battlefield. Deskari's corpse occupies the space of a Gargantuan creature. The corpse is riddled with vermin, including countless locusts, whose collective movement grants the corpse a Speed of 60 feet and a fly Speed of 60 feet.

**Arrive** *Behold the Rotten Lord* Deskari's corpse is unspeakably foul, emitting a putrid stench, and constantly twitches thanks to the movement of the millions of insects and vermin that consume it. A loud, persistent buzzing is created by the clouds of locusts surrounding it like a haze. Each living enemy creature within a @Template[type:emanation|distance:60] must attempt a Fortitude save with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Sickened]] 2.
- **Failure** The creature is [[Sickened]] 3 and [[Deafened]] for the duration.
- **Critical Failure** The creature is [[Sickened]] 4, [[Stunned]] 1, and deafened for the duration.

**Depart** (poison) *Feast of the Locust Host* The millions of insects and vermin feasting on Deskari pour out of its corpse and surge across the battlefield, consuming your enemies. This swarm deals 5d8 piercing damage and 5d8 poison damage to enemy creatures in a @Template[type:emanation|distance:60] with a basic Reflex save. A creature that critically fails is additionally [[Drained]] 2.

**Source:** `= this.source` (`= this.source-type`)
