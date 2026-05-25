---
type: creature
group: ["Beast", "Incorporeal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Feathered Bear"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Incorporeal"
trait_03: "Spirit"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Fey (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +22, Intimidation +20, Survival +16"
abilityMods: ["+7", "+2", "+5", "+0", "+2", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Mauler"
    desc: "The feathered bear gains a +4 circumstance bonus to damage rolls against creatures they have [[Grabbed]]."
armorclass:
  - name: AC
    desc: "29; **Fort** +21, **Ref** +16, **Will** +18"
health:
  - name: HP
    desc: "160; **Immunities** bleed, disease, paralyzed, poison, precision; **Resistances** all damage 10 except force, ghost touch, spirit"
abilities_mid:
  - name: "Avenging Claws"
    desc: "`pf2:r` **Trigger** A creature within 10 feet damages the feathered bear's ally with a melee attack <br>  <br> **Effect** The feathered bear immediately Steps toward the triggering attacker and makes a claws Strike."
  - name: "Guardian's Aegis"
    desc: "30 feet. All allies within 30 feet of the feathered bear gain a +1 status bonus to saves against magical effects. The bonus increases to +2 if the effect originated from a fiend. <br>  <br> > [!danger] Effect: Guardian's Aegis"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (magical, unarmed), **Damage** 3d10+9 force"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, magical), **Damage** 3d6+9 force plus [[Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 27, attack +19<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Haste]]<br>**2nd** [[Environmental Endurance]], [[Oaken Resilience]]<br>**1st** [[Jump]], [[Know the Way]]"
abilities_bot:
  - name: "Bond with Mortal"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The spirit guide forms a bond with a mortal creature. While the bond exists, the spirit guide increases their current and maximum Hit Points by 20, gains a +2 status bonus to their attack and damage rolls, and can communicate telepathically with the bonded mortal as long as the two beings are on the same plane. <br>  <br> The spirit guide can only be bonded with one mortal at a time, and they can take this action again to end the bond or to form a new bond (which also ends the old bond). The bond also ends if the spirit guide or the mortal dies. <br>  <br> This bond strengthens the spirit guide's connection to the Universe. While bonded, the spirit guide loses the incorporeal and spirit traits, loses their immunities and resistances, and changes their Strikes to deal the appropriate physical damage (typically piercing or slashing) instead of force damage."
  - name: "Bonded Strike"
    desc: "`pf2:2` **Requirements** The spirit guide is currently Bonded with a Mortal <br>  <br> **Effect** The spirit guide makes a jaws Strike. If this attack hits, the bonded mortal can spend their reaction to Strike the same target."
  - name: "Feathered Charge"
    desc: "`pf2:2` The feathered bear Strides and makes a Strike at the end of that movement. During the Stride, the feathered bear ignores difficult terrain and greater difficult terrain, and they can move across air as easily as solid ground. If the feathered bear doesn't end their movement on solid ground, they fall as soon as the Strike is completed."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`



```statblock
creature: "Feathered Bear"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
