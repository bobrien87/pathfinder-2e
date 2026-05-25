---
type: creature
group: ["Humanoid", "Kobold"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kobold Earth Diver"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kobold"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Darkvision]], [[Tremorsense]] (imprecise) 10 feet"
languages: "Common, Petran, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +12, Nature +10, Stealth +10, Survival +8, Geology Lore +11"
abilityMods: ["+4", "+3", "+0", "+1", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +8, **Ref** +14, **Will** +11"
health:
  - name: HP
    desc: "60"
abilities_mid:
  - name: "Sinkhole"
    desc: "`pf2:2` **Requirements** The earth diver is burrowed beneath a Medium or smaller creature aboveground <br>  <br> **Effect** The earth diver creates a small sinkhole under the creature, who must attempt a DC 20 [[Reflex]] save. Regardless of the result, the target's space becomes difficult terrain. <br> - **Failure** The creature falls into the sinkhole and is [[Restrained]] until it Escapes. <br> - **Critical Failure** As failure, and the creature takes 2d8 bludgeoning damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pick +14 (`pf2:1`) (fatal d10), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, unarmed), **Damage** 1d4+10 slashing"
  - name: "Ranged strike"
    desc: "Crossbow +13 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+6 piercing"
spellcasting: []
abilities_bot:
  - name: "Pick Smash"
    desc: "`pf2:2` The kobold earth diver smashes their pick into the ground, sending debris exploding in a @Template[type:emanation|distance:5]. All creatures and unattended objects in range take @Damage[3d6[bludgeoning]|options:area-damage] damage with a DC 20 [[Reflex]] save. A creature that is [[Restrained]] by an earth diver's Sinkhole takes an additional 1d6 bludgeoning damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Kobold earth divers study the geology of the areas near their communities. The mystical influence of their community's patron or years of extensive training at digging or earth magic allow them to swiftly burrow through the ground and to feel movements in the ground beneath their feet.

Kobolds are drawn to beings and objects of power, establishing their communities near them. Once a warren has been formed, the resident kobolds construct traps and set up ambushes to deter interlopers.

```statblock
creature: "Kobold Earth Diver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
