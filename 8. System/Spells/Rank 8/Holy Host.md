---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Holy]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

In stories, armies with just and righteous causes win with little difficulty, conquering unholy legions. However, many holy armies know that an extra hand never hurts in the fight to exterminate cruelty and unholy forces, and they might call upon the assistance of a holy army. The holy army occupies the space of a Huge creature. When you Cast this Spell, choose one of the holy militaries below to summon.

- **Agathions** Speed 30 feet

- **Arrive** (fire) *Pranks for All* A squadron of procyals arrives, eager to see your enemies learn their lesson in this fight. All enemies in a @Template[cone|distance:60] take @Damage[8d6[fire]|options:area-damage|traits:fire] damage ([[Reflex]] save) as the procyals bombard them with popping firecrackers
- **Depart** *Parting Lesson* (emotion, mental) The procyals laugh uproariously as they leave, each throwing out a piece of unrelated advice to a nearby enemy. Enemies in a @Template[type:emanation|distance:20] take @Damage[4d6[mental]|options:area-damage|traits:emotion,mental] damage ([[Will]] save). On a failure, a creature is also [[Stunned]] 1. On a critical failure, they're [[Stunned]] 2.

- **Angels** Speed 30 feet, fly 40 feet

- **Arrive** (spirit) *Flaming Truth* A legion of balisses arrive in a burst of holy flame, dealing @Damage[8d6[spirit]|options:area-damage] damage to all creatures in a @Template[type:emanation|distance:20] with a [[Fortitude]] save. On a critical failure, a creature is also [[Blinded]] for 1 round
- **Depart** *Hidden Departure* With a plume of smoke, the balisses vanish, spreading a thick cloud of smoke in a @Template[type:emanation|distance:10]. All creatures within the smoke are [[Concealed]]. Unholy creatures within the smoke are [[Enfeebled]] 2, and holy creatures within the smoke gain the effects of truesight and ignore the concealment granted by the smoke.

- **Archons** Speed 30 feet, fly 60 feet

- **Arrive** (spirit) *Justice Prevails* A battalion of aesras, also known as legion archons, swoop in to provide assistance. Enemies within a @Template[type:cone|distance:60] take @Damage[8d6[spirit]|options:area-damage] damage ([[Reflex]] save)
- **Depart** (fire) *Eyes of Judgment* With one final examination of the battlefield, the aesras take their leave, but not before bringing down their fiery swords to create a corridor of sacred flame. Enemies in a @Template[type:line|distance:60] take @Damage[4d6[slashing],2d6[persistent,fire]|options:area-damage] damage ([[Reflex]] save).

- **Azatas** Speed 30 feet, fly 80 feet

- **Arrive** (auditory, sonic) *Inspiring Song* Kanya muses arrive to embolden your allies while pushing back your foes. Enemies in a @Template[type:emanation|distance:20] take @Damage[6d6[sonic]|options:area-damage|traits:auditory,sonic] damage ([[Fortitude]] save). A creature that fails the save is also pushed 10 feet away from the kanyas. Allies in the emanation gain a +2 status bonus to attack rolls and saving throws, as well as +4 status bonus to damage rolls for the duration of the spell
- **Depart** (emotion, fear, mental) *Booming Finale* With a thunderous chord that stirs the hearts of your forces, the kanyas depart. Enemies in a @Template[type:cone|distance:60] must attempt a [[Will]] save. On a failure, they're [[Frightened]] 2, and on a critical failure, they're [[Frightened]] 3 and [[Deafened]] for 1 round. Allies in this cone regain @Damage[(4d10+16)[healing]|traits:emotion,fear,mental] Hit Points.

- **Garudas** Speed 25 feet, fly 60 feet

- **Arrive** *Swooping Dive* A battalion of garudas sweep through enemy lines, dealing @Damage[6d10[slashing]|options:area-damage] damage to enemies in a @Template[line|distance:120] ([[Reflex]] save)
- **Depart** *Winds of Freedom* The garudas flap their wings in tandem, focusing on a @Template[burst|distance:20] within 60 feet of them. All allies in that area gain a +1 circumstance bonus to all skill checks and DCs for 1 round, and enemies must succeed a [[Reflex]] save or be knocked [[Prone]].

> [!danger] Effect: Spell Effect: Holy Host (Azata)

> [!danger] Effect: Spell Effect: Holy Host (Garuda)

**Source:** `= this.source` (`= this.source-type`)
