---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elemental Avalanche"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Tremorsense]] (imprecise) 90 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +24, Stealth +14"
abilityMods: ["+7", "-1", "+8", "+0", "+3", "-1"]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the elemental avalanche is [[Slowed]] 1, can't use reactions, and can't Trample."
  - name: "Earth Glide"
    desc: "The elemental avalanche can Burrow through any earthen matter, including rock. When it does so, the elemental avalanche moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "32; **Fort** +26, **Ref** +17, **Will** +21"
health:
  - name: HP
    desc: "215; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Crumble"
    desc: "`pf2:r` **Trigger** The elemental avalanche takes damage from a hostile source while atop rock or earth <br>  <br> **Effect** The elemental avalanche crumbles into the ground, Burrowing down 20 feet. This Burrowing does not trigger reactions. <br>  <br> The elemental avalanche can't Crumble again for 1d4 rounds."
  - name: "Spike Stones"
    desc: "10 feet. <br>  <br> Spikes of rock rise up from all stone surfaces in the emanation, creating difficult terrain. A creature moving in the terrain takes 2d8 piercing damage for each square of spikes it moves into (a Large or larger creature takes damage only once for each square it moves, even if its space covers multiple squares of spikes). Creatures with the earth trait ignore all effects within the area. <br>  <br> The elemental avalanche can disable or activate this aura using a single action, which has the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (reach 20 ft., unarmed), **Damage** 2d12+11 bludgeoning plus [[Knockdown]]"
  - name: "Ranged strike"
    desc: "Rock +24 (`pf2:1`) (brutal, range 80 ft.), **Damage** 2d12+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Grinding Stones"
    desc: "`pf2:2` The elemental avalanche deals 4d12 bludgeoning damage to each [[Prone]] creature within the elemental's melee reach with a DC 30 [[Reflex]] save."
  - name: "Trample"
    desc: "`pf2:3` Large or smaller, fist, DC 30 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Stubborn and ponderous, elemental avalanches are massive beings of living rock and dirt. Once their ire is raised, they will take the shortest route to resolving the problem, usually by burying it in rock.

Earth elementals make excellent bodyguards for adventuresome spelunkers and are ideal protectors of important subterranean locations such as vaults and treasuries.

```statblock
creature: "Elemental Avalanche"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
