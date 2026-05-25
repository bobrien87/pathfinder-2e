---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Empyreal Dragon (Young, Spellcaster)"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]], [[Lifesense]] (imprecise) 30 feet, [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +22, Diplomacy +20, Intimidation +20, Medicine +21, Religion +21, Society +19, Heaven Lore +21"
abilityMods: ["+6", "+3", "+4", "+3", "+5", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "30; **Fort** +18, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "170; **Immunities** fear effects, paralyzed, sleep; **Weaknesses** unholy 10"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine"
    desc: ""
  - name: "Divine Deflection"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by an attack <br>  <br> **Effect** Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
  - name: "Inspiring Presence"
    desc: "20 feet. <br>  <br> The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +22 (`pf2:1`) (holy, magical, reach 10 ft., unarmed), **Damage** 1d8 spirit plus 2d10+9 piercing"
  - name: "Melee strike"
    desc: "Claws +22 (`pf2:1`) (agile, holy, magical), **Damage** 2d8+9 slashing plus 1d8 spirit"
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (holy, magical, reach 15 ft.), **Damage** 1d8 spirit plus 2d10+9 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +20 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 1d8 spirit plus 1d10+9 slashing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 29, attack +22<br>**4th** (3 slots) [[Dispel Magic]], [[Unfettered Movement]], [[Vital Beacon]]<br>**3rd** (3 slots) [[Bind Undead]], [[Ring of Truth]], [[Sound Body]]<br>**2nd** (3 slots) [[Clear Mind]], [[Everlight]], [[Share Life]]<br>**1st** (3 slots) [[Bless]], [[Mending]], [[Sanctuary]]<br>**Cantrips** [[Detect Magic]], [[Divine Lance]], [[Guidance]], [[Shield]], [[Stabilize]]"
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Holy Light]] (At Will)<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Direct Halo"
    desc: "`pf2:1` The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Halo Pulse"
    desc: "`pf2:2` The dragon chooses one effect to impose on creatures in their inspiring presence aura. <br>  <br> The dragon can't use Halo Pulse again for 1d4 rounds. <br>  <br> - **Repulsion** Each creature must succeed at a DC 29 [[Fortitude]] save or be pushed until it's no longer in the aura. <br>  <br> - **Restoration** (healing, vitality) Each creature recovers 5d8 Hit Points."
  - name: "Spirit Breath"
    desc: "`pf2:2` The dragon unleashes a blast of holy fire that deals @Damage[9d8[spirit]|options:area-damage] damage in a @Template[cone|distance:40] (DC 29 [[Reflex]] save). <br>  <br> The dragon can't use Spirit Breath again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The three major celestial planes—Heaven, Nirvana, and Elysium—each have their own respective dragons. Empyreal dragons have a direct connection to Heaven. Using the blessings of Heaven, empyreal dragons protect others and intercede against wickedness. Empyreal dragons are wise, considerate, and compassionate. When speaking with others, empyreal dragons are patient and understanding.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Empyreal Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
