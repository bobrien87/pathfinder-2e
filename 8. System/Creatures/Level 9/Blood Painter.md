---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Blood Painter"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Bloodsense]] (imprecise) 60 feet, [[Darkvision]]"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Athletics +20, Crafting +17, Medicine +19, Stealth +17, Art Lore +21"
abilityMods: ["+5", "+4", "+3", "+6", "+4", "+3"]
abilities_top:
  - name: "Bloodsense (Imprecise) 60 feet"
    desc: "A blood painter can detect exposed blood as an imprecise sense at the listed range, including from creatures taking [[Persistent Bleed Damage]]."
armorclass:
  - name: AC
    desc: "27; **Fort** +16, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "155"
abilities_mid:
  - name: "Easily Fascinated"
    desc: "When subject to a visual illusion with the incapacitation trait, the blood painter doesn't adjust their degree of success due to the incapacitation trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 3d8+8 slashing plus 1d8 bleed"
spellcasting:
  - name: "Paint"
    desc: "DC 20, attack +28<br>**6th** [[Vibrant Pattern]]<br>**5th** [[Cloak of Colors]]<br>**2nd** [[Illusory Creature]]<br>**1st** [[Illusory Disguise]], [[Illusory Object]]"
abilities_bot:
  - name: "Dab"
    desc: "`pf2:1` **Requirements** The blood painter is within reach of an enemy taking [[Persistent Bleed Damage]]. <br>  <br> **Effect** The blood painter touches the creature and applies blood to one of their four claws; the blood remains fresh for 1 minute. The target must succeed at a DC 28 [[Will]] save or become [[Fascinated]] with the blood painter."
  - name: "Paint"
    desc: "`pf2:1` **Requirements** The blood painter has fresh blood applied to a claw using Dab <br>  <br> **Effect** The blood painter expends the blood on one claw to paint an illusion with the efects of one of the following spells: [[Illusory Creature]], [[Illusory Disguise]], or [[Illusory Object]]. The Paint action gains the traits of the spell it's reproducing, and the blood painter can Sustain these efects. They use a spell attack modifer of Blood painter paint check{+20} and DC 28 for these efects, which are heightened to 5th rank. <br>  <br> If they have fresh blood applied to two or more claws, the blood painter can expend the blood on all of them to instead produce the effects of [[Cloak of Colors]] or [[Vibrant Pattern]]. <br>  <br> Any effects produced by this ability have a +2 status bonus to attack rolls, damage rolls, saving throws, skill checks, and AC against the creature whose blood was used to Paint. That creature also takes a –2 status penalty to Perception checks and saves against them."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Simultaneously enamored with the natural world yet too alien to survive in it, blood painters are eight-limbed artists who stalk, kill, and dismember in search of pigment and sustenance alike. Blood painter physiology can't digest typical food, so the creatures feed by harvesting blood and using it to paint and animate something edible.

When not on the hunt, blood painters seek out beautiful vistas, which they placidly admire via the eyes in the hands of their uppermost limbs and then reproduce on canvas. Exceptional art endlessly fascinates these creatures, and skilled dancers and painters alike occasionally escape the aberrations by creating a new work to trade for their lives. Blood painters jealously guard these works, and much of their treasure consists of art. Blood painters tend to mastermind the periodic theft of masterpieces.

```statblock
creature: "Blood Painter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
