---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Empyreal Dragon (Ancient)"
level: "19"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+35; [[Darkvision]], [[Lifesense]] (imprecise) 30 feet, [[Scent]] (imprecise) 60 feet"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean, Fey, Necril (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +31, Athletics +35, Diplomacy +31, Intimidation +31, Medicine +35, Religion +32, Society +30, Heaven Lore +32"
abilityMods: ["+8", "+4", "+6", "+4", "+7", "+5"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Spirit Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "43; **Fort** +31, **Ref** +31, **Will** +35"
health:
  - name: HP
    desc: "350; **Immunities** fear effects, paralyzed, sleep; **Weaknesses** unholy 15"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine"
    desc: ""
  - name: "Divine Deflection"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by an attack <br>  <br> **Effect** Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
  - name: "Inspiring Presence"
    desc: "60 feet. <br>  <br> The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +35 (`pf2:1`) (holy, magical, reach 20 ft., unarmed), **Damage** 1d8 spirit plus 4d10+16 piercing"
  - name: "Melee strike"
    desc: "Claws +35 (`pf2:1`) (agile, holy, magical, reach 15 ft.), **Damage** 4d8+16 slashing plus 1d8 spirit"
  - name: "Melee strike"
    desc: "Tail +33 (`pf2:1`) (holy, magical, reach 25 ft.), **Damage** 1d8 spirit plus 4d10+16 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +26 (`pf2:1`) (agile, holy, reach 20 ft.), **Damage** 1d8 spirit plus 3d10+16 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 41, attack +33<br>**7th** [[Interplanar Teleport (At Will, Self Only)]]<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Holy Light]] (At Will)<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Direct Halo"
    desc: "`pf2:1` The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Halo Pulse"
    desc: "`pf2:2` The dragon chooses one effect to impose on creatures in their inspiring presence aura. <br>  <br> The dragon can't use Halo Pulse again for 1d4 rounds. <br>  <br> - **Repulsion** Each creature must succeed at a DC 41 [[Fortitude]] save or be pushed until it's no longer in the aura. <br>  <br> - **Restoration** (healing, vitality) Each creature recovers 9d8 Hit Points. <br>  <br> - **Restriction** (incapacitation, mental) Creatures must succeed at a DC 41 [[Will]] save or be [[Slowed]] 1 ([[Slowed]] 2 on a critical failure) while they remain within the aura. Regardless of the result, a creature is then temporarily immune to restriction for 1 minute."
  - name: "Spirit Breath"
    desc: "`pf2:2` The dragon unleashes a blast of holy fire that deals @Damage[16d8[spirit]|options:area-damage] damage in a @Template[cone|distance:50] (DC 41 [[Reflex]] save). <br>  <br> The dragon can't use Spirit Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The three major celestial planes—Heaven, Nirvana, and Elysium—each have their own respective dragons. Empyreal dragons have a direct connection to Heaven. Using the blessings of Heaven, empyreal dragons protect others and intercede against wickedness. Empyreal dragons are wise, considerate, and compassionate. When speaking with others, empyreal dragons are patient and understanding.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

```statblock
creature: "Empyreal Dragon (Ancient)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
