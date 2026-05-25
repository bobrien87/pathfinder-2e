---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jotunborn Sage"
level: "2"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Jotunborn"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Low-Light Vision]]"
languages: "Common, Cyclops, Fey, Jotun, Petran, Shadowtongue"
skills:
  - name: Skills
    desc: "Arcana +8, Athletics +6, Diplomacy +4, Medicine +5, Occultism +8, Religion +5, Society +8, Jotunborn Lore +8"
abilityMods: ["+2", "+0", "+2", "+4", "+1", "+0"]
abilities_top:
  - name: "Iivlar Weaving"
    desc: "The sage has planar thread woven into their skin. This thread glows with dim light in a @Template[type:emanation|distance:10]. They can Sustain to extinguish, reactivate, or adjust the coloration of this light."
armorclass:
  - name: AC
    desc: "16; **Fort** +8, **Ref** +4, **Will** +9"
health:
  - name: HP
    desc: "26"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +10 (`pf2:1`) (agile, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (3 slots) [[Dizzying Colors]], [[Grim Tendrils]], [[Sleep]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Read Aura]], [[Shield]], [[Telekinetic Projectile]], [[Void Warp]]"
abilities_bot:
  - name: "Plane-Hopper Dash"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The jotunborn sage moves with swiftness between planar boundaries to shorten their journey. The sage Strides; this movement doesn't trigger reactions. Once the Stride is complete, the sage gains a +5-status bonus to their Speed until the start of their next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Jotunborn are large humanoids with indirect connections to ancient giants like titans. In ancient days, jotunborn served the gods as custodians for new worlds. They lived in a sub-planar realm between the mortal Universe and the Ethereal Plane known as the Fray, and they emerged as necessary to tend to the worlds they watched over. These planar associations granted jotunborn unique abilities, including the ability to travel between planes and shaping the physical aspects of the Universe. At present, many jotunborn have found their planar abilities diminished or disrupted, and they're now more common in the Universe.

The original abilities of jotunborn have diminished in power over time. What was once a people capable of teleportation at great distances or the ability to reshape mountain ranges, is now a group that has minor magical abilities. These abilities can grow in power, however, usually as a jotunborn ages, becomes more attuned to planar energies, or weaves more iivlar silk into their skin. Particularly skilled jotunborn mages and warriors are capable of feats that rival those of their forebears.

Jotunborn who live in the mortal Universe tend to lead reclusive lives. Many other ancestries confuse jotunborn with frost giants or cloud giants due to a jotunborn's size and skin coloration. This confusion can lead to fear or hostility, a reaction that most jotunborn prefer to avoid. Due to the difficulties that come with living in the Fray, many jotunborn are fiercely loyal to those they trust. These loyalties help keep fellow jotunborn alive, and these sentiments extend to any other people that befriend a jotunborn.

In jotunborn society, sages are keepers of knowledge. They maintain histories of their clans or entire civilizations. Their weavings tend to appear along their eyes and ears, representing their observational skills and knowledge they retain.

```statblock
creature: "Jotunborn Sage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
