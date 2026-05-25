---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Deep One Hybrid"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Arcana +4, Athletics +4, Deception +5, Religion +7, Society +4, Dagon Lore +6"
abilityMods: ["+1", "+1", "+2", "+1", "+4", "+0"]
abilities_top:
  - name: "Natural Swimmer"
    desc: "The deep one hybrid can hold their breath underwater for 10 minutes and gains a +2 circumstance bonus to initiative rolls and Reflex saves while swimming."
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +5, **Will** +9"
health:
  - name: HP
    desc: "20; **Resistances** piercing 2"
abilities_mid:
  - name: "Ocean's Call"
    desc: "A deep one hybrid that remains 10 or more miles from the sea for 24 hours becomes [[Stupefied 1]]. This effect is removed only once the hybrid returns to the sea."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +4 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Dagger +4 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Trident +4 (`pf2:1`), **Damage** 1d8+1 piercing"
  - name: "Melee strike"
    desc: "Trident +4 (`pf2:1`) (thrown 20), **Damage** 1d8+1 piercing"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 17, attack +9<br>**1st** (7 slots) [[Bless]], [[Fear]], [[Harm]], [[Harm]], [[Harm]], [[Harm]], [[Heal]]<br>**Cantrips** [[Bullhorn]], [[Daze]], [[Haunting Hymn]], [[Light]], [[Void Warp]]"
  - name: "Cleric Domain Spells"
    desc: "DC 17, attack +0<br>**1st** [[Tidal Surge]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Whether from their devout faith to Dagon or their own biological lineage, some humans display physical indicators of their connection to deep ones.

Lumbering, amphibious, and deathless humanoids known as deep ones inhabit coastal areas and deep ocean trenches all across Golarion. Though most simply wish to be left alone, others work tirelessly to grow their ranks.

```statblock
creature: "Deep One Hybrid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
