---
type: creature
group: ["Arcane", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fortune Dragon (Adult, Spellcaster)"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Arcane"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Dwarven"
skills:
  - name: Skills
    desc: "Acrobatics +27, Arcana +28, Athletics +27, Crafting +28, Diplomacy +24, Thievery +27, Accounting Lore +28, Mercantile Lore +28"
abilityMods: ["+7", "+7", "+6", "+8", "+4", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "36; **Fort** +24, **Ref** +27, **Will** +24"
health:
  - name: HP
    desc: "230; **Immunities** drained, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Arcane"
    desc: ""
  - name: "Aura of Disruption"
    desc: "120 feet. <br>  <br> The dragon radiates disruptive energies that allow them to feed on magic. When a spell is counteracted or disrupted within the aura, the dragon regains one expended spontaneous spell slot and gains 25 temporary Hit Points that last for 1 minute."
  - name: "Capture Spell"
    desc: "`pf2:r` **Trigger** The dragon succeeds or critically succeeds on a saving throw against a spell <br>  <br> **Effect** The dragon attempts to capture a portion of the spell's magic to feed themself. They attempt to counteract the spell (counteract rank 7, counteract modifier +28). If successful, the dragon is unaffected by the spell and regains one expended spontaneous spell slot; other subjects are affected by the spell normally."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 3d10+13 piercing plus 1d6 force"
  - name: "Melee strike"
    desc: "Claw +27 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 1d6 force plus 3d6+13 piercing"
  - name: "Melee strike"
    desc: "Tail +25 (`pf2:1`) (magical, reach 20 ft.), **Damage** 1d6 force plus 3d10+13 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 36, attack +28<br>**6th** (3 slots) [[Cursed Metamorphosis]], [[Teleport]], [[Wall of Force]]<br>**5th** (3 slots) [[Howling Blizzard]], [[Scouting Eye]], [[Toxic Cloud]]<br>**4th** (3 slots) [[Flicker]], [[Translocate]], [[Vision of Death]]<br>**3rd** (3 slots) [[Aqueous Orb]], [[Grease]], [[Haste]]<br>**2nd** (3 slots) [[Invisibility]], [[Mist]], [[Web]]<br>**1st** (3 slots) [[Gust of Wind]], [[Item Facade]], [[Phantasmal Minion]]<br>**Cantrips** [[Electric Arc]], [[Figment]], [[Prestidigitation]], [[Shield]], [[Telekinetic Hand]]"
  - name: "Arcane Spontaneous Spells"
    desc: "DC 36, attack +22<br>**7th** (2 slots) [[Warp Mind]]<br>**6th** [[Chain Lightning]]<br>**5th** [[Slither]]<br>**4th** [[Unfettered Movement]]<br>**3rd** [[Fireball]]<br>**1st** [[Detect Magic]], [[Force Barrage]], [[Read Aura]]"
abilities_bot:
  - name: "Disruptive Breath"
    desc: "`pf2:2` The dragon unleashes a spray of magic-disrupting energies that deals @Damage[13d6[force]|options:area-damage] damage in a @Template[cone|distance:40] (DC 36 [[Reflex]] save). Creatures that fail become [[Stupefied 1]] ([[Stupefied 2]] on a critical failure) for 1 minute. <br>  <br> The dragon can't use Disruptive Breath again for 1d4 rounds."
  - name: "Share the Wealth"
    desc: "`pf2:2` **Requirements** The dragon's body is covered in riches (this is typically the case when the dragon is first encountered) <br>  <br> **Effect** The dragon shakes their body aggressively, sending coins and other riches flying in every direction, dealing @Damage[9d10[bludgeoning]|options:area-damage] damage with a DC 35 [[Reflex]] save to all creatures in a @Template[emanation|distance:40]. The dragon's body is then no longer covered in riches."
  - name: "Treasure Dive"
    desc: "`pf2:2` **Requirements** The dragon's body isn't covered in riches and the dragon is adjacent to their hoard <br>  <br> **Effect** The dragon Strides or Burrows through their hoard using their land Speed. They coat themself in coins, magic items, and other treasures. This contact with magical items revitalizes the dragon, causing them to regain one expended spontaneous spell slot. <br>  <br> The dragon can move through other creatures while moving in this way. Creatures in the dragon's path, or above it if the dragon Burrows, must succeed at a DC 33 [[Reflex]] save or be pushed 10 feet (or pushed 20 feet and knocked [[Prone]] on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fortune dragons have the innate ability to draw upon the raw magical energies that surround them. They constantly use these magical energies to empower their magical abilities and even their bodies, as the energy can heal wounds. A fortune dragon has a typical build for an arcane dragon, but their bodies sport a striking feature: their treasure. The dragon's nature of drawing upon magic causes coins, gems, and, most notably, magical items to cling to their body like iron drawn to magnets. A dragon constantly pulls magical energies from the items attached to their body and makes use of these energies to cast spells. The magical energies that flow through a fortune dragon constantly flow through the dragon's items as well, and in many cases, the items melt from the heat produced in this process. Fortune dragons are seekers of novel experiences. This desire for originality leads fortune dragons to approach visitors of other ancestries with curiosity, though this initial interest quickly wanes if a visitor lacks exciting qualities.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Fortune Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
