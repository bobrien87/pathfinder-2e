---
type: creature
group: ["Aquatic", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Merfolk Wavecaller"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aquatic"
trait_02: "Humanoid"
trait_03: "Merfolk"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +7, Deception +6, Nature +8, Religion +8"
abilityMods: ["+3", "+2", "+0", "+1", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +6, **Ref** +6, **Will** +10"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, versatile s), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Dagger +9 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+3 piercing"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (3 slots) [[Charm]], [[Heal]], [[Hydraulic Push]]<br>**Cantrips** [[Detect Magic]], [[Electric Arc]], [[Frostbite]], [[Light]], [[Stabilize]]"
abilities_bot:
  - name: "Hydraulic Asphyxiation"
    desc: "`pf2:1` **Requirements** The target is fully submerged in water, within 30 feet of the merfolk wavecaller, and holding its breath <br>  <br> **Effect** The merfolk wavecaller commands the tides to crush their foe's throat, rooting the target in place and forcing it to choke up precious air. The target must succeed at a DC 18 [[Fortitude]] save or become [[Immobilized]] for 1 round and immediately lose 1d4 rounds' worth of air (or twice that on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Merfolk wavecallers use their primal magic to defend their people. Their ability to asphyxiate airbreathers makes them crucial when surface dwellers invade.

Elegant, mysterious, and graceful; all this and more can be said of merfolk. These enigmatic people resemble humanoids with delicate features from the waist up but with the fins and tail of a massive fish from the waist down. Found in nearly all of Golarion's oceans, merfolk are as varied in appearance as humans, their skin ranging from pale to umber and all shades in between, while their gleaming scales shimmer with the majesty of the sea.

```statblock
creature: "Merfolk Wavecaller"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
