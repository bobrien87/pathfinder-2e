---
type: creature
group: ["Fiend", "Sahkil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nucol"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]], [[Scent]] (imprecise) 100 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Athletics +12, Deception +10, Intimidation +12, Stealth +10"
abilityMods: ["+4", "+2", "+3", "+0", "+3", "+2"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Easy to Call"
    desc: "A nucol's level is considered 2 lower for the purpose of being conjured by the [[Binding Circle]] ritual (and potentially other rituals, at the GM's discretion), but it is always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
  - name: "Nervous Consumption"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Onset** 1 minute <br>  <br> **Stage 1** [[Sickened]] 1 and [[Stupefied 1]] (1 day) <br>  <br> **Stage 2** [[Clumsy]] 1 and [[Stupefied 2]] (1 day) <br>  <br> **Stage 3** [[Clumsy]] 2 and [[Stupefied 3]] (1 day)"
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +10, **Will** +11"
health:
  - name: HP
    desc: "75; **Immunities** disease, fear effects; **Weaknesses** holy 5; **Resistances** poison 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tusk +12 (`pf2:1`) (deadly d10, unarmed, unholy), **Damage** 2d8+6 piercing plus 1d4 spirit plus [[Nervous Consumption]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20, attack +12<br>**2nd** [[Cleanse Affliction]]<br>**1st** [[Detect Magic]], [[Fear]] (At Will), [[Grease]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Skip Between"
    desc: "`pf2:1` The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Spray Pus"
    desc: "`pf2:1` The nucol flexes one of its infected wounds, releasing a spray of pus in a @Template[cone|distance:15] or targeting an individual creature within 30 feet. A creature targeted or in the area is exposed to nervous consumption."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Representing the fear of parasites and affliction, nucols appear as violent, pestilence-ridden boars. They pollute their victim's body and mind, spreading not only fear but a mind-altering affliction that exacerbates feelings of self-doubt.

Though very aggressive, the fiends are capable of cunning manipulation. After they infect a victim with potent insecurity, they'll offer to remove the affliction for a price. Many of these deals are esoteric in nature, driving the victim into despair and forcing them to give up things they cherish. The sinister nucol may even reinfect its victim after completing the bargain, but a canny negotiator may be able to turn the tables on the fiend and free themselves from its grasp.

Ages ago, when this cycle of the multiverse was still adolescent, a cabal of psychopomps who already felt bored and restrained in their role of ushering souls to their ultimate resting place rebelled against their station. It was this corruption of the cycle of souls that spawned the first sahkils.

Ambivalent to the prescribed order of the multiverse and spiteful of mortals, sahkils delight in spreading fear and unease to all beings, clogging up the metaphysical cycle with anxiety-ridden mortals too scared to achieve their potential. These fiends have drastically changed from their dedicated psychopomp predecessors. They are creatures of spite and torment, fear and disgust. They exploit the most common and rare fears for their own perverse satisfaction, and they want nothing more than to frighten mortals and make them quetion their reason for existence.

Most sahkils lurk on the Ethereal Plane, but they frequently invade the Material Plane to torment mortals and spread terror. They use their innate ability to slip between the veils of the Ethereal and Material effortlessly, often stalking their targets for days or weeks before enacting their devious plots.

```statblock
creature: "Nucol"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
