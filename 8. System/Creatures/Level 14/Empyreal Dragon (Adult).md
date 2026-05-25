---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Empyreal Dragon (Adult)"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]], [[Lifesense]] (imprecise) 30 feet, [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean, Chthonian, Diabolic (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +26, Athletics +28, Diplomacy +25, Intimidation +25, Medicine +28, Religion +28, Society +24, Heaven Lore +26"
abilityMods: ["+8", "+4", "+6", "+4", "+7", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Spirit Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "36; **Fort** +24, **Ref** +24, **Will** +26"
health:
  - name: HP
    desc: "250; **Immunities** fear effects, paralyzed, sleep; **Weaknesses** unholy 10"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine"
    desc: ""
  - name: "Divine Deflection"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by an attack <br>  <br> **Effect** Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
  - name: "Inspiring Presence"
    desc: "40 feet. <br>  <br> The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +28 (`pf2:1`) (holy, magical, reach 15 ft., unarmed), **Damage** 1d8 spirit plus 3d10+11 piercing"
  - name: "Melee strike"
    desc: "Claws +28 (`pf2:1`) (agile, holy, reach 10 ft.), **Damage** 3d8+11 slashing plus 1d8 spirit"
  - name: "Melee strike"
    desc: "Tail +26 (`pf2:1`) (holy, reach 20 ft.), **Damage** 1d8 spirit plus 3d10+11 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +26 (`pf2:1`) (agile, holy, reach 15 ft.), **Damage** 1d8 spirit plus 2d10+11 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +26<br>**7th** [[Interplanar Teleport (At Will, Self Only)]]<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Holy Light]] (At Will)<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Direct Halo"
    desc: "`pf2:1` The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Halo Pulse"
    desc: "`pf2:2` The dragon chooses one effect to impose on creatures in their inspiring presence aura. <br>  <br> The dragon can't use Halo Pulse again for 1d4 rounds. <br>  <br> - **Repulsion** Each creature must succeed at a DC 34 [[Fortitude]] save or be pushed until it's no longer in the aura. <br>  <br> - **Restoration** (healing, vitality) Each creature recovers 7d8 Hit Points."
  - name: "Spirit Breath"
    desc: "`pf2:2` The dragon unleashes a blast of holy fire that deals @Damage[12d8[spirit]|options:area-damage] damage in a @Template[cone|distance:50] (DC 34 [[Reflex]] save). <br>  <br> The dragon can't use Spirit Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The three major celestial planes—Heaven, Nirvana, and Elysium—each have their own respective dragons. Empyreal dragons have a direct connection to Heaven. Using the blessings of Heaven, empyreal dragons protect others and intercede against wickedness. Empyreal dragons are wise, considerate, and compassionate. When speaking with others, empyreal dragons are patient and understanding.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Empyreal Dragon (Adult)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
