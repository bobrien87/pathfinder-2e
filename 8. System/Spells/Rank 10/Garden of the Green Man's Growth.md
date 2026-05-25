---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cast your magic into the earth, calling out to a powerful green man, a verdant lesser deity of nature, to come to your aid. They occupy the space of a Medium creature, have a Speed of 40 feet, and a climb Speed of 40 feet.

**Arrive** (plant) *Verdant Bloom* The green man erupts from the ground in a burst of lush growth, dealing 10d8 bludgeoning damage to creatures in a @Template[type:emanation|distance:60] with a basic Reflex save. Creatures that fail this save are pushed 30 feet away from the green man and are knocked [[Prone]]. The area becomes greater difficult terrain for 24 hours.

**Depart** (plant) *Forest of Grasping Vines* The green man casts out their arms, causing vines to rise from the ground, lash at up to six different creatures, and coil them up. Each of these vines targets a different enemy within 100 feet of the green man and deals 12d6 slashing damage with a basic Reflex save. A creature that fails is [[Grabbed]] until it Escapes (on a critical failure it is [[Restrained]] until it Escapes). The [[Escape]] DC is your spell DC. Each creature that begins its turn grabbed or [[Immobilized]] by these vines takes an additional 4d6 bludgeoning damage, as the vines continue to squeeze the life from it.

**Source:** `= this.source` (`= this.source-type`)
