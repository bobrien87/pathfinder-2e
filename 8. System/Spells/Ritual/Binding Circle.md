---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
cast: "1 day"
range: "interplanar"
targets: "1 extraplanar creature"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth an extraplanar creature of a level no greater than double that of the *binding circle* ritual's rank and attempt to bargain with it, generally to perform a task for you in exchange for payment.

You conjure the extraplanar creature within your circle and negotiate a deal with it. A creature that doesn't wish to negotiate at all can attempt a Will save to stay on its home plane. Most extraplanar creatures feel that they have something better to do than cater to the whims of mortals and require a significant gift, especially if your task poses major risks. Fiends and similarly wicked extraplanar creatures are more likely to accept a bargain for a lower cost as long as it allows them to wreak havoc on the Universe or inflict evil upon the world along the way.

Monetary prices usually range from the cost of a consumable item of the creature's level for a short and simple task to a permanent magic item of the creature's level or more to persuade the creature to fight alongside you. However, some extraplanar creatures may want payments other than money, such as permission to cast a [[Geas]] on you to fulfill an unspecified later favor or obtain ownership of your soul via an infernal contract.

You can add an additional secondary caster to create a warding circle that prevents the extraplanar creature from attacking or leaving the circle during the bargain. This uses the Crafting skill and has the same DC as a secondary check would. This protection ends if you use a hostile action against the extraplanar creature or the warding circle breaks.
- **Critical Success** You call the extraplanar creature and can prevent it from returning home for up to a full day, potentially allowing you to negotiate a better deal by threatening to leave it in the wards for the duration.
- **Success** You call the extraplanar creature and must make your case succinctly, after which the creature can return home at any time.
- **Failure** You fail to call the extraplanar creature.
- **Critical Failure** You call something vile and horrible, unbound by your wards, and it immediately attempts to destroy you.

**Source:** `= this.source` (`= this.source-type`)
