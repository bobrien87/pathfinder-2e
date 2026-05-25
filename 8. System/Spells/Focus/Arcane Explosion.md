---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Force]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "basic Fortitude"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your body is temporarily converted into a ball of pure magic, rapidly exploding outward and reforming as a glowing sphere, after which you eventually regain your normal form. All creatures and objects in the emanation take 16d6 force damage (basic Fortitude saving throw). Creatures that fail are also pushed 10 feet directly away from you; creatures that can't complete this forced movement are knocked [[Prone]] (but creatures who reduce this movement, such as with an ability or feat, don't fall prone). You become unfiltered magic; you gain the incorporeal trait, are immune to disease, poison, and precision damage, and gain resistance to all damage equal to your level (except force damage, spirit damage, and damage from Strikes with the [[Ghost Touch]] property rune), with double the resistance against non-magical damage. While incorporeal, you can't Strike, Cast a Spell, or take any actions with the manipulate trait. Any creature that ends its turn adjacent to you while you're in this state takes 6d6 force damage. You remain as pure magic until you Dismiss your new form, returning to your normal state at maximum Hit Points.

> [!danger] Effect: Spell Effect: Arcane Explosion

**Source:** `= this.source` (`= this.source-type`)
