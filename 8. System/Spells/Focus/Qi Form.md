---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Monk]]", "[[Polymorph]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Drawing from deep wells of spiritual power, you take on a special qi form. In your qi form, your hair, feathers, skin, or scales change color and begin to glow.

In this form, you gain a fly Speed equal to your land Speed. Choose force, spirit, vitality, or void damage. All your Strikes deal 1d6 additional damage of the chosen type.

Your entire body is also surrounded by a glowing corona of the same color as your inner qi; this is a light effect. Your corona is an aura in a 5-foot emanation that deals 2d6 damage of the chosen type to creatures who start their turn within the emanation. If the emanation overlaps with a darkness effect, the corona's glow attempts to counteract the darkness. Regardless of the outcome, the corona can't attempt to counteract that effect again for 1 day. You can Sustain to flare your corona out to become a 30-foot emanation or return the corona to a 5-foot emanation.

In your qi form, your emotions surge to the forefront, and it's difficult to moderate your attacks. Your weapons and unarmed attacks lose the nonlethal trait. You take a –2 status penalty to saves against emotion effects but gain a +2 status bonus to saves against all other mental effects.

> [!danger] Effect: Spell Effect: Qi Form

**Source:** `= this.source` (`= this.source-type`)
