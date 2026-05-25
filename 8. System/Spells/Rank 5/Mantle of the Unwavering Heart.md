---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Morph]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Vines and branches envelop you in an instant, growing a wild bloom of colors that open to reveal your new form. Upon Casting this Spell, pick two of the options below. As a single action, which has the concentrate trait, you can change one of your chosen abilities to a different option from the list.

- **Evergreen Vitality** You gain fast healing 3 and a +2 bonus to saves against poison and disease. This effect has the healing and vitality traits.

- **Overwhelming Perfume** (aura, olfactory) A cloud of potent floral scent surrounds you in a @Template[emanation|distance:15]. Creatures in the aura can't benefit from the scent ability and are [[Sickened]] 1 as long as they remain in the aura. The sickness is a disease effect.

- **Towering Trunk** You grow to a considerable height. Increase your size to Large. You're [[Clumsy]] 1. Your reach increases by 5 feet (or by 10 feet if you started out Tiny), and you gain a grasping branch unarmed attack; this attack is in the brawling weapon group and deals 2d8 bludgeoning damage plus Grab.

- **Unyielding Will** Your mind becomes incredibly resilient to change. You're immune to being [[Fascinated]], and you get a +1 bonus to saves and DCs against mental effects.

> [!danger] Effect: Spell Effect: Mantle of the Unwavering Heart

**Source:** `= this.source` (`= this.source-type`)
