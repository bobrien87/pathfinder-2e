---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Horned Dragon (Adult, Spellcaster)"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Elven, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +19, Arcana +22, Athletics +24, Deception +19, Diplomacy +23, Intimidation +23, Nature +20, Occultism +24, Society +22, Stealth +21, Forest Lore +22"
abilityMods: ["+6", "+3", "+3", "+4", "+4", "+5"]
abilities_top:
  - name: "Forest Passage"
    desc: "The horned dragon ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth. Even plants manipulated by magic don't impede their progress."
  - name: "Trackless Journey"
    desc: "The horned dragon always gains the benefits of Cover Tracks in natural surroundings, even while moving at full speed."
armorclass:
  - name: AC
    desc: "34; **Fort** +20, **Ref** +22, **Will** +23"
health:
  - name: HP
    desc: "215; **Immunities** paralyzed, poison, sleep"
abilities_mid:
  - name: "+1 Status to All Saves vs. Primal"
    desc: ""
  - name: "Frightful Presence"
    desc: "90 feet. DC 31 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Twisting Tail"
    desc: "`pf2:r` **Trigger** A creature within reach of the dragon's tail uses a move action or leaves a square during a move action it's using <br>  <br> **Effect** The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (magical, poison, reach 15 ft., unarmed), **Damage** 3d10+12 piercing plus 3d4 poison"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 3d8+12 slashing"
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d8+10 bludgeoning"
  - name: "Melee strike"
    desc: "Horn +24 (`pf2:1`) (magical, reach 15 ft., unarmed), **Damage** 2d8+10 piercing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 33, attack +26<br>**5th** (3 slots) [[Dispel Magic]], [[Toxic Cloud]], [[Veil of Privacy]]<br>**4th** (3 slots) [[Hydraulic Torrent]], [[Mountain Resilience]], [[Unfettered Movement]]<br>**3rd** (4 slots) [[Dispel Magic]], [[Slow]], [[Veil of Privacy]], [[Wall of Thorns]]<br>**2nd** (3 slots) [[Humanoid Form]], [[One with Plants]], [[Sound Body]]<br>**1st** (3 slots) [[Gust of Wind]], [[Vanishing Tracks]], [[Ventriloquism]]<br>**Cantrips** [[Detect Magic]], [[Know the Way]], [[Light]], [[Read Aura]], [[Tangle Vine]]"
  - name: "Primal Innate Spells"
    desc: "DC 32, attack +24<br>**4th** [[Suggestion]]<br>**2nd** [[Entangling Flora]]<br>**1st** [[Charm]] (At Will)"
abilities_bot:
  - name: "Impaling Charge"
    desc: "`pf2:2` **Requirements** The dragon doesn't have a creature impaled on their horn <br>  <br> **Effect** The dragon attempts to gore a foe. They Stride, then attempt a horn Strike. On a hit, the target becomes impaled on the dragon's horn. The creature is [[Grabbed]] while on the horn (and can attempt to [[Escape]] as normal). The dragon doesn't need to use additional actions to keep the impaled creature grabbed. If the dragon moves, they bring the grabbed creature along with them."
  - name: "Poison Breath"
    desc: "`pf2:2` The dragon breathes a toxic cloud that deals @Damage[13d6[poison]|options:area-damage] damage in a @Template[cone|distance:50] (DC 31 [[Fortitude]] save). <br>  <br> They can't use Poison Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The magic that flows through primal dragons can manifest more animalistic or bestial features in a given type of dragon. Notably among these are the massive paired horns of the horned dragon. While their bulky frames, natural coloration, and prominent ridged scales are all remarkable in their own way, it's the horns that are most obvious and striking at first glance. Horned dragons use their horns to impale their prey in a quick and brutal display of their might. They are generally contemplative and have a fixation on knowledge and self-discipline, traits belied by their bestial appearance. As a result, horned dragons are generally more open to speaking with outsiders.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Horned Dragon (Adult, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
