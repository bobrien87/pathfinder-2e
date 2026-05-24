---
type: spell
sub-type: Spell
level: 1
traits:
  - "[[concentrate]]"
  - "[[force]]"
  - "[[manipulate]]"
traditions:
  - "[[arcane]]"
  - "[[occult]]"
cast: "`pf2:1` to `pf2:3`"
range: 120 feet
area:
targets: 1 creature
defense:
duration:
trigger:
requirements:
source: Player Core, pg. 332
source-type: Remaster
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

***

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

***

You fire a shard of solidified magic toward a creature that you can see. It automatically hits and deals 1d4+1 force damage. For each additional action you use when Casting the Spell, increase the number of shards you shoot by one, to a maximum of three shards for 3 actions. You choose the target for each shard individually. If you shoot more than one shard at the same target, combine the damage before applying bonuses or penalties to damage, resistances, weaknesses, and so forth.

**Heightened (+2)** You fire one additional shard with each action you spend.

**Source:** `= this.source` (`= this.source-type`)