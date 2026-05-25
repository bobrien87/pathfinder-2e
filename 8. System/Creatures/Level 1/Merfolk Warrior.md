---
type: creature
group: ["Aquatic", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Merfolk Warrior"
level: "1"
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
    desc: "+6; [[Low-Light Vision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +5, Medicine +4"
abilityMods: ["+2", "+4", "+1", "+1", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +9, **Will** +4"
health:
  - name: HP
    desc: "19"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +7 (`pf2:1`), **Damage** 1d8+2 piercing"
  - name: "Melee strike"
    desc: "Trident +9 (`pf2:1`) (thrown 20), **Damage** 1d8+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Aquatic Dash"
    desc: "`pf2:2` The merfolk warrior swims and attacks in one of two patterns. They either Swim twice and Strike at the end of their movement, or Swim once and Strike at any point during their movement."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Merfolk warriors form the bulk of the militias of their vast underwater realms and meet potential aggressors head-on with uncompromising force.

Elegant, mysterious, and graceful; all this and more can be said of merfolk. These enigmatic people resemble humanoids with delicate features from the waist up but with the fins and tail of a massive fish from the waist down. Found in nearly all of Golarion's oceans, merfolk are as varied in appearance as humans, their skin ranging from pale to umber and all shades in between, while their gleaming scales shimmer with the majesty of the sea.

```statblock
creature: "Merfolk Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
