---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sramana"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean, Requian (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +23, Athletics +29, Diplomacy +26, Medicine +27, Religion +29, Legal Lore +27"
abilityMods: ["+8", "+4", "+6", "+4", "+8", "+5"]
abilities_top:
  - name: "Heed the Fettered"
    desc: "The sramana can detect penitent creatures who wish to atone for their misdeeds, creatures with the soulbound trait, and soul gems as an imprecise sense with a range of 120 feet."
  - name: "Soul-Rescuing Vow"
    desc: "A sramana can use interplanar teleport to teleport near a truly penitent creature, soulbound creature, or soul gem of which they're aware. If they do, they don't need a planar key and arrive `r 1d20` miles away from the subject. They can also teleport to Nirvana or The Boneyard without a planar key."
armorclass:
  - name: AC
    desc: "36; **Fort** +26, **Ref** +24, **Will** +28"
health:
  - name: HP
    desc: "300; **Immunities** confused, fear effects; **Weaknesses** unholy 15; **Resistances** mental 15"
abilities_mid:
  - name: "Aura of Renunciation"
    desc: "100 feet. Truly penitent creatures in the sramana's aura are affected by a DC 35 [[Sanctuary]] spell. If any creature within the aura takes a hostile action, sanctuary ends for only that creature, not for the other creatures in the aura. <br>  <br> In addition, soul gems in the aura can't be ingested, consumed, or otherwise used. A creature who attempts to do so becomes [[Sickened]] 1 unless it succeeds at a DC 37 [[Fortitude]] save."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Khakkhara +31 (`pf2:1`) (magical, shove, two hand d10, versatile p), **Damage** 2d6+14 bludgeoning plus 2d6 spirit"
  - name: "Melee strike"
    desc: "Fist +30 (`pf2:1`) (agile, holy, nonlethal, unarmed), **Damage** 2d4+12 bludgeoning plus 2d6 poison"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29<br>**8th** [[Divine Inspiration]], [[Moment of Renewal]], [[Pinpoint]]<br>**7th** [[Divine Decree]], [[Interplanar Teleport (at will; see soul-rescuing vow)]], [[Planar Seal]]<br>**5th** [[Sending]], [[Truespeech]] (Constant)<br>**2nd** [[Calm]], [[Cleanse Affliction]], [[Clear Mind]], [[Dispel Magic]]<br>**1st** [[Daze]], [[Divine Lance]], [[Heal]], [[Light]], [[Message]], [[Vitality Lash]]"
abilities_bot:
  - name: "Shelter the Sufering"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The sramana tosses the shawl of their robes into the air, where it expands to protect the sufering. Each truly penitent creature in a @Template[type:emanation|distance:100] is affected by an [[Invisibility]] spell, and the area is affected by the feld of life spell, though it afects only penitent creatures and soulbound creatures. These efects last for 1 round but can be sustained for up to 1 hour."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sramanas, or renouncer angels, exist to help liberate the penitent and ease their suffering. Unusual for angels of such power, sramanas are drawn exclusively from compassionate and enlightened mortal souls who are often more perceptive to the pains of mortal existence.

These tireless celestials embark upon impossible tasks and unfathomable labors to free souls lost, abandoned, and imprisoned in the Lower Planes. This earns them great enmity from fiends and other callous entities, many of whom treat souls as simple playthings and currency and who ironically see the renouncer angels as thieves of souls they've "rightfully" cheated, stolen, or traffcked for their own purposes.

```statblock
creature: "Sramana"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
