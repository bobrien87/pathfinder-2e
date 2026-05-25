---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Choral"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +12, Diplomacy +15, Performance +17, Religion +14"
abilityMods: ["+1", "+4", "+2", "+3", "+4", "+5"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Deafening Aria"
    desc: "On a critical hit with piercing hymn, the target is [[Deafened]] for one minute."
armorclass:
  - name: AC
    desc: "24; **Fort** +10, **Ref** +14, **Will** +16"
health:
  - name: HP
    desc: "100; **Weaknesses** unholy 5; **Resistances** sonic 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Harmonizing Aura"
    desc: "20 feet. <br>  <br> Allies in the aura gain a +2 status bonus to sonic damage rolls and a +1 status bonus to AC and all saves against effects with the auditory or sonic trait. Enemies in the aura take a –2 status penalty to sonic damage rolls and a –1 status penalty to AC and all saves against sonic and auditory effects."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, holy, magical, unarmed), **Damage** 2d6+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Piercing Hymn +17 (`pf2:1`) (holy, magical, sonic), **Damage** 4d6 sonic plus [[Deafening Aria]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15<br>**5th** [[Truespeech]] (Constant)<br>**2nd** [[Cleanse Affliction]], [[Clear Mind]] (At Will), [[Invisibility (At Will) (Self Only)]], [[Noise Blast]], [[Noise Blast]] (At Will)<br>**1st** [[Counter Performance]] (At Will), [[Courageous Anthem]], [[Heal]], [[Uplifting Overture]]"
abilities_bot:
  - name: "Harmonize"
    desc: "`pf2:1` The choral angel lends their harmony to a choral angel ally within their harmonizing aura. <br>  <br> The ally can, on their next turn, expend their 3rd-rank [[Noise Blast]] to instead cast [[Calm]], [[Heroism]], or 4th-rank *noise blast*. <br>  <br> If the ally is benefiting from 5 or more chorals' Harmonize actions, they can instead choose [[Divine Decree]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Choral angels are incredible singers who fill the halls of Nirvana with pious chants and sacred hymns. Most form from the souls of talented bards and other performers, though anyone who takes superlative joy in music might ascend to their ranks. Though their duties are typically to spread peace and joy through their music, their holy incantations also brim with mystic purpose, their songs bolstering angelic wards and strengthening the very fabric of the celestial planes themselves.

While choral angels shy away from conflict, they will brave the mortal realm to deliver good omens and auspicious messages. Choral angels often serve the goddess Shelyn, but they can also serve other good deities and empyreal lords.

The celestial hosts of angels are messengers and warriors, divided into choirs based on their abilities and purviews. Angels were one of the first creations of the gods, and many still assist their righteous creators throughout the cosmos. Most angels in modern times are not direct creations of the divine, however, instead consisting of ascended mortal souls drawn from the celestial planes.

The majority of unaffiliated angels live in Nirvana, the plane of virtue and enlightenment. Angels who are affiliated with deities dwell in those deities' domains or other areas where that god holds influence. Regardless of residence or service, angels remain benevolent messengers possessed with magical auras to aid their allies.

```statblock
creature: "Choral"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
