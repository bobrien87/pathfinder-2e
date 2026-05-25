---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]", "[[Unholy]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Reaching out to the legions of the wicked, you call upon them for assistance. They emerge, bubbling up from the ground, and stand to face your enemies, malevolent and ready for bloodshed. The unholy army occupies the space of a Huge creature. When you Cast this Spell, choose one of the unholy squadrons below to summon.

- **Asuras** Speed 40 feet

- **Arrive** *Dance of Duality* A legion of adhukaits arrive on the field, dancing and scurrying in and among your enemy's front line. All enemies in a @Template[emanation|distance:10] take @Damage[10d6[slashing]|options:area-damage] damage ([[Reflex]] save) as the adhukaits slash at them with their kukris.
- **Depart** *Split Remembrance* As the adhukaits begin to retreat, they argue about who did the most damage and decide to see which half is stronger. All enemies in a @Template[emanation|distance:20] take @Damage[6d6[bludgeoning]|options:area-damage] damage ([[Fortitude]] save) as they're violently yanked by adhukaits. On a failure, a creature is [[Clumsy]] 1 for 1 minute ([[Clumsy]] 2 on a critical failure).

- **Daemons** Speed 25 feet, fly 40 feet

- **Arrive** (disease) *Winds of Pestilence* Leukodaemons fly into position, their wings beating with the dust of a thousand diseases of a thousand years. Enemies in a @Template[cone|distance:60] take @Damage[8d8[piercing]|traits:disease|options:area-damage] damage ([[Fortitude]] save). On a failure, a creature is also [[Sickened]] 1 ([[Sickened]] 2 on a critical failure).
- **Depart** (disease) *Remember Me* The leukodaemons claw at your enemies with their infected nails. All enemies in a @Template[emanation|distance:10] take @Damage[6d6[slashing]|traits:disease|options:area-damage] damage ([[Reflex]] save). On a failure, a creature is also [[Drained]] 1 ([[Drained]] 2 on a critical failure).

- **Demons** Speed 25 feet

- **Arrive** (fire) *Fuming Entrance* A legion of brimoraks arrive in clouds of thick black smoke. The army's space and every square in a @Template[emanation|distance:20] is choked with burning ash and smog, making all creatures outside the smoke [[Concealed]] to creatures within it and all creatures within the smoke concealed to creatures outside the smoke and other creatures within it. This smoke lasts for 1 minute, and a creature who enters or begins its turn within the smoke must attempt a [[Fortitude]] save or take @Damage[2d6[persistent, fire]|options:area-damage] damage and become sickened 1 (3d6 persistent,fire damage and sickened 2 on a critical failure).
- **Depart** (fire) *Swords of Flame* The arson demons swing their flaming swords through your enemies' ranks. All enemies in a @Template[emanation|distance:10] take @Damage[(4d8)[slashing],(3d6)[fire]|options:area-damage] ([[Reflex]] save). On a critical failure, a creature also takes @Damage[2d8[persistent,fire]|options:area-damage] damage.

- **Devils** Speed 25 feet

- **Arrive** (spirit) *Diabolic Infantry* A legion of vordines swarm the battlefield. All enemies in a @Template[emanation|distance:20] take @Damage[4d10[piercing],2d6[spirit]|options:area-damage] damage ([[Reflex]] save) as the vordines impale them with their tridents.
- **Depart** (nonlethal) *Whipped and Tripped* The devils' whips lengthen impossibly to flense flesh from soul. Enemies in two non-intersecting 40-foot lines take @Damage[6d8[bludgeoning]|traits:nonlethal|options:area-damage] damage ([[Reflex]] save). On a failure, a creature is also knocked [[Prone]]. On a critical failure, it's also knocked prone and [[Immobilized]] for 1 round.

- **Divs** Speed 35 feet

- **Arrive** (mental) *Deceptive Delight* A battalion of sepids arrives to torment your enemies. Enemies in a @Template[cone|distance:60] take @Damage[6d6[mental]|options:area-damage] damage ([[Will]] save). On a failure, a creature is [[Confused]] for 1 round.
- **Depart** (spirit) *Battle Debris* The sepids slam their falchions into the remnants of the chaos of battle, shattering bones, which explode out in a @Template[emanation|distance:30]. All non-fiends in the area take @Damage[8d6[slashing],3d6[spirit]|options:area-damage] damage from debris ([[Reflex]] save).

- **Qlippoths** Speed 40 feet, climb 40 feet, fly 40 feet

- **Arrive** (visual) *Terrifying Scuttle* A horde of gongorinans opens their maws to reveal the horror inside. All enemies in a @Template[cone|distance:60] must succeed at a [[Will]] save or be sickened 2 (sickened 2 and [[Blinded]] for 1 round on a critical failure).
- **Depart** *Pincer Assault* The gongorinans lash out at everyone. All enemies in a @Template[emanation|distance:20] take @Damage[6d12[slashing]|options:area-damage] damage ([[Reflex]] save).

- **Velstracs** Speed 25 feet

- **Arrive** *Chains of Pain* A legion of sacristans emerges from the shadows, their barbed chains wrapping around enemy limbs to prevent all escape. Enemies in a @Template[emanation|distance:20] must attempt a [[Reflex]] save. On a failure, they take a –10-foot circumstance penalty to their Speeds and @Damage[2d6[bleed]|options:area-damage] damage. On a critical failure they take a –20-foot circumstance penalty to their Speeds and 4d6 bleed damage. This penalty to Speeds lasts until they recover from their persistent bleed damage
- **Depart** *Pleasant Screams* The sacristans rip their chains from their victims, screaming in unison with their pain. Any enemies who failed the initial Reflex save during the sacristans' arrival take 4d8 piercing damage ([[Fortitude]] save). In addition, everyone in a @Template[cone|distance:60] must attempt a [[Will]] save. On a failure, they're [[Frightened]] 2 and [[Deafened]] for 1 minute ([[Frightened]] 3 and deafened for 1 minute on a critical failure); this effect has the auditory, emotion, fear, and mental traits.

**Source:** `= this.source` (`= this.source-type`)
