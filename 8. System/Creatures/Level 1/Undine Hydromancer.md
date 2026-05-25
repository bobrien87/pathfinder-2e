---
type: creature
group: ["Amphibious", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Undine Hydromancer"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Undine"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Arcana +3, Athletics +3, Diplomacy +7, Intimidation +7, Nature +5, Survival +5"
abilityMods: ["+0", "+2", "+1", "+0", "+2", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +5, **Will** +7"
health:
  - name: HP
    desc: "15"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4 piercing"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4 piercing"
spellcasting:
  - name: "Primal Spontaneous Spells"
    desc: "DC 17, attack +9<br>**1st** (3 slots) [[Caustic Blast]], [[Create Water]], [[Detect Magic]], [[Heal]], [[Hydraulic Push]], [[Know the Way]], [[Stabilize]], [[Tangle Vine]]"
  - name: "Primal Focus Spells"
    desc: "DC 17, attack +9<br>**1st** [[Elemental Toss]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Undines are infused with elemental water-the churning power of the briny deep flows through them. These planar scions are often athletic and lithe, but they are easily distracted by auditory sensations because of how much louder and clearer sound rings above the waves.

Undines are perhaps the most settled of all geniekin, often forming communities along the coast or even on the water itself. In the latter case, they prefer to settle in ship-towns that sometimes number dozens of vessels in all shapes and sizes. The undines who fill these communities are similarly diverse, bringing aspects of multiple cultures together to form one whole. Ship-towns are permanent, but fluid-they grow, recede, and migrate constantly as undine families add their ships to or remove them from the flotilla. An undine town like this may remain at sea for years, its residents coming ashore only on rare occasions to collect wood for cookfires or to repair their homes. The paradoxically ever-shifting permanence of these communities reflects the undine virtues of adaptability and freedom, while also maintaining the prime importance of the community.

Undine hydromancers are quite valued on these floating settlements, if only for their ability to create fresh drinking water while adrift on the sea.

```statblock
creature: "Undine Hydromancer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
