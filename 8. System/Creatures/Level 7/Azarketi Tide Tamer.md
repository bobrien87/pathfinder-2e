---
type: creature
group: ["Amphibious", "Azarketi"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Azarketi Tide Tamer"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Azarketi"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15"
languages: "Common, Alghollthu"
skills:
  - name: Skills
    desc: "Athletics +15, Intimidation +15, Nature +12, Stealth +15, Survival +14, Underwater Lore +11"
abilityMods: ["+4", "+4", "+2", "+0", "+1", "+2"]
abilities_top:
  - name: "Aquatic Predator"
    desc: "An azarketi deals 2d8 additional damage on a successful weapon Strike while they are underwater."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +18, **Will** +12"
health:
  - name: HP
    desc: "115"
abilities_mid:
  - name: "Hydration"
    desc: "Azarketi must regularly submerge themselves in water to rehydrate their water-acclimated skin. After the first 24 hours outside of water, they gain a –1 status penalty to Fortitude saves as their skin cracks and their gills become painful. After 48 hours, they begin to suffocate until returned to water."
  - name: "Speaker of the Oceans"
    desc: "An azarketi tide tamer can speak with animals that have the aquatic or amphibious trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +18 (`pf2:1`), **Damage** 1d8+7 piercing"
  - name: "Melee strike"
    desc: "Trident +18 (`pf2:1`) (thrown 20), **Damage** 1d8+7 piercing"
  - name: "Ranged strike"
    desc: "Hand Crossbow +17 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The most ambitious and capable azarketis become tide tamers, learning how to speak with and train aquatic animals.

Azarketis, also known as gillmen, can be found all over Golarion, with a particularly high concentration around Absalom and the Inner Sea. Descendants of the ancient Azlanti, the azarketis survived the cataclysm of Earthfall by fleeing into the ocean, where they were warped into amphibious forms by the alghollthu.

```statblock
creature: "Azarketi Tide Tamer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
