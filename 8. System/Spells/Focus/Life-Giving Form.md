---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Light]]", "[[Manipulate]]", "[[Oracle]]", "[[Vitality]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transcend your physical form, becoming a beacon of healing energy. Your body exudes bright light like a torch. You gain resistance 5 to precision damage and weakness 5 to void damage, and your unarmed Strikes deal an extra 1d4 vitality damage. You can touch a living creature with an Interact action to restore @Damage[(@item.level)d8[healing,vitality]|shortLabel:true] Hit Points to it, and when a creature touches you with an Interact action you can allow it to gain the same healing; either way, the creature becomes temporarily immune to life-giving form's healing for 1 minute. This is a vitality healing effect. You can't heal yourself with life-giving form. A creature harmed by vitality damage (such as an undead) that touches you or damages you with an unarmed attack or non-reach melee weapon instead takes @Damage[(3d4 + (@item.level - 6))[vitality]] damage, and it doesn't become temporarily immune. You can Dismiss this spell.

> [!danger] Effect: Spell Effect: Life Giving Form

**Heightened (+1)** The Hit Points restored with an Interact action increases by 1d8, the vitality damage increases by 1, and the resistance and weakness increases by 1

**Source:** `= this.source` (`= this.source-type`)
