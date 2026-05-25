---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fortune Dragon (Young)"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+19; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Acrobatics +21, Arcana +22, Athletics +21, Crafting +22, Diplomacy +19, Thievery +21, Accounting Lore +22, Mercantile Lore +22"
abilityMods: ["+5", "+5", "+4", "+6", "+3", "+3"]
abilities_top:
  - name: "Draconic Momentum"
    desc: "Whenever they score a critical hit with a Strike, the dragon chooses to either recharge Disruptive Breath or regain one expended spontaneous spell slot."
armorclass:
  - name: AC
    desc: "30; **Fort** +18, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "175; **Immunities** drained, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Capture Spell"
    desc: "`pf2:r` **Trigger** The dragon succeeds or critically succeeds on a saving throw against a spell <br>  <br> **Effect** The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 5, counteract modifier +20). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d10+11 piercing plus 1d6 force"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, magical, unarmed), **Damage** 1d6 force plus 2d6+11 piercing"
  - name: "Melee strike"
    desc: "Tail +19 (`pf2:1`) (magical, reach 15 ft.), **Damage** 1d6 force plus 2d10+11 bludgeoning"
spellcasting:
  - name: "Arcane Spontaneous Spells"
    desc: "DC 30, attack +22<br>**5th** (1 slots) [[Slither]]<br>**4th** [[Unfettered Movement]]<br>**3rd** [[Fireball]]<br>**1st** [[Detect Magic]], [[Force Barrage]], [[Read Aura]]"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "`pf2:2` The dragon unleashes a spray of magic-disrupting energies that deals @Damage[9d6[force]|options:area-damage] damage in a @Template[cone|distance:30] (DC 30 [[Reflex]] save). Creatures that fail become [[Stupefied 1]] ([[Stupefied 2]] on a critical failure) for 1 minute. <br>  <br> The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one tail Strike in any order."
  - name: "Share the Wealth"
    desc: "`pf2:2` **Requirements** The dragon's body is covered in riches (this is typically the case when the dragon is first encountered) <br>  <br> **Effect** The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing @Damage[6d10[bludgeoning]|options:area-damage] damage with a DC 29 [[Reflex]] save to all creatures in a @Template[emanation|distance:30]. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "`pf2:2` **Requirements** The dragon's body isn't covered in riches and the dragon is adjacent to their hoard <br>  <br> **Effect** The dragon Strides or Burrows through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. <br>  <br> The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 27 [[Reflex]] save or be pushed 10 feet (or pushed 20 feet and knocked [[Prone]] on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fortune dragons have the innate ability to draw upon the raw magical energies that surround them. They constantly use these magical energies to empower their magical abilities and even their bodies, as the energy can heal wounds. A fortune dragon has a typical build for an arcane dragon, but their bodies sport a striking feature: their treasure. The dragon's nature of drawing upon magic causes coins, gems, and, most notably, magical items to cling to their body like iron drawn to magnets. A dragon constantly pulls magical energies from the items attached to their body and makes use of these energies to cast spells. The magical energies that flow through a fortune dragon constantly flow through the dragon's items as well, and in many cases, the items melt from the heat produced in this process. Fortune dragons are seekers of novel experiences. This desire for originality leads fortune dragons to approach visitors of other ancestries with curiosity, though this initial interest quickly wanes if a visitor lacks exciting qualities.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Fortune Dragon (Young)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
