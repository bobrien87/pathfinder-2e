---
type: creature
group: ["Amphibious", "Azarketi"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Azarketi Crab Catcher"
level: "0"
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
    desc: "+6"
languages: "Common, Alghollthu"
skills:
  - name: Skills
    desc: "Athletics +4, Diplomacy +3, Nature +3, Stealth +5, Survival +5, Underwater Lore +4"
abilityMods: ["+2", "+3", "+2", "+0", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +9, **Will** +3"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Hydration"
    desc: "Azarketi must regularly submerge themselves in water to rehydrate their water-acclimated skin. After the first 24 hours outside of water, they gain a –1 status penalty to Fortitude saves as their skin cracks and their gills become painful. After 48 hours, they begin to suffocate until returned to water."
  - name: "Swim Away"
    desc: "`pf2:r` **Requirements** The azarketi crab catcher is swimming <br>  <br> **Trigger** The azarketi crab catcher is targeted with an attack and can see the attacker <br>  <br> **Effect** The azarketi crab catcher gains a +2 circumstance bonus to AC against the triggering attack. After the attack, they Swim 5 feet."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +7 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The average azarketi citizen in Absalom makes a living fishing or catching crabs.

Azarketis, also known as gillmen, can be found all over Golarion, with a particularly high concentration around Absalom and the Inner Sea. Descendants of the ancient Azlanti, the azarketis survived the cataclysm of Earthfall by fleeing into the ocean, where they were warped into amphibious forms by the alghollthu.

```statblock
creature: "Azarketi Crab Catcher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
