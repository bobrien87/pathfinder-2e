---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fortune Dragon (Ancient, Spellcaster)"
level: "19"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Dwarven, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +36, Arcana +37, Athletics +34, Crafting +37, Diplomacy +32, Thievery +36, Accounting Lore +37, Mercantile Lore +37"
abilityMods: ["+9", "+9", "+8", "+10", "+5", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "43; **Fort** +31, **Ref** +34, **Will** +32"
health:
  - name: HP
    desc: "300; **Immunities** drained, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Aura of Disruption"
    desc: "120 feet. <br>  <br> The dragon radiates disruptive energies that allow them to feed on magic. When a spell is counteracted or disrupted within the aura, the dragon regains one expended spontaneous spell slot and gains 35 temporary Hit Points that last for 1 minute."
  - name: "Capture Spell"
    desc: "`pf2:r` **Trigger** The dragon succeeds or critically succeeds on a saving throw against a spell <br>  <br> **Effect** The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 10, counteract modifier +37). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +34 (`pf2:1`) (magical, reach 20 ft., unarmed), **Damage** 4d10+15 piercing plus 1d6 force"
  - name: "Melee strike"
    desc: "Claw +34 (`pf2:1`) (agile, magical, reach 15 ft., unarmed), **Damage** 1d6 force plus 4d6+15 piercing"
  - name: "Melee strike"
    desc: "Tail +32 (`pf2:1`) (magical, reach 25 ft.), **Damage** 1d6 force plus 4d10+15 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 45, attack +37<br>**9th** (3 slots) [[Detonate Magic]], [[Falling Stars]], [[Phantasmagoria]]<br>**8th** (3 slots) [[Arctic Rift]], [[Disappearance]], [[Uncontrollable Dance]]<br>**7th** (3 slots) [[Contingency]], [[Energy Aegis]], [[Planar Palace]]<br>**6th** (3 slots) [[Cursed Metamorphosis]], [[Teleport]], [[Wall of Force]]<br>**5th** (3 slots) [[Howling Blizzard]], [[Scouting Eye]], [[Toxic Cloud]]<br>**4th** (3 slots) [[Flicker]], [[Translocate]], [[Vision of Death]]<br>**3rd** (3 slots) [[Aqueous Orb]], [[Grease]], [[Haste]]<br>**2nd** (3 slots) [[Invisibility]], [[Mist]], [[Web]]<br>**1st** (3 slots) [[Gust of Wind]], [[Item Facade]], [[Phantasmal Minion]]<br>**Cantrips** [[Electric Arc]], [[Figment]], [[Prestidigitation]], [[Shield]], [[Telekinetic Hand]]"
  - name: "Arcane Spontaneous Spells"
    desc: "DC 45, attack +37<br>**9th** [[Implosion]]<br>**8th** [[Quandary]]<br>**7th** [[Warp Mind]]<br>**6th** [[Chain Lightning]]<br>**5th** [[Slither]]<br>**4th** [[Unfettered Movement]]<br>**3rd** [[Fireball]]<br>**1st** [[Detect Magic]], [[Force Barrage]], [[Read Aura]]"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "`pf2:2` The dragon unleashes a spray of magic-disrupting energies that deals @Damage[18d6[force]|options:area-damage] damage in a @Template[cone|distance:60] (DC 45 [[Reflex]] save). Creatures that fail become [[Stupefied 1]] ([[Stupefied 2]] on a critical failure) for 1 minute. <br>  <br> The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Drain Hoard"
    desc: "`pf2:1` **Requirements** The dragon is within 60 feet of their hoard <br>  <br> **Frequency** once per day <br>  <br> **Effect** The dragon draws power out of the magic items in their hoard, regaining all their expended spontaneous spell slots."
  - name: "Share the Wealth"
    desc: "`pf2:2` **Requirements** The dragon's body is covered in riches (this is typically the case when the dragon is first encountered) <br>  <br> **Effect** The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing @Damage[18d10[bludgeoning]|options:area-damage] damage with a DC 40 [[Reflex]] save to all creatures in a @Template[emanation|distance:50]. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "`pf2:2` **Requirements** The dragon's body isn't covered in riches and the dragon is adjacent to their hoard <br>  <br> **Effect** The dragon Strides or Burrows through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. <br>  <br> The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 38 [[Reflex]] save or be pushed 10 feet (or pushed 20 feet and knocked [[Prone]] on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fortune dragons have the innate ability to draw upon the raw magical energies that surround them. They constantly use these magical energies to empower their magical abilities and even their bodies, as the energy can heal wounds. A fortune dragon has a typical build for an arcane dragon, but their bodies sport a striking feature: their treasure. The dragon's nature of drawing upon magic causes coins, gems, and, most notably, magical items to cling to their body like iron drawn to magnets. A dragon constantly pulls magical energies from the items attached to their body and makes use of these energies to cast spells. The magical energies that flow through a fortune dragon constantly flow through the dragon's items as well, and in many cases, the items melt from the heat produced in this process. Fortune dragons are seekers of novel experiences. This desire for originality leads fortune dragons to approach visitors of other ancestries with curiosity, though this initial interest quickly wanes if a visitor lacks exciting qualities.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Fortune Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
