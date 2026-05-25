---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Concentrate]]", "[[Earth]]", "[[Fire]]", "[[Manipulate]]", "[[Metal]]", "[[Water]]", "[[Wood]]"]
cast: "`pf2:3`"
range: "60 feet"
area: "10-foot burst"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure four types of elementals who combine forces to form into a chaotic storm. The confluence has AC 28 and 120 Hit Points, weakness 10 to area effects, and immunity to bleed and poison. Creatures can move through the confluence; creatures within the confluence are concealed, and all creatures outside the confluence are concealed to creatures within it. When you Cast or Sustain this Spell, you choose up to two different types of elementals to act.

- **Air** (air, electricity) The elemental looses a bolt of electricity from the confluence, dealing 4d4 electricity damage to creatures within 20 feet of the confluence, with a basic Reflex save. This doesn't affect creatures that are completely inside of the confluence.

- **Earth** (earth) The confluence gains a +2 circumstance bonus to AC and resistance 10 to all physical damage (except adamantine) for 1 round.

- **Fire** (fire) Flames roar through the confluence, dealing 1d6 persistent,fire damage to those partially or entirely inside the confluence.

- **Metal** (metal) The elemental flings shards of metal through the confluence, dealing 2d6 slashing damage to those partially or entirely inside the confluence with a basic Reflex save. A creature that critically fails also takes 1d6 persistent,bleed damage.

- **Water** (attack, water) The elemental expels a powerful jet of water. Attempt a ranged spell attack against a target within 60 feet of the confluence, using your spell attack roll modifier. This attack ignores concealment granted by the confluence, and the elemental gets a +2 circumstance bonus on the spell attack roll against a target inside the confluence. The water deals 4d6 bludgeoning damage on a hit (doubled on a critical hit). This attack doesn't count toward your multiple attack penalty.

- **Wood** (wood) Roots and stumps grow, making ground in the area difficult terrain.

**Source:** `= this.source` (`= this.source-type`)
