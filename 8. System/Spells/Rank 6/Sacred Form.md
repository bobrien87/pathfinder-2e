---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You focus all your divine energy and transform yourself into a battle form, similar to your normal form and of the same size as you, but wielding powerful divine armaments. While in this form, you gain the statistics and abilities listed below. You have hands in this battle form and can use manipulate actions. You can Dismiss the spell. You gain the following statistics and abilities.

- AC = 20 + your level. Ignore your armor's check penalty and Speed reduction.
- 10 temporary Hit Points.
- Speed 40 feet.
- Resistance 3 against physical damage.
- Darkvision.
- A special attack with a sacred armament, which is the only attack you can use. Your attack modifier with the sacred armament is +21, and your damage bonus is +8 (or +6 for a ranged attack). The damage dice for Strikes with the weapon are 3d6 bludgeoning damage plus 1d6 spirit damage. If you have a deity, you can have the weapon take the form of your deity's favored weapon and use its damage die size, damage type, and traits. If the favored weapon is a simple weapon with 1d4 or 1d6 damage die, the weapon damage dice are one size larger than normal, though the spirit damage is unchanged. You can also use your attack modifier with this favored weapon if it's higher than that given by the spell.
- Athletics modifier of +23, unless your own is higher.

**Heightened (8th)** You instead gain AC = 21 + your level, 15 temporary Hit Points, resistance 4 against physical damage, attack modifier +28, damage bonus +15 (+12 for a ranged attack), and Athletics +29. If you're Medium or smaller, your battle form is Large, and your attacks also have 10-foot reach, or 15-foot reach if you're using a favored weapon with reach.

> [!danger] Effect: Spell Effect: Sacred Form

**Source:** `= this.source` (`= this.source-type`)
