---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ankhrav Hive Mother"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Tremorsense]] (imprecise) 90 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +20, Stealth +11, Survival +16"
abilityMods: ["+6", "+1", "+4", "-4", "+2", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "29; **Fort** +18, **Ref** +15, **Will** +14"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +20 (`pf2:1`) (acid), **Damage** 2d8+6 piercing plus 2d6 acid"
  - name: "Ranged strike"
    desc: "Acid Spit +17 (`pf2:1`) (acid), **Damage** 5d6 acid"
spellcasting: []
abilities_bot:
  - name: "Armor-Rending Bite"
    desc: "`pf2:2` The hive mother makes a mandibles Strike; if the Strike hits, the target's armor takes the damage and the acid damage bypasses the armor's Hardness."
  - name: "Frenzy Pheromone"
    desc: "`pf2:2` The hive mother unleashes a pheromone that causes all other ankhravs within a @Template[emanation|distance:100] to become [[Quickened]] until the start of the hive mother's next turn, and they can use the extra action only for Burrow, Stride, or Strike actions. <br>  <br> The hive mother can't unleash the pheromone again for 1d4 rounds."
  - name: "Spray Acid"
    desc: "`pf2:2` The hive mother spews acid in a @Template[cone|distance:60], dealing @Damage[8d6[acid],1d6[persistent,acid]|options:area-damage]{8d6 acid damage and 1d6 persistent acid damage} (DC 26 [[Reflex]] save). <br>  <br> It can't spew acid again for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Ankhrav hive mothers are fearsome predators that one can easily distinguish from the typical ankhrav not only by their greater size, but the presence of a large pair of razor-sharp, mantis-like arms.

Ankhravs are immense, burrowing, and insectile predators, considered by inhabitants of the rural areas of the world to be an all-too-common plague.

```statblock
creature: "Ankhrav Hive Mother"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
