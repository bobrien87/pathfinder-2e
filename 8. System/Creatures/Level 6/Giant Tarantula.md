---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Tarantula"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +16, Stealth +11"
abilityMods: ["+6", "+1", "+5", "-5", "+2", "-4"]
abilities_top:
  - name: "Giant Tarantula Venom"
    desc: "**Saving Throw** DC 23 [[Fortitude]] save <br>  <br> **Maximum Duration** 8 rounds <br>  <br> **Stage 1** 1d10 poison damage (1 round) <br>  <br> **Stage 2** 1d12 poison damage, [[Clumsy]] 1, and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 2d6 poison damage, [[Clumsy]] 2, and off-guard (1 round) <br>  <br> **Stage 4** 2d6 poison damage and [[Paralyzed]] (1 round)"
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +13, **Will** +10"
health:
  - name: HP
    desc: "135"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +17 (`pf2:1`), **Damage** 2d8+8 piercing plus [[Giant Tarantula Venom]]"
  - name: "Melee strike"
    desc: "Leg +17 (`pf2:1`) (reach 10 ft.), **Damage** 1d12+8 bludgeoning plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Hair Barrage"
    desc: "`pf2:2` The tarantula flicks its legs, flinging spiky hairs in a @Template[cone|distance:15]. This deals @Damage[4d6[piercing]|options:area-damage] damage with a DC 25 [[Reflex]] save."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tarantulas are ambush predators, but will attack prey in the open.

Few everyday vermin inspire as much dread as the infamous spider.

```statblock
creature: "Giant Tarantula"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
