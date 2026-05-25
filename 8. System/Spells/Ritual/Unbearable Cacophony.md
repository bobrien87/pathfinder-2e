---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Curse]]", "[[Mythic]]"]
cast: "1 day"
range: "1-mile radius circle centered on you"
duration: "3 days"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You amplify the sound of every item and creature to impossible levels. Deaf creatures and creatures immune to sonic damage remain unaffected in most cases.
- **Critical Success** As success, and you and the secondary casters gain sonic resistance equal to your level for the duration.
- **Success** Any sound produced by a creature or object (such as a cricket, a ringing anvil, or a lion's roar) deals sonic damage equal to the level of the creature or item (minimum 1) to every creature within 15 feet (basic Fortitude save with a DC equal to the ritual's casting DC). For every size category over Tiny of the item or creature making noise, this damage increases by 2. Organized groups of creatures, such as a singing quartet or a swarm of insects, count as the next size category larger for this effect. Effects that normally deal sonic damage to creatures and objects ignore half the creature or object's sonic resistance or Hardness.
- **Failure** The ritual has no effect.
- **Critical Failure** An intense sound of ringing echoes in each caster's ears, imparting a weakness to sonic damage equal to their level for 1 day.

**Heightened (+2)** The increase in damage made by creatures larger than Tiny increases to 6 per size category.

**Source:** `= this.source` (`= this.source-type`)
