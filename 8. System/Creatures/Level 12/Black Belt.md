---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Black Belt"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +25, Stealth +20, Martial Arts Lore +22"
abilityMods: ["+5", "+4", "+3", "+1", "+3", "+0"]
abilities_top:
  - name: "Powerful Fists"
    desc: "The black belt's fist Strikes don't take penalties when making lethal attacks, and fist Strikes are treated as cold iron and silver."
armorclass:
  - name: AC
    desc: "32; **Fort** +23, **Ref** +23, **Will** +20"
health:
  - name: HP
    desc: "220"
abilities_mid:
  - name: "Blocking Counterattack"
    desc: "`pf2:r` **Trigger** A creature within the black belt's reach targets them with a melee attack <br>  <br> **Effect** The black belt blocks, gaining a +2 circumstance bonus to their AC against the triggering attack. If the attack misses, the black belt retaliates with a Strike. This Strike doesn't count toward the black belt's multiple attack penalty, and the multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bo Staff +25 (`pf2:1`) (magical, parry, reach, trip), **Damage** 2d8+9 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, magical, nonlethal, unarmed), **Damage** 2d8+9 bludgeoning"
spellcasting:
  - name: "Monk Focus Spells"
    desc: "DC 32, attack +23<br>**1st** [[Inner Upheaval]], [[Qi Rush]]"
abilities_bot:
  - name: "Flurry of Blows"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The black belt makes two fist Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. <br>  <br> The black belt can substitute any number of the attacks with bo staff Strikes or attempts to `act grapple`, `act reposition`, `act shove`, or `act trip`."
  - name: "Rapid Barrage"
    desc: "`pf2:2` The black belt pummels their fists in a fast onslaught. They make three fist Strikes against one target. If more than one Strike hits, combine damage for the purpose of resistances and weaknesses. Regardless of whether any Strikes hit, the target must succeed at a DC 32 [[Fortitude]] save or be [[Clumsy]] 1 until the end of their next turn and [[Stunned]] 1 ([[Clumsy]] 2 and [[Stunned]] 2 on a critical failure)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many martial arts schools use colored belts to differentiate skill levels. Above all is the black belt, an advanced practitioner who can counter any attack.

Martial artists strive to master the art of hand-to-hand fighting.

```statblock
creature: "Black Belt"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
