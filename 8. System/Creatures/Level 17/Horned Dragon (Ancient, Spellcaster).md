---
type: creature
group: ["Amphibious", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Horned Dragon (Ancient, Spellcaster)"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Amphibious"
trait_02: "Dragon"
trait_03: "Primal"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Elven, Fey, Chthonian, Jotun"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +32, Athletics +30, Deception +27, Diplomacy +31, Intimidation +31, Nature +28, Occultism +34, Society +31, Stealth +29, Forest Lore +31"
abilityMods: ["+7", "+4", "+5", "+6", "+5", "+6"]
abilities_top:
  - name: "Camouflage"
    desc: "The dragon can Hide in natural environments even if they don't have cover."
  - name: "Forest Passage"
    desc: "The horned dragon ignores any difficult terrain caused by plants, such as bushes, vines, and undergrowth. Even plants manipulated by magic don't impede their progress."
  - name: "Trackless Journey"
    desc: "The horned dragon always gains the benefits of Cover Tracks in natural surroundings, even while moving at full speed."
armorclass:
  - name: AC
    desc: "41; **Fort** +30, **Ref** +29, **Will** +32"
health:
  - name: HP
    desc: "315; **Immunities** paralyzed, poison, sleep"
abilities_mid:
  - name: "+1 Status to All Saves vs. Primal"
    desc: ""
  - name: "Frightful Presence"
    desc: "90 feet. DC 37 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Miasma"
    desc: "20 feet. <br>  <br> After the dragon uses their Poison Breath, a cloud of poison gas continues to emanate from their body for 1 round. Any creature that ends its turn in the miasma takes @Damage[4d6[poison]|options:area-damage] damage (DC 37 [[Fortitude]] save). <br>  <br> Any creature in the miasma is [[Concealed]] and treats other creatures as concealed. The dragon can see through this concealment."
  - name: "Twisting Tail"
    desc: "`pf2:r` **Trigger** A creature within reach of the dragon's tail uses a move action or leaves a square during a move action it's using <br>  <br> **Effect** The dragon makes a tail Strike at the creature with a –2 penalty. If the Strike hits, the dragon disrupts the creature's action."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +33 (`pf2:1`) (magical, poison, reach 20 ft., unarmed), **Damage** 3d12+15 piercing plus 4d4 poison"
  - name: "Melee strike"
    desc: "Claw +33 (`pf2:1`) (agile, magical, reach 15 ft., unarmed), **Damage** 3d10+15 slashing"
  - name: "Melee strike"
    desc: "Tail +31 (`pf2:1`) (magical, reach 25 ft.), **Damage** 3d10+13 bludgeoning"
  - name: "Melee strike"
    desc: "Horn +31 (`pf2:1`) (magical, reach 20 ft., unarmed), **Damage** 2d10+13 piercing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 39, attack +33<br>**8th** (2 slots) [[Desiccate]], [[Punishing Winds]]<br>**7th** (3 slots) [[Execute]], [[Mask of Terror]], [[Veil of Privacy]]<br>**6th** (3 slots) [[Field of Life]], [[Tangling Creepers]], [[Truesight]]<br>**5th** (3 slots) [[Dispel Magic]], [[Toxic Cloud]], [[Veil of Privacy]]<br>**4th** (3 slots) [[Hydraulic Torrent]], [[Mountain Resilience]], [[Unfettered Movement]]<br>**3rd** (4 slots) [[Dispel Magic]], [[Slow]], [[Veil of Privacy]], [[Wall of Thorns]]<br>**2nd** (3 slots) [[Humanoid Form]], [[One with Plants]], [[Sound Body]]<br>**1st** (3 slots) [[Gust of Wind]], [[Vanishing Tracks]], [[Ventriloquism]]<br>**Cantrips** [[Detect Magic]], [[Know the Way]], [[Light]], [[Read Aura]], [[Tangle Vine]]"
  - name: "Primal Innate Spells"
    desc: "DC 39, attack +31<br>**6th** [[Dominate]]<br>**4th** [[Suggestion]]<br>**2nd** [[Entangling Flora]] (At Will)<br>**1st** [[Charm]] (At Will)"
abilities_bot:
  - name: "Impaling Charge"
    desc: "`pf2:2` **Requirements** The dragon doesn't have a creature impaled on their horn <br>  <br> **Effect** The dragon attempts to gore a foe. They Stride, then attempt a horn Strike. On a hit, the target becomes impaled on the dragon's horn. The creature is [[Grabbed]] while on the horn (and can attempt to [[Escape]] as normal). The dragon doesn't need to use additional actions to keep the impaled creature grabbed. If the dragon moves, they bring the grabbed creature along with them."
  - name: "Poison Breath"
    desc: "`pf2:2` The dragon breathes a toxic cloud that deals @Damage[18d6[poison]|options:area-damage] damage in a @Template[cone|distance:60] (DC 37 [[Fortitude]] save). <br>  <br> They can't use Poison Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The magic that flows through primal dragons can manifest more animalistic or bestial features in a given type of dragon. Notably among these are the massive paired horns of the horned dragon. While their bulky frames, natural coloration, and prominent ridged scales are all remarkable in their own way, it's the horns that are most obvious and striking at first glance. Horned dragons use their horns to impale their prey in a quick and brutal display of their might. They are generally contemplative and have a fixation on knowledge and self-discipline, traits belied by their bestial appearance. As a result, horned dragons are generally more open to speaking with outsiders.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Horned Dragon (Ancient, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
